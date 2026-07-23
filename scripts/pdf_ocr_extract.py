#!/usr/bin/env python3
"""
PDF OCR Text Extractor for Arabic Scanned Books
Extracts text from scanned PDFs using Tesseract OCR and organizes into chapters.

Requirements:
    python3 -m venv /tmp/pdf_venv
    /tmp/pdf_venv/bin/pip install pymupdf pytesseract Pillow

System requirements:
    tesseract-ocr
    tesseract-data-ara  (for Arabic OCR)

Usage:
    python3 scripts/pdf_ocr_extract.py <pdf_path> [--output-dir <dir>] [--dpi <dpi>] [--lang <lang>]
"""

import argparse
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os
import re
import sys
import time


def extract_text_from_pdf(pdf_path, output_dir, dpi=300, lang="ara"):
    """OCR every page and save raw text + page markers."""
    doc = fitz.open(pdf_path)
    total = doc.page_count
    print(f"PDF: {pdf_path}")
    print(f"Pages: {total}")
    print(f"DPI: {dpi} | Lang: {lang}")
    print(f"Output: {output_dir}")
    print()

    os.makedirs(output_dir, exist_ok=True)

    all_pages = []
    start = time.time()

    for i in range(total):
        page = doc[i]
        pix = page.get_pixmap(dpi=dpi)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang=lang, config="--psm 6")
        text = text.strip()
        all_pages.append(text)

        elapsed = time.time() - start
        eta = (elapsed / (i + 1)) * (total - i - 1) if i > 0 else 0
        if (i + 1) % 50 == 0 or i == 0 or i == total - 1:
            print(
                f"  [{i+1}/{total}] {len(text):>5} chars | "
                f"elapsed {elapsed:.0f}s | ETA {eta:.0f}s"
            )

    doc.close()

    # Build full text with page markers
    full_text = ""
    for i, text in enumerate(all_pages):
        full_text += f"\n\n### PAGE {i+1} ###\n{text}"

    full_path = os.path.join(output_dir, "full_ocr_text.txt")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"\nSaved: {full_path} ({len(full_text):,} chars)")
    return full_text


def find_headings(full_text, custom_patterns=None):
    """Scan OCR text for chapter/section headings."""
    pages = re.split(r"### PAGE (\d+) ###", full_text)
    page_map = {}
    for i in range(1, len(pages), 2):
        page_map[int(pages[i])] = pages[i + 1]

    default_patterns = [
        r"^الفصل\s+ال",
        r"^الفصل\s+\d+",
        r"^الباب\s+ال",
        r"^الباب\s+\d+",
        r"^المقدم[هة]",
        r"^الخاتمه",
        r"^فهرس",
        r"^المراجع",
        r"^الملاحق",
        r"^الملخص",
    ]
    patterns = custom_patterns or default_patterns

    found = []
    for page_num in sorted(page_map.keys()):
        for line in page_map[page_num].split("\n"):
            line_s = line.strip()
            if not line_s or len(line_s) > 80:
                continue
            for pat in patterns:
                if re.search(pat, line_s):
                    found.append({"page": page_num, "text": line_s})
                    break
    return found


