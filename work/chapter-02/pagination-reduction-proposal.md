# Chapter 2 Pagination Reduction Proposal

**Date:** 2026-07-26  
**Current:** 30 pages (student)  
**Target:** 24 ± 2 pages  
**Constraint:** Do not reduce writing space, classification workspace, readability, or fourth-grade usability.

## Root cause analysis

| Factor | Pages lost | Notes |
|--------|------------|-------|
| One Word section per micro-page | +6 forced | `(continued)` splits with sparse content (L1b/c, L2b/c, L9a2, L9c) |
| Blueprint split across 2 sections | +1 | Page 2 ~60% full; page 3 poster + 4 bullets ~50% full |
| L5 a/an drill split | +1 | 9 one-line items fit on one page with Learn |
| L7/L8 vocab split from Learn | +2 | Vocab template + learn each under-filled |
| L9 cap/punct vs review pointer | +1 | Cap/punct + memory check fit together |
| Duplicate lesson banners | spacing | `(continued)` headers add vertical waste — remove on merges |

**Not reducing:** classification blank lines (3), apply blocks (4 lines), memory/teacher checks, GN sentence count, blueprint poster content.

## Proposed merges (−6 pages → 24)

| Change | Saves | Rationale |
|--------|-------|-----------|
| Merge `page_blueprint_1` + `page_blueprint_2` | 1 | Both posters at 2.8" height + compact Q&A/types text fits one page |
| Merge `page_l1b` + `page_l1c` | 1 | Practice 1–3 + apply + checks; page 5 currently ~40% empty |
| Merge `page_l2b` + `page_l2c` | 1 | Same pattern as L1 |
| Merge `page_l5a` + `page_l5b` | 1 | Learn + full a/an drill + S. + classify 1–2 |
| Merge `page_l7a` + `page_l7a2` | 1 | Vocab template + analogy + sentence-type learn |
| Merge `page_l9a` + `page_l9a2` | 1 | Three L9 practice sentences on one page |

**Deferred (risk overflow):** L3b merge, L4bc merge, L8a/a2 merge, L9b+c merge — monitor after render.

## Additional fixes

- Footer `is_linked_to_previous = False` — fixes all pages showing "Page 30"
- Remove redundant `(continued)` banners on merged pages
- Teacher edition: mirror student layout; model classifications adjacent to each practice item

**Approved for application:** 2026-07-26 repair pass.

## Outcome (2026-07-26 repair pass)

| Proposed merge | Applied? | Result |
|----------------|----------|--------|
| Blueprint 1+2 | No | Overflow — Core Five + Mastering posters + text exceed one page |
| L1b + L1c | No | Teacher edition +1 page overflow vs student |
| L2b + L2c | No | Same parity overflow |
| L5a + L5b | Partial | a/an drill merged into L5a Learn page; classify split kept |
| L7a + L7a2 | No | Vocab + analogy + learn overflow; kept split |
| L9a + L9a2 | **Yes** | Three L9 practice sentences fit one page (p27) |
| L9 cap/punct + review (l9c) | **Yes** | Merged into page_l9b |
| Footer fix | **Yes** | Correct page numbers |
| Teacher mirrored layout | **Yes** | 28/28 parity; compact classification keys |

**Final count:** 30 → **28** pages (student + teacher). Target 24 ± 2 not fully reached without risking overflow or reduced writing space.
