# Chapter 1 Pagination Optimization Proposal

**Date:** 2026-07-26  
**Branch:** `main`  
**Before:** 27 rendered pages (student + teacher)  
**Target:** Reduce whitespace where possible without breaking parity or handwriting space  

---

## Chapter 2 Standard Applied

| Rule | Chapter 1 Status |
|------|------------------|
| Lessons may share pages | Not currently merged — one logical section per page |
| Clear lesson heading required | PASS — every page has `add_lesson_banner()` or analogy banner |
| Spacing separator required | **Gap** — `add_section_separator()` not yet in Ch.1 generator |
| No stranded headings | PASS — QA render confirms no orphan headings |
| No reduced handwriting space | PASS — 72-char underscore lines, 2.0 in drawing boxes preserved |
| No student/teacher page drift | PASS — 27/27 parity verified |

---

## Pages with Excess Unused Space

| Page | Section | Est. fill | Notes |
|------|---------|-----------|-------|
| 1 | Cover | ~55% | Drawing box intentional |
| 18 | Reference intro | ~30% | Intentional — precedes embedded reference images |
| 16 | L4 Vocab + analogy | ~50% | Blank vocab template + one example |
| 21 | L5 Vocab + analogy | ~45% | Blank vocab template only |
| 24 | L6 Vocab + analogy | ~45% | Blank vocab template only |
| 27 | Embedded review | ~40% | Abbreviated review; full review is separate 2-page file |

---

## Merge Candidates Tested (Analysis Only — Not Applied)

| Merge | Expected issue | Verdict |
|-------|----------------|---------|
| L5a + L5a2 (vocab + capitalization) | Teacher answer block overflow; vocab template needs drawing box | **Rejected** |
| L6a + L6a2 (vocab + model sentences) | Same as Ch.2 L7ab — teacher +1 page | **Rejected** |
| L3b + L3c (syn/ant + vocab) | 8 pairs + vocab template exceeds one sheet with teacher keys | **Rejected** |
| L4c + L4d (vocab + create-your-own) | Two analogy frames + vocab template | **Rejected** |
| L2b + L2b2 (planning parts 1+2) | Already split to prevent overflow (Phase 2 fix) | **Rejected** |

**Conclusion:** Same constraint as Chapter 2 — rendered page reduction below 27 requires either smaller student writing areas or teacher/student layout divergence. Neither is permitted.

---

## Recommended Actions (Approved for Implementation)

| Action | Status |
|--------|--------|
| Add `add_section_separator()` helper to Ch.1 generator | **Deferred** — no same-page subsections yet |
| Keep one section per rendered page | **Maintained** |
| Do not reduce vocab drawing box below 2.0 in | **Maintained** |
| Do not merge teacher answer blocks onto shared pages | **Maintained** |

---

## Regeneration Decision

**No packet pagination changes applied.** Current build passes all validation. Review files updated separately (2-page front/back In-Class Chapter Review).

---

## Final Page Counts (Post-Review Update)

| Document | Pages | Status |
|----------|-------|--------|
| Student Shurley Packet | 27 | PASS |
| Teacher Edition | 27 | PASS |
| In-Class Chapter Review | 2 | PASS (≤ 2, front/back printable) |
| In-Class Chapter Review Key | 2 | PASS (≤ 2) |

**Student/teacher parity:** PASS — 27 = 27

---

## Validation Commands Run

```bash
python3 scripts/generate_chapter_01.py
python3 scripts/validate_chapter_01.py   # VALIDATION PASSED
python3 scripts/render_qa.py             # 27/27/2/2 PNG renders
```
