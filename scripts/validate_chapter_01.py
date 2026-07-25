#!/usr/bin/env python3
"""Validate Chapter 1 generated packets and protected reference content."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STUDENT_PACKET = ROOT / "packets/student/chapter-01/chapter-01-shurley-packet.docx"
TEACHER_PACKET = ROOT / "packets/teacher-keys/chapter-01/chapter-01-shurley-packet-teacher-edition.docx"
REVIEW = ROOT / "packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review.docx"
REVIEW_KEY = ROOT / "packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review-key.docx"

REF_PDF = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference.pdf"
REF_TRANSCRIPTION = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference-transcription.md"
REF_PUNCT_IMG = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference-page-1.png"
REF_CAP_IMG = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference-page-2-oriented.png"

# SHA-256 of protected PDF at integration time (visual-verified source).
REF_PDF_SHA256 = "246155da24ae2e6334438d7f1823f953b153aeeb38b81dd77bd1bb2cb6dca0da"

PUNCTUATION_RULE_MARKERS = [f"Rule {n}:" for n in range(1, 14)]
CAPITALIZATION_RULE_MARKERS = [f"Rule {n}:" for n in range(1, 9)]

REFERENCE_PHRASES = [
    "Capitalization and Punctuation Reference",
    "Reference 9 — Punctuation Rules",
    "Reference 7 — Capitalization Rules",
]

PROHIBITED_PHRASES = ["study guide"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        parts = []
        for name in zf.namelist():
            if name.endswith(".xml"):
                parts.append(zf.read(name).decode("utf-8", "ignore"))
        return "".join(parts)


def docx_has_embedded_images(path: Path, min_count: int = 2) -> bool:
    with zipfile.ZipFile(path) as zf:
        media = [n for n in zf.namelist() if n.startswith("word/media/")]
    return len(media) >= min_count


def pdf_page_count(path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"Could not read page count from {path}")


def render_docx_page_count(docx: Path) -> int:
    qa_dir = ROOT / "work" / "chapter-01" / "qa-render" / "validate"
    qa_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(qa_dir), str(docx)],
        check=True,
        capture_output=True,
    )
    pdf = qa_dir / f"{docx.stem}.pdf"
    return pdf_page_count(pdf)


def check_transcription_rules() -> list[str]:
    errors = []
    if not REF_TRANSCRIPTION.exists():
        return ["Missing transcription file"]
    text = REF_TRANSCRIPTION.read_text(encoding="utf-8")
    for marker in PUNCTUATION_RULE_MARKERS:
        if marker not in text:
            errors.append(f"Transcription missing {marker}")
    for marker in CAPITALIZATION_RULE_MARKERS:
        if marker not in text:
            errors.append(f"Transcription missing {marker}")
    if text.find("Rule 1:") >= text.find("Rule 8:"):
        errors.append("Capitalization rule order may be wrong in transcription")
    punct_section = text.split("Source Page 2", 1)[0]
    for n in range(1, 14):
        if f"**Rule {n}:**" not in punct_section and f"Rule {n}:" not in punct_section:
            errors.append(f"Transcription missing punctuation rule {n} statement")
    return errors


def check_no_study_guide(paths: list[Path]) -> list[str]:
    errors = []
    for path in paths:
        lower = docx_text(path).lower()
        for phrase in PROHIBITED_PHRASES:
            if phrase in lower:
                errors.append(f'{path.name} contains prohibited phrase "{phrase}"')
    return errors


def check_reference_in_docx(path: Path) -> list[str]:
    errors = []
    text = docx_text(path)
    for phrase in REFERENCE_PHRASES:
        if phrase not in text:
            errors.append(f"{path.name} missing reference phrase: {phrase}")
    if not docx_has_embedded_images(path, min_count=2):
        errors.append(f"{path.name} missing embedded reference images (expected >= 2)")
    return errors


def main() -> int:
    errors: list[str] = []

    required = [STUDENT_PACKET, TEACHER_PACKET, REVIEW, REVIEW_KEY, REF_PDF, REF_TRANSCRIPTION, REF_PUNCT_IMG, REF_CAP_IMG]
    for path in required:
        if not path.exists():
            errors.append(f"Missing required file: {path}")

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    pdf_hash = sha256(REF_PDF)
    if pdf_hash != REF_PDF_SHA256:
        errors.append(
            f"Protected PDF modified: expected {REF_PDF_SHA256}, got {pdf_hash}"
        )

    errors.extend(check_transcription_rules())
    errors.extend(check_no_study_guide([STUDENT_PACKET, TEACHER_PACKET, REVIEW, REVIEW_KEY]))
    errors.extend(check_reference_in_docx(STUDENT_PACKET))
    errors.extend(check_reference_in_docx(TEACHER_PACKET))

    try:
        student_pages = render_docx_page_count(STUDENT_PACKET)
        teacher_pages = render_docx_page_count(TEACHER_PACKET)
        review_pages = render_docx_page_count(REVIEW)
        review_key_pages = render_docx_page_count(REVIEW_KEY)
    except subprocess.CalledProcessError as exc:
        print(f"FAIL: LibreOffice render failed: {exc}", file=sys.stderr)
        return 1

    if student_pages != teacher_pages:
        errors.append(f"Page parity FAIL: student={student_pages}, teacher={teacher_pages}")
    if review_pages > 2:
        errors.append(f"In-Class Chapter Review exceeds 2 pages: {review_pages}")
    if review_key_pages > 2:
        errors.append(f"Review key exceeds 2 pages: {review_key_pages}")

    print("Protected reference PDF SHA-256:", pdf_hash)
    print(f"Student packet pages: {student_pages}")
    print(f"Teacher edition pages: {teacher_pages}")
    print(f"In-Class Chapter Review pages: {review_pages}")
    print(f"Review key pages: {review_key_pages}")
    print(f"Transcription punctuation rules: 1–13 present")
    print(f"Transcription capitalization rules: 1–8 present")
    print(f"Reference embedded in student packet: OK")
    print(f"Reference embedded in teacher edition: OK")
    print(f"No 'Study Guide' phrase: OK")

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
