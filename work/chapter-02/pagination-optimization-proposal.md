# Chapter 2 Pagination Optimization Proposal

**Date:** 2026-07-26  
**Before:** 28 rendered pages (student + teacher)  
**Target:** 24 ± 2 rendered pages  

## Pages with excessive unused space (pre-pass)

| Page | Section | Est. fill | Notes |
|------|---------|-----------|-------|
| 5 | L1 Practice 1–2 | ~50% | Two classification items only |
| 8 | L2 Practice 1–2 | ~60% | Same pattern |
| 13 | L4 Practice 1–2 | ~55% | Same pattern |
| 20 | L7 Vocab | ~45% | Vocab template + drawing box |
| 27 | L9 Practice 1–3 | ~50% | Three items, cap/punct on next page |

## Merges attempted

| Merge | Rendered result | Verdict |
|-------|-----------------|---------|
| L1b + L1c (one section) | 27 logical → 28 rendered (+overflow) | Rejected — teacher overflow |
| L2bc, L4bc, L6ab, L8bc | 24 logical → 28 rendered | Rejected — multiple overflows |
| L7 vocab + learn + analogy | Student 27, teacher 28 | Rejected — parity fail |
| L9 practice + cap/punct | 27 logical → 28 rendered | Rejected — overflow |

## Applied (print-efficiency without page-count change)

| Change | Effect |
|--------|--------|
| L1/L2/L4: Practice item 3 on practice page | Fills pages 5, 8, 13 |
| L1/L2/L4: Memory Check follows practice when room allows | Pages 5, 8, 13; apply pages 6, 9, 14 slimmer |
| L1/L2/L4: Apply + Teacher Check on follow-on page | No split activities |
| L3/L6/L8: Practice item 3 on practice page | Fills pages 10, 18, 25 |
| L3/L6/L8: Apply or memory on follow-on page | Pages 11, 19, 26 |
| `add_section_separator()` helper | Ready for future same-page subsection breaks |

## Final pass merge matrix (2026-07-26)

| Merge tested | Rendered result | Verdict |
|--------------|-----------------|---------|
| L1bc / L2bc / L4bc (practice + apply, one banner) | 27 logical → 28 rendered | Rejected — overflow |
| L7ab (vocab + analogy + learn, 1.2" drawing box) | Student 26, teacher 27 | Rejected — parity fail |
| L7ab tight (0.9" drawing box) | 26 / 26 | Rejected — reduces student writing space |
| L6ab / L8bc / L3bc | Student ≤27, teacher +1 | Rejected — parity fail |
| L9ab (practice + cap/punct) | 27 logical → 28 rendered | Rejected — overflow |
| L1c + L2a cross-lesson (full content) | 27 logical → 28 rendered | Rejected — overflow |

**Conclusion:** Rendered page reduction below 28 requires either smaller student writing areas or teacher/student layout divergence. Neither is permitted.

## Expected vs actual page reduction

| Metric | Expected | Actual |
|--------|----------|--------|
| Rendered pages | 24–26 | **28** (unchanged) |
| Logical sections | 28 | **28** |
| Whitespace on practice pages | Reduced | **Yes** — L1–L4, L6, L8 practice pages |
| Whitespace on apply-only pages | Reduced | **Partial** — memory moved off apply pages |

Full section merges that preserve writing space exceed one rendered sheet when teacher inline keys are included. Further rendered-page reduction requires either lighter teacher adjunct content or fewer items per merged page (not permitted).
