#!/usr/bin/env python3
"""Validate Chapter 2 generated packets and protected reference content."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generate_chapter_02 import (  # noqa: E402
    CLASSIFICATION_KEYS,
    STUDENT_OUT,
    TEACHER_OUT,
    REVIEW_OUT,
    REVIEW_KEY_OUT,
)

REF_PDF = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference.pdf"
REF_PDF_SHA256 = "246155da24ae2e6334438d7f1823f953b153aeeb38b81dd77bd1bb2cb6dca0da"

PROHIBITED_PHRASES = ["study guide"]
TEMP_ARTIFACT_DIRS = [
    ROOT / "work/chapter-02/qa-render",
    ROOT / "work/chapter-02/validate-render",
]

VALID_LABELS = {"SN", "V", "Adv", "Adj", "A", "P1", "D", "Imp", "Int", "E", "type"}


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


def render_docx_page_count(docx: Path, qa_subdir: str) -> tuple[int, Path]:
    qa_dir = ROOT / "work/chapter-02" / qa_subdir
    qa_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(qa_dir), str(docx)],
        check=True,
        capture_output=True,
    )
    pdf = qa_dir / f"{docx.stem}.pdf"
    return pdf_page_count(pdf), pdf


def check_no_study_guide(paths: list[Path]) -> list[str]:
    errors = []
    for path in paths:
        lower = docx_text(path).lower()
        for phrase in PROHIBITED_PHRASES:
            if phrase in lower:
                errors.append(f'{path.name} contains prohibited phrase "{phrase}"')
    return errors


def check_no_temp_artifacts() -> list[str]:
    errors = []
    for d in TEMP_ARTIFACT_DIRS:
        if d.exists():
            leftovers = list(d.glob("*.tmp")) + list(d.glob("~$*"))
            for f in leftovers:
                errors.append(f"Temporary artifact: {f}")
    return errors


def docx_plain_text(path: Path) -> str:
    from docx import Document as DocxDocument

    doc = DocxDocument(path)
    parts: list[str] = []
    for p in doc.paragraphs:
        parts.append(p.text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                parts.append(cell.text)
    return "\n".join(parts)


def check_classification_keys_in_teacher() -> list[str]:
    errors = []
    text = docx_plain_text(TEACHER_OUT)
    for key_id, classified in CLASSIFICATION_KEYS.items():
        for word, _ in classified.tokens:
            if word not in text:
                errors.append(f"Teacher edition missing token '{word}' for {key_id}")
                break
        if classified.sentence_type and classified.sentence_type not in text:
            errors.append(f"Teacher edition missing sentence type {classified.sentence_type} for {key_id}")
    return errors


def check_word_order_preserved() -> list[str]:
    errors = []
    text = docx_plain_text(TEACHER_OUT)
    for key_id, classified in CLASSIFICATION_KEYS.items():
        words = [w for w, _ in classified.tokens]
        indices = []
        pos = 0
        failed = False
        for w in words:
            idx = text.find(w, pos)
            if idx < 0:
                errors.append(f"Word order check failed for {key_id}: missing {w}")
                failed = True
                break
            indices.append(idx)
            pos = idx + len(w)
        if not failed and len(indices) > 1 and indices != sorted(indices):
            errors.append(f"Word order not preserved for {key_id}")
    return errors


def check_p1_not_at_sentence_end() -> list[str]:
    errors = []
    text = docx_plain_text(TEACHER_OUT)
    if re.search(r"[.!?]\s*P1", text):
        errors.append("P1 appears at sentence end (invalid placement)")
    return errors


def check_no_invented_terms() -> list[str]:
    errors = []
    for path in (STUDENT_OUT, TEACHER_OUT):
        lower = docx_plain_text(path).lower()
        if "determiners" in lower:
            errors.append(f"{path.name} contains prohibited term 'determiners'")
        if "to what extent" in lower:
            errors.append(f"{path.name} contains prohibited fourth adverb question")
    return errors


def check_review_key_match() -> list[str]:
    errors = []
    review = docx_plain_text(REVIEW_OUT)
    key = docx_plain_text(REVIEW_KEY_OUT)
    for phrase in ("Plane", "Boys raced", "The music played softly", "rhyming", "soothing"):
        if phrase not in review:
            errors.append(f"Review missing expected content: {phrase}")
        if phrase not in key:
            errors.append(f"Review key missing expected content: {phrase}")
    if "How?" not in key or "What kind?" not in key:
        errors.append("Review key missing question answers")
    return errors


def check_blueprint_content() -> list[str]:
    errors = []
    text = docx_plain_text(STUDENT_OUT)
    required = [
        "The Sentence Blueprint",
        "Who? / What?",
        "How? / When? / Where?",
        "What kind? / Which one? / How many?",
        "Declarative (D)",
        "Mover",
    ]
    for phrase in required:
        if phrase not in text:
            errors.append(f"Student packet missing blueprint content: {phrase}")
    return errors


def main() -> int:
    errors: list[str] = []

    required = [STUDENT_OUT, TEACHER_OUT, REVIEW_OUT, REVIEW_KEY_OUT, REF_PDF]
    for path in required:
        if not path.exists():
            errors.append(f"Missing required file: {path}")

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    pdf_hash = sha256(REF_PDF)
    if pdf_hash != REF_PDF_SHA256:
        errors.append(f"Protected PDF modified: expected {REF_PDF_SHA256}, got {pdf_hash}")

    paths = [STUDENT_OUT, TEACHER_OUT, REVIEW_OUT, REVIEW_KEY_OUT]
    errors.extend(check_no_study_guide(paths))
    errors.extend(check_no_invented_terms())
    errors.extend(check_blueprint_content())
    errors.extend(check_classification_keys_in_teacher())
    errors.extend(check_p1_not_at_sentence_end())
    errors.extend(check_word_order_preserved())
    errors.extend(check_review_key_match())
    errors.extend(check_no_temp_artifacts())

    try:
        student_pages, student_pdf = render_docx_page_count(STUDENT_OUT, "qa-render/student")
        teacher_pages, teacher_pdf = render_docx_page_count(TEACHER_OUT, "qa-render/teacher")
        review_pages, review_pdf = render_docx_page_count(REVIEW_OUT, "qa-render/review")
        review_key_pages, review_key_pdf = render_docx_page_count(REVIEW_KEY_OUT, "qa-render/review-key")
    except subprocess.CalledProcessError as exc:
        print(f"FAIL: LibreOffice render failed: {exc}", file=sys.stderr)
        return 1
    except FileNotFoundError:
        print("FAIL: pdfinfo or soffice not available", file=sys.stderr)
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
    print(f"Classification keys registered: {len(CLASSIFICATION_KEYS)}")
    print(f"Student PDF: {student_pdf}")
    print(f"Teacher PDF: {teacher_pdf}")

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
