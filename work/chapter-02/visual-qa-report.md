# Chapter 2 Visual QA Report

**Date:** 2026-07-26 (final polish pass)  
**Branch:** `phase-3/chapter-02-gold-standard`  
**Render:** LibreOffice headless → PDF → `pdftoppm` @ 120 DPI (`work/chapter-02/qa-render/polish/`)

## Scope

| Document | Pages inspected | Focus |
|----------|-----------------|-------|
| Student packet | 28 | Vocab p20, p24; classification practice pages |
| Teacher edition | 28 | Classification keys p27; parity vs student |
| In-Class Chapter Review | 2 | Parts A–D layout |
| Review key | 1 | Full classification tables, type column |

## Polish-pass fixes

| Fix | Result |
|-----|--------|
| `_render_classification_table()` — reserved type column (`noWrap`, fixed width) | Review key: labels above words, P1 under SN V, type at end; no type wrap |
| Dynamic 8pt font for tables with ≥7 tokens | Sentence 4 (stormy winter sky) no longer breaks mid-row |
| `render_classification_compact()` — tokens line + right-aligned `type D/E` line | Teacher keys: sentence type never wraps with token string |
| `add_fixed_drawing_area()` — 1×1 table, 1.2 in height, cell borders | L7 p20, L8 p24: proper drawing box |

## Defects resolved

| ID | Was | Resolution |
|----|-----|------------|
| VQ-02 | Vocab drawing box border only on first line | Fixed — fixed-height bordered table cell |
| VQ-03 | Compact classification `→ D` wrapped to second line | Fixed — type on dedicated right-aligned line |
| VQ-06 | Review key sentence 4 verb row broke across lines | Fixed — noWrap cells + 8pt for wide tables |

## Spot-check results (pass)

| Area | Check | Result |
|------|-------|--------|
| L7 p20 vocab | Fixed drawing area, full-width bordered box | Pass |
| L8 p24 vocab | Drawing box + analogy + Remember boxes below | Pass |
| Teacher p27 | Three practice items; type right-aligned per item | Pass |
| Review key | Tables: SN/V/P1, divide `\|`, type column D/E | Pass |
| Review p1–2 | Classification blanks, Part D + Teacher Check | Pass |
| Student/teacher parity | 28 / 28 rendered pages | Pass |

## Remaining concerns

1. **Page count vs target:** 28 pages (spec 24 ± 2) — unchanged; acceptable per prior repair pass.
2. **Teacher compact format:** Type label on line below tokens (not same row as full table) — preserves no-wrap without page overflow.
3. **Review page 2 density:** Part D sparse (~25% fill) — within 2-page spec.
4. **Wide classification tables:** 8pt auto-scaling for ≥7 tokens; monitor if future sentences exceed page width.

## Pagination optimization pass (2026-07-26, final)

| Change | Result |
|--------|--------|
| L1/L2/L4: Practice item 3 on practice page | Pages 5, 8, 13 better filled |
| L1/L2/L4: Memory Check follows practice (pages 5, 8, 13) | Apply pages 6, 9, 14 slimmer |
| L3/L6/L8: Practice item 3 on practice page | Pages 10, 18, 25 better filled |
| Section merges (L1bc, L7ab, L9ab, cross-lesson, etc.) | Rejected — overflow or parity fail |

**Rendered page count:** 28 → 28 (unchanged). See `pagination-optimization-proposal.md`.

Visual spot-check (pages 5–6, 10): no clipping, classification blanks intact, memory checks follow practice.

## Validation

```
Student packet pages: 28
Teacher edition pages: 28
In-Class Chapter Review pages: 2
Review key pages: 1
VALIDATION PASSED
```

Protected PDF SHA-256 unchanged: `246155da24ae2e6334438d7f1823f953b153aeeb38b81dd77bd1bb2cb6dca0da`
