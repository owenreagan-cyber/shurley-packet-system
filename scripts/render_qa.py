#!/usr/bin/env python3
"""Render DOCX files to PDF/PNG for visual QA."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QA_DIR = ROOT / "work" / "chapter-01" / "qa-render"

DOCX_FILES = [
    ROOT / "packets/student/chapter-01/chapter-01-shurley-packet.docx",
    ROOT / "packets/teacher-keys/chapter-01/chapter-01-shurley-packet-teacher-edition.docx",
    ROOT / "packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review.docx",
    ROOT / "packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review-key.docx",
]


def render_docx(docx: Path) -> list[Path]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    pdf = QA_DIR / f"{docx.stem}.pdf"
    png_dir = QA_DIR / f"png-{docx.stem}"
    if png_dir.exists():
        shutil.rmtree(png_dir)
    png_dir.mkdir()

    subprocess.run(
        [
            "soffice", "--headless", "--convert-to", "pdf",
            "--outdir", str(QA_DIR), str(docx),
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["pdftoppm", "-png", "-r", "120", str(pdf), str(png_dir / "page")],
        check=True,
        capture_output=True,
    )
    return sorted(png_dir.glob("*.png"))


def page_count(docx: Path) -> int:
    return len(render_docx(docx))


def cleanup():
    if QA_DIR.exists():
        shutil.rmtree(QA_DIR)


def main():
    counts = {}
    for docx in DOCX_FILES:
        if not docx.exists():
            print(f"MISSING: {docx}", file=sys.stderr)
            sys.exit(1)
        pngs = render_docx(docx)
        counts[docx.name] = len(pngs)
        print(f"{docx.name}: {len(pngs)} pages, {len(pngs)} PNG renders")
    return counts


if __name__ == "__main__":
    main()
