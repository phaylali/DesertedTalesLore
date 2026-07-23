#!/usr/bin/env python3
"""
Arabic OCR Text Corrector - Conservative version
Fixes common OCR errors while preserving Moroccan Arabic (Darija).
"""

import re
import sys
import os


# ── Safe Word Replacements (OCR errors found in this book) ──────────────

SAFE_REPLACEMENTS = {
    # المؤرخين variants
    'الموؤ رخين': 'المؤرخين',
    'الموؤ رخون': 'المؤرخون',
    'موؤ رخين': 'مؤرخين',
    'موؤ رخون': 'مؤرخون',
    # الاجتماعي variants
    'الاجياعية': 'الاجتماعية',
    'الاجياعي': 'الاجتماعي',
    'الاجتاعية': 'الاجتماعية',
    'الاجتاعي': 'الاجتماعي',
    'الاجماعية': 'الاجتماعية',
    'الاجتياعية': 'الاجتماعية',
    'الاجتياعي': 'الاجتماعي',
    'الإجياعية': 'الاجتماعية',
    'الإجياعي': 'الاجتماعي',
    # المعطيات
    'الملعطيات': 'المعطيات',
    # استفادة
    'استقادة': 'استفادة',
    # استعمار
    'الاستعيار': 'الاستعمار',
    'استعيار': 'استعمار',
    # فئاتهم
    'قثاتهم': 'فئاتهم',
    'فثاتهم': 'فئاتهم',
    'قئاتهم': 'ئاتهم',
    # الإدارة
    'الادارة': 'الإدارة',
    'ادارية': 'إدارية',
    # التجاري
    'التاجي': 'التجاري',
    'التاجية': 'التجارية',
    'التاجيين': 'التجاريين',
    # Additional OCR errors
    'الاجنحية': 'الاستراتيجية',
    'الاجنحي': 'الاستراتيجي',
    'الاجماعي': 'الاجتماعي',
}


def fix_line_breaks(text):
    """Join Arabic words split across lines."""
    lines = text.split('\n')
    result = []
    buffer = ""
    
    arabic_chars = set('ابتثجحخدذرزسشصضطظعغفقكلمنهويىءؤئ')
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if buffer:
                result.append(buffer)
                buffer = ""
            result.append("")
            continue
        
        if buffer:
            if buffer[-1] in arabic_chars and stripped[0] in arabic_chars:
                buffer += stripped
                continue
            else:
                result.append(buffer)
                buffer = ""
        
        if (len(stripped) > 3 and
            stripped[-1] in arabic_chars and
            not stripped.endswith(('،', '.', '؟', '!', ':', '؛', 'ـ'))):
            buffer = stripped
        else:
            result.append(stripped)
    
    if buffer:
        result.append(buffer)
    
    return '\n'.join(result)


def apply_safe_replacements(text):
    """Apply safe word-level corrections."""
    for wrong, correct in SAFE_REPLACEMENTS.items():
        text = text.replace(wrong, correct)
    return text


def clean_text(text, strictness=0.85):
    """
    Clean OCR text with configurable strictness.
    
    strictness: 0.0 (minimal) to 1.0 (aggressive)
    - Always: line break fixing, safe word replacements
    - >0.5: remove garbled unicode sequences
    - >0.7: remove isolated short noise lines
    """
    # Remove page markers
    text = re.sub(r'### PAGE \d+ ###', '\n', text)
    
    # Fix line breaks
    text = fix_line_breaks(text)
    
    # Apply safe word replacements
    text = apply_safe_replacements(text)
    
    if strictness > 0.5:
        # Remove zero-width and invisible characters
        text = re.sub(r'[\u200b-\u200f\u2028-\u202f\u2060-\u2069\ufeff]+', '', text)
        # Remove garbled diacritics sequences
        text = re.sub(r'[\u064b-\u065f]{2,}', '', text)
    
    if strictness > 0.7:
        # Remove very short noise lines
        text = re.sub(r'^.{0,3}$', '', text, flags=re.MULTILINE)
        # Remove lines that are only punctuation/symbols
        text = re.sub(r'^[^\u0600-\u06FF\w]+$', '', text, flags=re.MULTILINE)
    
    # Final cleanup
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    
    return text.strip()


def process_file(input_path, output_path, strictness=0.85):
    """Process a single file."""
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    corrected = clean_text(text, strictness)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(corrected)
    
    print(f"  {os.path.basename(input_path)}: {len(text)} → {len(corrected)} chars")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Arabic OCR Text Corrector")
    parser.add_argument("input", help="Input file or directory")
    parser.add_argument("output", nargs="?", default=None, help="Output file or directory")
    parser.add_argument("--strictness", "-s", type=float, default=0.85,
                        help="Correction strictness 0.0-1.0 (default: 0.85)")
    parser.add_argument("--dir", action="store_true",
                        help="Process directory of .txt files")
    
    args = parser.parse_args()
    
    if args.dir:
        output_dir = args.output or args.input + "_corrected"
        os.makedirs(output_dir, exist_ok=True)
        files = sorted([f for f in os.listdir(args.input) if f.endswith('.txt')])
        print(f"Processing {len(files)} files (strictness={args.strictness})")
        for f in files:
            process_file(
                os.path.join(args.input, f),
                os.path.join(output_dir, f),
                args.strictness
            )
        print(f"Done! Output: {output_dir}")
    else:
        output_path = args.output or args.input.replace('.txt', '_corrected.txt')
        process_file(args.input, output_path, args.strictness)


if __name__ == "__main__":
    main()
