# Phase 2 Plan — Chapter 1 Shurley Packet

**Date:** 2026-07-24  
**Status:** Planning — ready for production step  
**Branch:** `phase-2/chapter-01-gold-standard`

---

## 1. Source Files Inspected

| File | Status | Role |
|------|--------|------|
| `README.md` | Empty | No project overview yet |
| `docs/standards/naming-conventions.md` | Read | Product names, directory layout, filename patterns, lesson labels |
| `docs/standards/packet-content-rules.md` | Read | 4th-grade audience, curriculum integrity, vocabulary standard, instructional rhythm, Lessons 1–6 rules |
| `docs/standards/packet-design-rules.md` | Read | Page setup, typography, layout, QA process |
| `docs/blueprints/Shurley_Packet_Master_Blueprint.docx` | **Not found** | `docs/blueprints/` directory exists but is empty |
| `source-materials/chapter-01/Chapter 1 Guided Notes.docx` | Read | Authoritative source for Lessons 3–6 |
| `source-materials/chapter-01/planning/lesson-01-02-planning.md` | Read | Authoritative source for Lessons 1–2 |
| `archive/Ch. 1 Study Guide - Study Sheet.pdf` | Read (historical only) | Legacy summary sheet — not authoritative for new content |
| `work/chapter-01/chapter-01-student-packet.docx` | Read | Phase 1 student draft (16 pages, pre–gold-standard structure) |
| `work/chapter-01/chapter-01-teacher-key.docx` | Read | Phase 1 teacher key (page-aligned to Phase 1 draft) |
| `work/chapter-01/chapter-01-in-class-chapter-review.docx` | Read | Phase 1 review draft (combined student + key in one file) |
| `packets/student/chapter-01/chapter-01-shurley-packet.docx` | Read (prior build) | Gold-standard attempt — not validated; do not treat as final |
| `packets/teacher-keys/chapter-01/chapter-01-shurley-packet-teacher-edition.docx` | Read (prior build) | Prior build — pagination audit shows page-count mismatch |
| `packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review.docx` | Read (prior build) | Prior build — separate review file exists |
| `packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review-key.docx` | Read (prior build) | Prior build — separate key exists |
| `scripts/generate_chapter_01.py` | Read | Generation script (24 logical page builders) |
| `work/chapter-01/pagination-audit.md` | Read | Current build fails physical page parity (25 student / 23 teacher) |

**Repository tree (top level):**

```
archive/                  # Historical reference only
assets/                   # fonts, images (empty placeholders)
docs/blueprints/          # Empty — blueprint missing
docs/standards/           # Naming, content, design rules (populated)
exports/                  # docx/pdf export targets (empty)
packets/                  # Final deliverables (prior build present)
scripts/                  # generate_chapter_01.py, render_qa.py
source-materials/         # Original teacher materials (do not overwrite)
templates/                # docx/pdf templates (empty)
work/chapter-01/          # Planning, drafts, audits
```

---

## 2. Chapter 1 Lesson Inventory

Content currently represented across supplied source materials:

### Lesson 1 — Discussion and Goal Setting
**Source:** `lesson-01-02-planning.md` only (not in Guided Notes)

| Topic | Confirmed Detail |
|-------|-----------------|
| Discussion expectations | Listen respectfully, wait for turn, stay on topic, link comments |
| Linking comment starters | 5 sentence starters provided |
| Goal types | Short-term vs long-term; academic vs personal |
| Student practice | Sort 6 example goals; choose academic + personal long-term goals with 2–3 action steps each |
| Teacher-only | Ball-passing discussion activity |

### Lesson 2 — Journaling and Letter to Future Me
**Source:** `lesson-01-02-planning.md` only

| Topic | Confirmed Detail |
|-------|-----------------|
| Journal definition | Personal record of thoughts, feelings, experiences, plans, stories |
| Journal topic ideas | 10 topics listed |
| Letter structure | 4 flexible parts (not rigid 3-paragraph requirement) |
| Planning questions | Provided for each letter section |
| Envelope directions | Name, teacher/class, "Do Not Open Until the Last Week of School" |
| Teacher-only | Letter storage and end-of-year return procedure |

### Lesson 3 — Complete Sentences, Synonyms, Antonyms
**Source:** Guided Notes Lesson 3

| Topic | Confirmed Detail |
|-------|-----------------|
| Five sentence parts | Hint references Sentence Jingle; parts: Subject, Verb, Complete sense, Capital letter, End mark (archive confirms list) |
| Synonyms | Definition + 3 examples; blank for "same" meaning |
| Antonyms | Definition + 3 examples; blank for "opposite" meaning |
| Practice | 8 synonym/antonym pairs to circle |
| Vocabulary | **Blank template** — word, definition, synonym, antonym, sentence, drawing box |

### Lesson 4 — Analogies
**Source:** Guided Notes Lesson 4

