#!/usr/bin/env python3
"""
Arabic Audiobook Generator
Converts extracted OCR text into a clean audiobook with subtitles.

Requirements:
    /tmp/pdf_venv/bin/pip install edge-tts pydub
    System: ffmpeg, mpv or ffplay

Usage:
    /tmp/pdf_venv/bin/python3 scripts/audiobook_generator.py <chapters_dir> [options]

Example:
    /tmp/pdf_venv/bin/python3 scripts/audiobook_generator.py workspace/Book-Extract/chapters/chapters/ \\
        --voice ar-SA-ZariyahNeural \\
        --output workspace/Book-Extract/audiobook \\
        --title "دكالة في عهد البرتغاليين"
"""

import argparse
import asyncio
import os
import re
import subprocess
import sys
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


# ── Configuration ──────────────────────────────────────────────────────

DEFAULT_VOICE = "ar-SA-ZariyahNeural"
DEFAULT_RATE = "+0%"
SILENCE_THRESHOLD_MS = 500  # Remove silences longer than this
SILENCE_KEEP_MS = 200       # Keep this much silence between sentences
CHUNK_MAX_CHARS = 400       # Max characters per TTS chunk


# ── Text Cleaning ──────────────────────────────────────────────────────

def clean_ocr_text(text):
    """Clean OCR artifacts from Arabic text for TTS."""
    # Import the corrector
    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from arabic_text_corrector import clean_text
    
    # Use the dedicated corrector with TTS-friendly settings
    return clean_text(text, strictness=0.85)


def split_into_sentences(text):
    """Split Arabic text into sentences for TTS."""
    # Split on Arabic sentence endings
    sentences = re.split(r'(?<=[.؟!])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def chunk_sentences(sentences, max_chars=CHUNK_MAX_CHARS):
    """Group sentences into chunks respecting max character limit."""
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= max_chars:
            current = (current + " " + sentence).strip()
        else:
            if current:
                chunks.append(current)
            current = sentence
    if current:
        chunks.append(current)
    return chunks


# ── TTS Generation ─────────────────────────────────────────────────────

async def generate_tts_chunk(text, voice, rate, output_path):
    """Generate TTS audio for a single chunk using edge-tts."""
    import edge_tts
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_path)


def generate_tts_sync(text, voice, rate, output_path):
    """Sync wrapper for TTS generation."""
    asyncio.run(generate_tts_chunk(text, voice, rate, output_path))


# ── Audio Processing ───────────────────────────────────────────────────

def get_audio_duration(path):
    """Get duration of audio file in seconds using ffprobe."""
    result = subprocess.run(
        ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', path],
        capture_output=True, text=True
    )
    info = json.loads(result.stdout)
    return float(info['format']['duration'])


def remove_silence(input_path, output_path, threshold_ms=SILENCE_THRESHOLD_MS, keep_ms=SILENCE_KEEP_MS):
    """Remove long silences from audio using ffmpeg silencedetect."""
    # Step 1: Detect silences
    result = subprocess.run(
        [
            'ffmpeg', '-i', input_path, '-af',
            f'silencedetect=noise=-30dB:d={threshold_ms/1000}',
            '-f', 'null', '-'
        ],
        capture_output=True, text=True
    )

    # Parse silence segments
    silences = []
    for line in result.stderr.split('\n'):
        if 'silence_start' in line:
            m = re.search(r'silence_start:\s*([\d.]+)', line)
            if m:
                silences.append({'start': float(m.group(1))})
        elif 'silence_end' in line:
            m = re.search(r'silence_end:\s*([\d.]+).*silence_duration:\s*([\d.]+)', line)
            if m and silences:
                silences[-1]['end'] = float(m.group(1))
                silences[-1]['duration'] = float(m.group(2))

    if not silences:
        subprocess.run(['cp', input_path, output_path])
        return

    # Step 2: Build filter to trim silences
    # Create a volume filter that mutes long silences
    filter_parts = []
    for s in silences:
        if s.get('duration', 0) > threshold_ms / 1000:
            start = s['start']
            end = s.get('end', start + s.get('duration', 0))
            trim_amount = s['duration'] - (keep_ms / 1000)
            if trim_amount > 0:
                filter_parts.append(f"atrim={start}:{end - trim_amount}:end_mode=keep")

    if not filter_parts:
        subprocess.run(['cp', input_path, output_path])
        return

    # Simple approach: use silenceremove filter
    subprocess.run([
        'ffmpeg', '-y', '-i', input_path,
        '-af', f'silenceremove=start_periods=1:start_duration={threshold_ms/1000}:start_threshold=-30dB:start_silence=0:start_periods=0:stop_periods=-1:stop_duration={keep_ms/1000}:stop_threshold=-30dB',
        '-ar', '24000', '-ac', '1',
        output_path
    ], capture_output=True)