def split_into_chapters(full_text, chapter_defs, output_dir):
    """
    Split OCR text into chapter files.
    chapter_defs: list of dicts with keys: name, start_page, end_page
    """
    pages = re.split(r"### PAGE (\d+) ###", full_text)
    page_map = {}
    for i in range(1, len(pages), 2):
        page_map[int(pages[i])] = pages[i + 1]

    os.makedirs(output_dir, exist_ok=True)
    all_page_nums = sorted(page_map.keys())

    for ch in chapter_defs:
        name = ch["name"]
        start = ch.get("start_page", all_page_nums[0])
        end = ch.get("end_page", all_page_nums[-1])
        safe_name = re.sub(r"[^\w\u0600-\u06FF]+", "_", name).strip("_")

        chapter_text = ""
        for p in range(start, end + 1):
            if p in page_map:
                chapter_text += page_map[p] + "\n"

        # Clean: remove page numbers, excessive whitespace, garbled OCR artifacts
        chapter_text = clean_text(chapter_text)

        filepath = os.path.join(output_dir, f"{safe_name}.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(chapter_text)
        print(f"  {safe_name}.txt  (pages {start}-{end}, {len(chapter_text):,} chars)")

    print(f"\nDone. {len(chapter_defs)} chapter files saved to {output_dir}")


def clean_text(text):
    """Clean OCR artifacts from Arabic text."""
    # Remove standalone page numbers (Arabic or Latin digits)
    text = re.sub(r"\n\s*\d{1,3}\s*\n", "\n", text)
    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Remove isolated single characters / garbled lines (short junk)
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # Skip very short lines that are mostly numbers/symbols
        if len(stripped) <= 2 and not re.search(r"[\u0600-\u06FF]", stripped):
            continue
        cleaned.append(line)
    text = "\n".join(cleaned)
    return text.strip()


# ── Default chapter definitions for dakala.pdf ──────────────────────────

DAKALA_CHAPTERS = [
    {"name": "00_المقدمه", "start_page": 8, "end_page": 26},
    {"name": "01_الباب الاول - الفصل الاول - تطور اسم دكالة وحدودها", "start_page": 27, "end_page": 56},
    {"name": "02_الباب الاول - الفصل الاول - مشكل الماء والغطاء النباتي", "start_page": 57, "end_page": 73},
    {"name": "03_الباب الاول - الفصل الثاني - دخول القبائل العربية والبربرية", "start_page": 74, "end_page": 102},
    {"name": "04_الباب الاول - الفصل الثالث - أوضاع دكالة الاقتصادية", "start_page": 103, "end_page": 118},
    {"name": "05_الباب الاول - الفصل الرابع - المجتمع الدكالي", "start_page": 119, "end_page": 146},
    {"name": "06_الباب الثاني - الفصل الاول - الغزو البرتغالي لسواحل المغرب", "start_page": 147, "end_page": 172},
    {"name": "07_الباب الثاني - الفصل الثاني - التجربة السياسية البرتغالية", "start_page": 173, "end_page": 208},
    {"name": "08_الباب الثاني - الفصل الثالث - محاولات التوسع بدكالة", "start_page": 209, "end_page": 246},
    {"name": "09_الباب الثالث - الفصل الاول - التنظيم الإداري والجبائي", "start_page": 247, "end_page": 280},
    {"name": "10_الباب الثالث - الفصل الثاني - استغلال الطاقات الإنتاجية", "start_page": 281, "end_page": 332},
    {"name": "11_الباب الثالث - الفصل الثالث - التنظيم الديني وأوضاع اليهود والمسلمين", "start_page": 333, "end_page": 348},
    {"name": "12_الباب الرابع - الفصل الاول - موقف الفئات المجتمعية", "start_page": 349, "end_page": 378},
    {"name": "13_الباب الرابع - الفصل الثاني - الحركات الجهادية", "start_page": 379, "end_page": 403},
    {"name": "14_الباب الرابع - الفصل الثالث - تأزم البرتغاليين واجلاؤهم", "start_page": 404, "end_page": 436},
    {"name": "15_الباب الخامس - الفصل الاول - نتائج الغزو الاقتصادية", "start_page": 437, "end_page": 458},
    {"name": "16_الباب الخامس - الفصل الثاني - النتائج الاجتماعية والثقافية", "start_page": 459, "end_page": 490},
    {"name": "17_الملاحق", "start_page": 491, "end_page": 629},
]


def main():
    parser = argparse.ArgumentParser(description="Extract text from scanned PDFs using OCR")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory")
    parser.add_argument("--dpi", type=int, default=300, help="Render DPI (default: 300)")
    parser.add_argument("--lang", default="ara", help="Tesseract language (default: ara)")
    parser.add_argument("--ocr-only", action="store_true", help="Only OCR, skip chapter splitting")
    parser.add_argument("--skip-ocr", action="store_true", help="Skip OCR, use existing full_ocr_text.txt")

    args = parser.parse_args()

    base_name = os.path.splitext(os.path.basename(args.pdf_path))[0]
    output_dir = args.output_dir or os.path.join(
        os.path.dirname(args.pdf_path), f"{base_name}_extracted"
    )

    if args.skip_ocr:
        full_text_path = os.path.join(output_dir, "full_ocr_text.txt")
        if not os.path.exists(full_text_path):
            print(f"Error: {full_text_path} not found. Run OCR first.")
            sys.exit(1)
        with open(full_text_path, "r", encoding="utf-8") as f:
            full_text = f.read()
        print(f"Loaded existing OCR text: {len(full_text):,} chars")
    else:
        full_text = extract_text_from_pdf(args.pdf_path, output_dir, args.dpi, args.lang)

    if args.ocr_only:
        return

    # Detect headings
    print("\nDetecting chapter headings...")
    headings = find_headings(full_text)
    if headings:
        print(f"Found {len(headings)} potential headings:")
        for h in headings:
            print(f"  Page {h['page']:>4}: {h['text']}")
    else:
        print("No headings detected with default patterns.")

    # Split into chapters (using DAKALA_CHAPTERS for this specific book)
    print("\nSplitting into chapters...")
    chapters_dir = os.path.join(output_dir, "chapters")
    split_into_chapters(full_text, DAKALA_CHAPTERS, chapters_dir)


if __name__ == "__main__":
    main()