| Topic | Confirmed Detail |
|-------|-----------------|
| Analogy intro | Spoken and written format examples |
| Four relationship types | Synonym, Antonym, Rhyming, Part-to-Whole (with examples) |
| Guided practice | 4 fill-in analogies with relationship circles |
| Multiple choice | 2 items (weak:strong :: hot:__ ; mouse:house :: __) |
| Vocabulary | Blank template + source analogy example: `encourage : cheer :: easy : simple` |
| Create-your-own | 2 blank analogy frames |

### Lesson 5 — Vocabulary, Capitalization, Editing
**Source:** Guided Notes Lesson 5

| Topic | Confirmed Detail |
|-------|-----------------|
| Vocabulary | Blank template + source analogy: `fraction : whole :: wing : bird` |
| Create-your-own | 2 blank analogy frames |
| Capitalization | 2 passages requiring capitals above words (references Capitalization Reference Sheet — **not in repo**) |
| Editing | 2 sentences — capitals only; write letter above mistakes |

### Lesson 6 — Vocabulary, Capitalization & Punctuation, Editing
**Source:** Guided Notes Lesson 6

| Topic | Confirmed Detail |
|-------|-----------------|
| Vocabulary | Blank template + source analogy: `individual : community :: bird : flock` |
| Create-your-own | 2 blank analogy frames |
| Model sentences | 2 correctly punctuated sentences (source references rule numbers — **omit rule numbers**) |
| Mixed editing | Sentence 1: 6 capitals, 4 commas, 1 period, 1 end mark |
| Mixed editing | Sentence 2: 5 capitals, 2 commas, 1 period, 1 end mark, 1 apostrophe |

### Archive PDF — Historical Reference Only
**File:** `archive/Ch. 1 Study Guide - Study Sheet.pdf`  
Label in archive: "Chapter 1 - Study Guide" — **do not reuse this name**.

| Content | Notes |
|---------|-------|
| Five sentence parts | Matches Guided Notes / Lesson 3 |
| Vocabulary list | encourage, magnify, community, fraction with definitions — **not assigned in Guided Notes** |
| Synonym/antonym definitions | Matches Guided Notes |
| Analogy relationships | Matches Guided Notes |
| Analogy examples | Nice:Kind :: Mad:Angry; Finger:Hand :: Tree:Forest |
| Cap/punct rules | References textbook pages 24–25, 29–30 — **not reproduced** |
| Editing example | `kevin asked bobby bill and tonya to his birthday party` (4 capitals, 2 commas, 1 end mark) |

---

## 3. Recommended Packet Page Order

Target: **24 student pages** with teacher edition mirroring exactly (1:1 page parity verified by LibreOffice render, not logical builder count alone).

| Page(s) | Section | Primary Source |
|---------|---------|----------------|
| 1 | Cover — Chapter 1 Shurley Packet, name/date/teacher, drawing prompt | New (design rules) |
| 2 | Lesson 1 — Learn: discussion expectations, linking starters, goal concepts | Planning source |
| 3 | Lesson 1 — Practice Together / Independently / Apply / Memory Check / Teacher Check | Planning source |
| 4 | Lesson 2 — Learn: journal definition, topic ideas | Planning source |
| 5 | Lesson 2 — Practice Together: journal entry | Planning source |
| 6 | Lesson 2 — Planning organizer, Part 1 (Who I Am / Fourth Grade) | Planning source |
| 7 | Lesson 2 — Planning organizer, Part 2 (Goals / Future Self message) | Planning source |
| 8 | Lesson 2 — Model letter (fourth-grade example) | New (exercises confirmed skill) |
| 9 | Lesson 2 — Supported writing template | Planning source |
| 10 | Lesson 2 — Final draft, envelope directions, Memory Check, Teacher Check | Planning source |
| 11 | Lesson 3 — Learn: five sentence parts, Remember box, synonym/antonym intro | Guided Notes |
| 12 | Lesson 3 — Practice Together: 8 synonym/antonym pairs; create-your-own pair | Guided Notes |
| 13 | Lesson 3 — Apply: blank vocabulary template; Memory Check; Teacher Check | Guided Notes |
| 14 | Lesson 4 — Learn: analogy intro, four relationship types table | Guided Notes |
| 15 | Lesson 4 — Practice Together: 4 guided analogies + 2 multiple choice | Guided Notes |
| 16 | Lesson 4 — Apply: blank vocabulary + source analogy example; create 2 analogies | Guided Notes |
| 17 | Lesson 4 — Apply: create-your-own analogies; Memory Check; Teacher Check | Guided Notes |
| 18 | Lesson 5 — Apply: blank vocabulary + source analogy; create 2 analogies | Guided Notes |
| 19 | Lesson 5 — Learn/Practice: capitalization passages (2) | Guided Notes |
| 20 | Lesson 5 — Practice: editing — capitals (2 sentences) | Guided Notes |
| 21 | Lesson 6 — Apply: blank vocabulary + source analogy; create 2 analogies | Guided Notes |
| 22 | Lesson 6 — Learn: capitalization and punctuation model sentences (no rule numbers) | Guided Notes |
| 23 | Lesson 6 — Practice: mixed editing (2 sentences with error counts) | Guided Notes |
| 24 | In-Class Chapter Review (embedded end-of-packet page) | All lessons + archive editing example |

