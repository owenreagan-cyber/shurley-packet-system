# Phase 2 Build Report — Chapter 1 Gold Standard

**Date:** 2026-07-24 (updated: Lesson 4 analogy page repair)  
**Branch:** `phase-2/chapter-01-gold-standard`  
**Status:** Complete — Ready for teacher review

---

## 1. Protected Reference Integration

The official Shurley capitalization and punctuation reference (`source-materials/reference/shurley-capitalization-punctuation-reference.pdf`) is integrated immediately before Lesson 5:

| Page | Content |
|------|---------|
| 18 | **Capitalization and Punctuation Reference** (intro label page) |
| 19 | Reference 9 — Punctuation Rules (embedded source image) |
| 20 | Reference 7 — Capitalization Rules (embedded source image) |

Student and teacher editions contain the same reference pages at the same locations. Teacher procedural notes appear only on the intro page (18); reference image pages are unaltered.

## 2. Transcription vs. Image Embed

- **Transcription created:** `source-materials/reference/shurley-capitalization-punctuation-reference-transcription.md`
- **Packet delivery method:** Full-page **image embed** (not retyped text) to guarantee exact preservation of official wording, formatting, and examples.
- Transcription used for rule-number validation and teacher review; visually compared against 200 DPI PNG renders of both PDF pages.

## 3. Final Page Counts (LibreOffice PDF)

| Document | Pages |
|----------|-------|
| Student Shurley Packet | 27 |
| Teacher Edition | 27 |
| In-Class Chapter Review | 1 |
| In-Class Chapter Review Key | 1 |

## 4. Spacing and Layout Improvements

- Fixed Lesson 1 overflow (orphan TEACHER CHECK page).
- Fixed Lesson 2 overflow (orphan paragraph-combining note).
- Reference images scaled to fit portrait pages without spillover.
- Capitalization reference page rotated for correct reading orientation.
- **Lesson 4 analogy pages redesigned (pages 13–14):** replaced cramped 3-column table with two full instructional pages using 14–16 pt text, large Remember box, and 2×2 relationship cards.

## 4a. Lesson 4 Analogy Page Redesign

| | Old | New |
|---|-----|-----|
| Page 13 | Sparse intro + small Remember line (~top 25% of page) | **Understanding Analogies** — full-page instruction |
| Page 14 | Cramped 3-column table (~top 30% of page) | **Four Common Analogy Relationships** — 2×2 cards |
| Typography | 13 pt default throughout | Body 14 pt, examples 16 pt, headings 18 pt |
| Teacher parity | Answer block only | Identical student layout on pages 13–14 |

## 5. Validation

`scripts/validate_chapter_01.py` confirms:

- Punctuation rules 1–13 and capitalization rules 1–8 in transcription
- Reference phrases and embedded images in both packets
- Student/teacher page parity (27/27)
- Review ≤ 2 pages
- Protected PDF SHA-256 unchanged
- No "Study Guide" phrase

## 6. Files Created

| File | Purpose |
|------|---------|
| `source-materials/reference/shurley-capitalization-punctuation-reference-transcription.md` | Protected transcription |
| `source-materials/reference/shurley-capitalization-punctuation-reference-page-1.png` | Punctuation embed source |
| `source-materials/reference/shurley-capitalization-punctuation-reference-page-2-oriented.png` | Capitalization embed source (orientation corrected) |
| `scripts/validate_chapter_01.py` | Protected-content and pagination validation |
| `docs/standards/student-resource-qa-rules.md` | Student resource QA standards |
| `docs/standards/slideshow-qa-rules.md` | Slideshow QA standards (no Ch. 1 PPTX yet) |
| `work/chapter-01/page-pair-audit.md` | Student/teacher page-pair audit |

## 7. Files Modified

- `scripts/generate_chapter_01.py` — reference pages, overflow fixes, teacher reference mirroring
- `docs/standards/packet-content-rules.md` — reference integration rules
- `docs/standards/packet-design-rules.md` — validation step
- `docs/standards/naming-conventions.md` — reference resource name
- `work/chapter-01/pagination-audit.md` — updated counts
- All regenerated DOCX outputs under `packets/`

## 8. Slideshow QA

No Chapter 1 slideshow exists. Requirements added to `docs/standards/slideshow-qa-rules.md`.

## 9. Remaining Teacher-Review Concerns

- [ ] Confirm rotated capitalization page matches classroom Shurley materials
- [ ] Print-test reference image readability at school copier quality
- [ ] Verify Lesson 1 memory check reduction (2 questions vs. prior 3) is acceptable
- [ ] Confirm four vocabulary words and editing passage corrections
- [ ] Test handwriting space on printed packet

## 10. Validation Commands

```bash
python3 scripts/generate_chapter_01.py
python3 scripts/validate_chapter_01.py
python3 scripts/render_qa.py
```