def concatenate_audio(file_list, output_path):
    """Concatenate multiple audio files using ffmpeg."""
    # Create concat file
    concat_file = output_path + '.concat.txt'
    with open(concat_file, 'w') as f:
        for fp in file_list:
            f.write(f"file '{os.path.abspath(fp)}'\n")

    subprocess.run([
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
        '-i', concat_file, '-ar', '24000', '-ac', '1',
        output_path
    ], capture_output=True)

    os.remove(concat_file)


# ── Subtitle Generation ────────────────────────────────────────────────

def format_srt_time(seconds):
    """Format seconds to SRT timestamp HH:MM:SS,mmm."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"


def generate_subtitles(chunks_info, output_path):
    """Generate SRT subtitle file from chunk timing info."""
    srt_lines = []
    idx = 1
    for info in chunks_info:
        start = info['start_time']
        end = info['end_time']
        text = info['text']
        # Split long subtitles into two lines
        if len(text) > 80:
            mid = len(text) // 2
            # Find nearest space to mid
            space_pos = text.rfind(' ', 0, mid + 20)
            if space_pos > 0:
                text = text[:space_pos] + '\n' + text[space_pos+1:]
        srt_lines.append(f"{idx}")
        srt_lines.append(f"{format_srt_time(start)} --> {format_srt_time(end)}")
        srt_lines.append(text)
        srt_lines.append("")
        idx += 1

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(srt_lines))


def generate_chapter_markers(chapters_info, output_path):
    """Generate chapter marker file for media players."""
    markers = []
    for ch in chapters_info:
        markers.append({
            'time': format_srt_time(ch['start_time']),
            'title': ch['name']
        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(markers, f, indent=2, ensure_ascii=False)


# ── Main Pipeline ──────────────────────────────────────────────────────

def process_chapter(chapter_path, voice, rate, temp_dir, chapter_idx):
    """Process a single chapter: clean text → TTS → silence removal."""
    chapter_name = os.path.splitext(os.path.basename(chapter_path))[0]
    print(f"\n{'='*60}")
    print(f"Chapter {chapter_idx}: {chapter_name}")
    print(f"{'='*60}")

    # Read and clean text
    with open(chapter_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    clean_text = clean_ocr_text(raw_text)
    if len(clean_text) < 10:
        print(f"  Skipping (too short: {len(clean_text)} chars)")
        return None

    print(f"  Clean text: {len(clean_text):,} chars")

    # Split into sentences and chunks
    sentences = split_into_sentences(clean_text)
    chunks = chunk_sentences(sentences)
    print(f"  Chunks: {len(chunks)}")

    # Generate TTS for each chunk (parallel)
    chapter_dir = os.path.join(temp_dir, f"ch_{chapter_idx:03d}")
    os.makedirs(chapter_dir, exist_ok=True)

    def process_chunk(i, chunk):
        raw_path = os.path.join(chapter_dir, f"chunk_{i:04d}_raw.mp3")
        clean_path = os.path.join(chapter_dir, f"chunk_{i:04d}.mp3")
        try:
            generate_tts_sync(chunk, voice, rate, raw_path)
            remove_silence(raw_path, clean_path)
            duration = get_audio_duration(clean_path)
            return {'index': i, 'text': chunk, 'path': clean_path, 'duration': duration, 'error': None}
        except Exception as e:
            return {'index': i, 'text': chunk, 'path': None, 'duration': 0, 'error': str(e)}

    # Parallel TTS generation (4 workers)
    results = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(process_chunk, i, c): i for i, c in enumerate(chunks)}
        done_count = 0
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            done_count += 1
            if done_count % 10 == 0 or done_count == len(chunks):
                print(f"  [{done_count}/{len(chunks)}] TTS generated")

    # Sort by index and build output
    results.sort(key=lambda x: x['index'])
    chunk_files = []
    chunks_info = []
    current_time = 0.0

    for r in results:
        if r['error']:
            print(f"  ERROR chunk {r['index']}: {r['error']}")
            continue
        chunks_info.append({
            'text': r['text'],
            'start_time': current_time,
            'end_time': current_time + r['duration'],
            'duration': r['duration']
        })
        current_time += r['duration']
        chunk_files.append(r['path'])

    # Concatenate chapter
    chapter_output = os.path.join(temp_dir, f"chapter_{chapter_idx:03d}.mp3")
    if chunk_files:
        concatenate_audio(chunk_files, chapter_output)
        print(f"  Chapter total: {current_time:.1f}s")

    return {
        'name': chapter_name,
        'file': chapter_output,
        'chunks_info': chunks_info,
        'duration': current_time,
        'chunk_files': chunk_files
    }


def main():
    parser = argparse.ArgumentParser(description="Generate audiobook from extracted text")
    parser.add_argument("chapters_dir", help="Directory containing chapter .txt files")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help=f"TTS voice (default: {DEFAULT_VOICE})")
    parser.add_argument("--rate", default=DEFAULT_RATE, help=f"Speech rate (default: {DEFAULT_RATE})")
    parser.add_argument("--output", "-o", default=None, help="Output directory")
    parser.add_argument("--title", default=None, help="Audiobook title")
    parser.add_argument("--keep-temp", action="store_true", help="Keep temporary files")
    parser.add_argument("--skip-silence", action="store_true", help="Skip silence removal")
    parser.add_argument("--start-chapter", type=int, default=0, help="Start from chapter N (skip earlier ones)")
    parser.add_argument("--end-chapter", type=int, default=999, help="Stop after chapter N")

    args = parser.parse_args()

    chapters_dir = os.path.abspath(args.chapters_dir)
    output_dir = args.output or os.path.join(os.path.dirname(chapters_dir), "audiobook")
    os.makedirs(output_dir, exist_ok=True)

    temp_dir = os.path.join(output_dir, ".temp")
    os.makedirs(temp_dir, exist_ok=True)

    title = args.title or os.path.basename(chapters_dir)

    # Find chapter files
    chapter_files = sorted([
        os.path.join(chapters_dir, f)
        for f in os.listdir(chapters_dir)
        if f.endswith('.txt')
    ])

    if not chapter_files:
        print(f"No .txt files found in {chapters_dir}")
        sys.exit(1)

    print(f"Audiobook Generator")
    print(f"===================")
    print(f"Title: {title}")
    print(f"Chapters: {len(chapter_files)}")
    print(f"Voice: {args.voice}")
    print(f"Output: {output_dir}")
    print()

    start_time = time.time()

    # Process each chapter
    all_chapters = []
    all_chunks_info = []
    global_time = 0.0

    for idx, chapter_path in enumerate(chapter_files):
        if idx < args.start_chapter:
            # Skip already-processed chapters - but still need timing info
            # Read the chapter file to get chunk count for timing estimate
            with open(chapter_path, 'r') as f:
                text = clean_ocr_text(f.read())
            sentences = split_into_sentences(text)
            chunks = chunk_sentences(sentences)
            # Rough estimate: assume ~10s per chunk for skipped chapters
            estimated_duration = len(chunks) * 10
            all_chapters.append({
                'name': os.path.splitext(os.path.basename(chapter_path))[0],
                'file': None,
                'chunks_info': [],
                'duration': estimated_duration,
                'start_time': global_time,
                'skipped': True
            })
            global_time += estimated_duration
            print(f"  Skipping chapter {idx} ({estimated_duration:.0f}s estimated)")
            continue
        if idx > args.end_chapter:
            break
        
        result = process_chapter(chapter_path, args.voice, args.rate, temp_dir, idx)
        if result:
            # Adjust chunk times to global timeline
            for chunk in result['chunks_info']:
                chunk['start_time'] += global_time
                chunk['end_time'] += global_time
                all_chunks_info.append(chunk)

            result['start_time'] = global_time
            global_time += result['duration']
            all_chapters.append(result)

    # Stitch all chapters together
    print(f"\n{'='*60}")
    print(f"Stitching {len(all_chapters)} chapters...")
    print(f"{'='*60}")

    all_files = [ch['file'] for ch in all_chapters if ch.get('file') and not ch.get('skipped')]
    final_audio = os.path.join(output_dir, f"{title}.mp3")
    concatenate_audio(all_files, final_audio)

    total_duration = get_audio_duration(final_audio)
    print(f"\nFinal audiobook: {total_duration:.1f}s ({total_duration/60:.1f} min)")

    # Generate subtitles
    print("\nGenerating subtitles...")
    srt_path = os.path.join(output_dir, f"{title}.srt")
    generate_subtitles(all_chunks_info, srt_path)
    print(f"  Subtitles: {srt_path}")

    # Generate chapter markers
    markers_path = os.path.join(output_dir, f"{title}_chapters.json")
    generate_chapter_markers(all_chapters, markers_path)
    print(f"  Chapter markers: {markers_path}")

    # Generate metadata
    metadata = {
        'title': title,
        'voice': args.voice,
        'rate': args.rate,
        'total_duration': total_duration,
        'chapters': [
            {
                'name': ch['name'],
                'duration': ch['duration'],
                'start_time': ch.get('start_time', 0)
            } for ch in all_chapters
        ]
    }
    meta_path = os.path.join(output_dir, f"{title}_metadata.json")
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"  Metadata: {meta_path}")

    # Cleanup
    if not args.keep_temp:
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)
        print("\nCleaned up temporary files")

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"Done!")
    print(f"Total time: {elapsed:.0f}s ({elapsed/60:.1f} min)")
    print(f"Output: {output_dir}/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