**Separate files (not embedded pages):**

- In-Class Chapter Review — condensed 1-page classroom activity
- In-Class Chapter Review Key — matching answer key

---

## 4. Content to Preserve

- All Guided Notes exercises for Lessons 3–6 (sentence parts, synonym/antonym pairs, analogy table, guided practice, capitalization passages, editing sentences with error counts).
- Source analogy examples exactly as written: `encourage : cheer :: easy : simple`, `fraction : whole :: wing : bird`, `individual : community :: bird : flock`.
- Blank vocabulary templates from Guided Notes (word, definition, synonym, antonym, sentence, drawing box).
- Lessons 1–2 content from `lesson-01-02-planning.md` (linking starters, goal sorting examples, journal topics, letter parts, envelope label text).
- Archive editing sentence for review use: `kevin asked bobby bill and tonya to his birthday party`.
- Five sentence parts: Capital letter, End mark, Complete sense, Subject, Verb.
- Instructional section labels: Learn, Practice Together, Practice Independently, Apply, Memory Check, Teacher Check.
- Product name: **Shurley Packet** (cover title, headers, filenames).

---

## 5. Content to Improve

| Area | Current State | Improvement |
|------|---------------|-------------|
| Instructional rhythm | Guided Notes lacks section labels | Add Learn → Practice Together → Practice Independently → Apply → Memory Check → Teacher Check per lesson |
| Lesson 2 scaffolding | Phase 1 draft is single-page letter | Expand with planning organizer, model letter, supported template, final draft page |
| Layout / writing space | Guided Notes cramped in places | Generous 72-char underscore lines, 2.0 in drawing boxes, Remember boxes |
| Naming | Archive says "Study Guide"; Phase 1 draft says "Practice Packet" | Use "Shurley Packet" everywhere |
| Lesson 6 rule numbers | Source references textbook rule numbers | Omit rule numbers; use error-count editing cues only |
| Vocabulary | Phase 1 draft pre-fills archive words | Keep **blank templates** per content rules; teacher assigns vocabulary |
| Teacher edition | Phase 1 key is abbreviated | Full page-for-page mirror with timing, prompts, misconceptions, procedures |
| In-Class Review | Phase 1 combines student + key in one file | Separate student review and review key files |
| Pagination | Prior build: 25 physical student / 23 teacher pages | Fix generator until LibreOffice-rendered PDFs match exactly |
| Cover drawing prompt | Minor wording differences across drafts | Use: "Draw a picture about something you are learning in Chapter 1" |

---

## 6. Missing Information or Source Gaps

| Gap | Impact | Proposed Handling |
|-----|--------|-------------------|
| `Shurley_Packet_Master_Blueprint.docx` not in repo | No visual template reference | Establish Gold Standard from standards docs + this plan; first Chapter 1 packet sets precedent |
| `README.md` empty | No onboarding context | Out of scope for this step; note for later |
| Capitalization Reference Sheet | Lesson 5 source references it | Tell teachers to supply separately; do not invent rule list |
| Sentence Jingle lyrics | Guided Notes hints at it | Reference hint only; do not reproduce lyrics |
| Textbook rule numbers (pages 24–25, 29–30) | Archive and Lesson 6 source reference them | Omit entirely |
| Confirmed vocabulary word list | Guided Notes templates are blank; archive lists 4 words | Treat vocabulary as **teacher-assigned**; archive words may appear in review key as sample answers only |
| Kid-friendly vocabulary meanings | Not in source materials | Author may write interpretations in teacher edition only when teacher assigns a confirmed word |
| Physical page parity | Pagination audit FAIL on prior build | Mandatory LibreOffice render QA before calling production complete |
| Phase 1 vs Gold Standard conflict | `work/chapter-01/` drafts differ from `packets/` build | Treat `work/` drafts as historical; produce fresh files in `packets/` |

---

## 7. Proposed Student Packet Filename

```
packets/student/chapter-01/chapter-01-shurley-packet.docx
```

---

## 8. Proposed Teacher Key Filename

```
packets/teacher-keys/chapter-01/chapter-01-shurley-packet-teacher-edition.docx
```

---

## 9. Proposed In-Class Chapter Review Filename

```
packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review.docx
```

---

## 10. Proposed Production Sequence

1. **Align generator to this plan** — Update `scripts/generate_chapter_01.py`:
   - 24 logical pages matching Section 3 order
   - Blank vocabulary templates (no pre-filled archive words in student pages)
   - Instructional rhythm labels on every lesson
   - Teacher edition with 24 matching pages including ball-passing and letter-storage procedures
2. **Generate student packet** → `packets/student/chapter-01/chapter-01-shurley-packet.docx`
3. **Generate teacher edition** → `packets/teacher-keys/chapter-01/chapter-01-shurley-packet-teacher-edition.docx`
4. **Generate In-Class Chapter Review** → `packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review.docx`
5. **Generate review key** → `packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review-key.docx`
6. **Render QA** — LibreOffice → PDF → page images; inspect every page
7. **Pagination audit** — Confirm student and teacher physical page counts match
8. **Structural validation** — No "Study Guide" label; source files unchanged
9. **Write build report** → `work/chapter-01/phase-2-build-report.md`
10. **Do not overwrite** anything in `source-materials/` or `archive/`

---

## 11. Validation Checklist

- [ ] No "Study Guide" label in any generated file (title, header, footer, or body)
- [ ] Product titled **Shurley Packet** on cover and in filenames
- [ ] Student packet includes Lessons 1–6 plus embedded In-Class Chapter Review (page 24)
- [ ] Every lesson includes Memory Check and Teacher Check blocks
- [ ] Instructional rhythm labels used (Learn, Practice Together, Practice Independently, Apply)
- [ ] Vocabulary pages use blank templates — no pre-filled words unless teacher confirms
- [ ] All Guided Notes exercises preserved for Lessons 3–6
- [ ] Source analogy examples reproduced accurately
- [ ] Lesson 6 editing uses error counts, not rule numbers
- [ ] Teacher edition mirrors student page order with **identical physical page count**
- [ ] Teacher edition includes ball-passing activity (Lesson 1) and letter storage procedure (Lesson 2)
- [ ] In-Class Chapter Review is a separate file with matching separate key file
- [ ] Review covers all major Chapter 1 skills and includes one short application task (Part F)
- [ ] Review is not labeled or described as test prep or take-home study resource
- [ ] Generous handwriting space; drawing boxes ≥ 2.0 in; no large blank waste areas
- [ ] Fourth-grade reading level throughout student-facing text
- [ ] Source materials in `source-materials/` and `archive/` unchanged
- [ ] LibreOffice render QA passes (no clipping, overlap, awkward breaks, cramped space)

---

## 12. Exact List of Files to Create in the Next Step

| # | File | Type |
|---|------|------|
| 1 | `packets/student/chapter-01/chapter-01-shurley-packet.docx` | Student instructional workbook |
| 2 | `packets/teacher-keys/chapter-01/chapter-01-shurley-packet-teacher-edition.docx` | Page-for-page teacher edition |
| 3 | `packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review.docx` | Standalone in-class review (student) |
| 4 | `packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review-key.docx` | Standalone review answer key |

**Supporting file likely updated (not a deliverable):**

- `scripts/generate_chapter_01.py` — align to this plan before generation

**Report to update after production:**

- `work/chapter-01/phase-2-build-report.md`

**Files explicitly NOT created in next step:**

- No changes to `source-materials/chapter-01/Chapter 1 Guided Notes.docx`
- No changes to `archive/Ch. 1 Study Guide - Study Sheet.pdf`
- No blueprint file (source missing)
- No DOCX files in `work/chapter-01/` (drafts remain as-is; finals go to `packets/`)

---

## Major Decisions (Pre-Production)

1. **Product name:** Shurley Packet — never Study Guide.
2. **Lessons 1–2:** Built from `lesson-01-02-planning.md`; not present in Guided Notes.
3. **Lessons 3–6:** Preserve and improve Guided Notes content; add instructional rhythm and spacing.
4. **Vocabulary:** Blank templates in student packet; teacher assigns words. Archive four words inform review key sample answers only.
5. **Rule numbers:** Omitted from all generated materials.
6. **Blueprint:** Missing — this packet establishes the Gold Standard by precedent.
7. **Page target:** 24 student pages with 24 matching teacher pages (verify by render, not builder count).
8. **Phase 1 drafts:** Reference only; superseded by this plan.

## Unresolved Questions

1. Should the four archive vocabulary words (encourage, magnify, community, fraction) be pre-assigned by the teacher edition as recommended words, or left entirely open?
2. Is 24 pages the right length when printed, or should Lesson 2 be compressed if handwriting space tests tight?
3. Should the embedded page-24 review match the standalone In-Class Chapter Review exactly, or may the standalone be a shorter classroom checkpoint?
4. When will the Capitalization Reference Sheet be added to the repository (if ever)?
5. Should `docs/blueprints/Shurley_Packet_Master_Blueprint.docx` be created from the first successful Chapter 1 build?
