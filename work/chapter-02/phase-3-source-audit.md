# Phase 3 Source Audit — Chapter 2 Shurley Packet

**Date:** 2026-07-26 (updated with visual + slide resources)  
**Branch:** `phase-3/chapter-02-gold-standard`  
**Status:** Source audit complete — **awaiting teacher approval before DOCX generation**

---

## Repository Confirmation

| Check | Result |
|-------|--------|
| Working directory | `/Users/owen/Projects/shurley-packet-system` |
| Branch | `phase-3/chapter-02-gold-standard` |
| Git status | Untracked Chapter 2 audit/planning files present |

---

## 1. Every Chapter 2 Source File Found

### Authoritative Text Source

| File | Status | Role |
|------|--------|------|
| `source-materials/chapter-02/Chapter 2 Guided Notes.docx` | **Found** | Sole authoritative text source — 9 lessons, 119 paragraphs, classification sentences, vocabulary templates, analogies, cap/punct item |

### Visual Resources (NEW — 2026-07-26)

| File | Status | Role |
|------|--------|------|
| `source-materials/chapter-02/visuals/Core_Five_English_Grammar_Guide.png` | **Found** | Poster-style reference — Core Five labels, questions, definitions, color coding, sample sentence |
| `source-materials/chapter-02/visuals/Mastering_the_Sentence_Blueprint.png` | **Found** | Chapter overview — Pattern 1, four sentence kinds, Mover/Shaker, 4-step classify flow, quick-ref table |

### Slide Decks (NEW — image-only PPTX; no extractable text)

| File | Slides | Primary Lesson | Notes |
|------|--------|----------------|-------|
| `source-materials/chapter-02/slides/Operation_Pattern_1.pptx` | 10 | 1 | Detective theme; SN/V profiles; Interrogation Protocol; Case Studies |
| `source-materials/chapter-02/slides/Sentence_Blueprint.pptx` | 15 | 1 | Blueprint specimens; Q&A flow on Guided Notes sentences |
| `source-materials/chapter-02/slides/Adverb_Blueprint.pptx` | 19 | 2 | **Primary adverb deck** — guided practice, oral discussion, Classroom Practice 5 |
| `source-materials/chapter-02/slides/Adverb_Blueprint_(2).pptx` | 19 | 2 | Duplicate of primary adverb deck |
| `source-materials/chapter-02/slides/Adverb_Blueprint_(3).pptx` | 19 | 2 | Duplicate of primary adverb deck |
| `source-materials/chapter-02/slides/The_Grammar_Blueprint-3.pptx` | 13 | 3 | Mover/Shaker; Inspector's Checklist; Lesson 3 practice |
| `source-materials/chapter-02/slides/Building_Adjective_Blueprints.pptx` | 21 | 4 | Three adjective questions; oral discussion; Guided Notes sentences |
| `source-materials/chapter-02/slides/Article_Adjective_Blueprint.pptx` | 15 | 5 | a/an system check; article blocks; Guided Notes sentences |
| `source-materials/chapter-02/slides/The_Sentence_Blueprint.pptx` | 15 | 6 | Construction Site series; Lesson 6 practice sentences |
| `source-materials/chapter-02/slides/Sentence_Construction_Blueprint.pptx` | 13 | 7–9 | Four kinds; End Mark Flow; The Divide; Classroom Practice 10; editing |
| `source-materials/chapter-02/slides/Analogy_Codebreaker.pptx` | 15 | 7–8 | Analogy training; relationship types |

**Slide QA note:** All decks are fully image-based (1 image per slide). No speaker notes. Slideshow audit required before classroom use per `docs/standards/slideshow-qa-rules.md`.

### Reference Folder

| Path | Status |
|------|--------|
| `source-materials/chapter-02/reference/` | **Empty** — no Chapter 2-specific reference PDFs |

### Reusable Chapter 1 Protected Reference

| File | Role |
|------|------|
| `source-materials/reference/shurley-capitalization-punctuation-reference.pdf` | Lesson 9 rule-number exercise |
| `source-materials/reference/shurley-capitalization-punctuation-reference-transcription.md` | Rule lookup for teacher key |
| `source-materials/reference/shurley-capitalization-punctuation-reference-page-1.png` | Punctuation embed (Ch. 1) |
| `source-materials/reference/shurley-capitalization-punctuation-reference-page-2-oriented.png` | Capitalization embed (Ch. 1) |

### Gold-Standard Model Files (Chapter 1)

| File | Role |
|------|------|
| `scripts/generate_chapter_01.py` | Generation pattern, layout helpers, teacher notes |
| `scripts/validate_chapter_01.py` | Validation pattern (parity, Study Guide check, protected PDF hash) |
| `work/chapter-01/phase-2-build-report.md` | Production baseline (27/27/1/1 pages) |
| `docs/standards/*.md` | Naming, content, design, student-resource QA, slideshow QA |

---

## 2. Confirmed Grammar Concepts (Authoritative Hierarchy)

Content is tagged by source tier:

- **T1 — Guided Notes.docx** (highest text authority)
- **T2 — Visual PNGs** (authoritative for labels/questions shown on poster)
- **T3 — Slide decks** (authoritative for oral Q&A flow, marking conventions, classroom sequence; teacher-created NotebookLM visuals — not Shurley textbook text)
- **T4 — Proposed** (in `teacher-approval-checklist-proposed.md` — requires teacher sign-off)

### Core Five Labels and Questions

| Label | Full Name | Questions | Definition (best available source) | Source |
|-------|-----------|-----------|-----------------------------------|--------|
| **SN** | Subject Noun | Who? / What? | Names a person, place, thing, or idea; tells who or what the sentence is about | T2, T3 |
| **V** | Verb | What is being said about the subject? | Shows action or state of being; tells what the subject does or is | T2, T3 |
| **Adv** | Adverb | How? / When? / Where? | Modifies a verb, adjective, or another adverb | T1 (pattern), T2, T3 |
| **Adj** | Adjective | What kind? / Which one? / How many? | Describes a noun or a pronoun | T1, T2, T3 |
| **A** | Article Adjective | *(none — memorize)* | a, an, the — also known as noun markers | T2, T3 |

**Adverb extension (slide only):** One adverb title slide also lists **To what extent?** as a fourth adverb question. Guided Notes show three blanks for adverb questions. Treat fourth question as **T3 — teacher verify** before printing in student packet.

**Guided Notes adjective questions** use prompts What ___? / Which ___? / How ___? without printed answers. Slide + poster authority: **What kind? / Which one? / How many?**

### Pattern and Classification

| Concept | Confirmed Detail | Source |
|---------|------------------|--------|
| Pattern 1 | **SN V** labeled **P1** | T2, T3 |
| Pattern progression | L1: SN V → L2–3: SN V Adv Adv → L4: Adj Adj SN V Adv Adv → L5–9: A Adj Adj SN V Adv Adv | T1 |
| Subject/predicate divide | Vertical slash **directly in front of the verb** | T3 |
| End Mark Flow | After classifying words: identify punctuation → feeling/purpose → sentence type → label | T3 |
| Skill Check oral script | Example: *"Exclamation point, strong feeling, exclamatory sentence. It is labeled E."* | T3 |
| 4 Steps to Classify | 1. Ask the question 2. Name the word 3. Identify its job 4. Label with correct abbreviation | T2 |
| Interrogation Protocol | Always ask for **subject first**, then **verb** | T3 |
| Mover & Shaker | Move an adverb to sentence front for variety; **comma required after moved adverb** | T3 |
| Inspector's Checklist | Subject, Verb, Complete Sense, Capital Letter, End Mark | T3 |
| Intensifiers | Words like **very** classified as **Adv** modifying an **Adj** (e.g., *very soothing*) | T3 (shown, not titled in Guided Notes) |
| Article adjectives also known as | **noun markers** (poster); **determiners / noun markers** (T4 proposed for two blanks) | T2, T4 |

### Sentence Types

| Type | Definition | Label | Source |
|------|------------|-------|--------|
| Declarative | Makes a statement | **D** | T1 (definition), T2, T3 |
| Imperative | Gives a command | **Imp** | T1 (definition), T2, T3 |
| Interrogative | Asks a question | **Int** | T1 (definition), T2, T3 |
| Exclamatory | Expresses strong feeling | **E** | T1 (definition), T2, T3 |

**Correction from prior audit:** Slides and poster use **Imp** and **Int**, not **I** and **Int** as previously proposed. Teacher must confirm classroom oral convention matches slide labels.

### Parts of Speech (Lesson 7 blank row)

Guided Notes: four blanks, no printed answers.  
Best-supported fill from chapter arc: **Noun, Verb, Adjective, Adverb** (T4 — teacher verify).

### Noun Categories (Lesson 1)

Guided Notes: four numbered blanks, no answers.  
Slides + poster: **person, place, thing, idea** (T2, T3 — teacher verify for packet print).

### Verb Types (Lesson 1)

Guided Notes: action vs linking verb fill-ins blank.  
Slides: **action** or **state of being** (T3 — teacher verify exact wording).

---

## 3. Lesson-by-Lesson Topic Inventory

All classification sentences traced to Guided Notes unless noted.

### Lesson 1 — Nouns, Verbs, SN–V (Pattern 1)

| Topic | Source |
|-------|--------|
| Noun naming categories | 4 blanks — **T3/T2: person, place, thing, idea** |
| Subject questions | **Who? / What?** (T2, T3) |
| Verb types | action / state of being (T3) |
| Q&A flow | Interrogation Protocol (T3) |
| Pattern | SN V / P1 |
| Sample | S. Ships sailed. |
| Practice | Plane flew. / Ladybugs crawled. / Boys raced. |
| Apply | Write your own SN–V sentence |
| Visuals | Core Five poster, Operation Pattern 1, Sentence Blueprint |

### Lesson 2 — Adverbs, SN–V–Adv–Adv

| Topic | Source |
|-------|--------|
| Adverb questions | How? / When? / Where? (T2, T3) |
| Adverbs modify | verbs / adjectives / adverbs (T3 answer slide) |
| Abbreviation | **Adv** (T1 pattern) |
| Q&A flow | Go to verb first; ask adverb questions (T3) |
| Sample | S. Ships sailed slowly away today. |
| Practice | Planes flew. / Planes flew quickly away today. / Spiders crawled around very quickly. |
| Apply | Write your own SN–V–Adv–Adv sentence |
| Visuals | Adverb Blueprint |

### Lesson 3 — Adverb Classification + Mover/Shaker

| Topic | Source |
|-------|--------|
| Classification only in Guided Notes | No new Learn text |
| Mover/Shaker rule | Move adverb to front + comma (T3) |
| Inspector's Checklist | 5 parts of complete sentence (T3) |
| Practice | Bees buzzed angrily around today. / Rabbits hopped around everywhere. / Anthony listened very carefully yesterday. |
| Apply | Write your own SN–V–Adv–Adv sentence |
| Visuals | The Grammar Blueprint-3, Sentence Blueprint |

### Lesson 4 — Adjectives, Adj–Adj–SN–V–Adv–Adv

| Topic | Source |
|-------|--------|
| Definition | "An adjective describes a noun or a pronoun." (T1) |
| Questions | What kind? / Which one? / How many? (T2, T3) |
| Abbreviation | **Adj** (T1 pattern) |
| Oral flow | Go to subject noun first; ask adjective questions (T3) |
| Sample | S. Those five cargo ships sailed slowly away today. |
| Practice | That owl flew silently. / That large white owl flew silently overhead tonight. / Several little red ladybugs crawled everywhere yesterday. |
| Apply | Write your own full-pattern sentence |
| Visuals | Building Adjective Blueprints |

### Lesson 5 — Article Adjectives, A–Adj–Adj–SN–V–Adv–Adv

| Topic | Source |
|-------|--------|
| Articles | a, an, the (T2, T3 — Guided Notes blanks) |
| Abbreviation | **A** (T1 pattern) |
| Also known as | noun markers (T2); determiners (T4 proposed) |
| a/an practice | 9 confirmed sentences (T1) |
| Sample | S. The five cargo ships sailed slowly away. |
| Practice | The girls giggled loudly. / The four happy girls giggled loudly today. / A huge whale swam very slowly away. |
| Apply | Write your own full-pattern sentence |
| Visuals | Article Adjective Blueprint |

### Lesson 6 — Full-Pattern Classification

| Topic | Source |
|-------|--------|
| Classification only | No new Learn text |
| Practice | The nice young doctor spoke very kindly today. / A little yellow duck waddled slowly away. / An enormous black bug flew around today. |
| Classroom Practice preview | "Time to Build!" → Classroom Practice 6 (T3) |
| Visuals | The Sentence Blueprint |

### Lesson 7 — Vocabulary, Sentence Types, Extended Classification

| Topic | Source |
|-------|--------|
| Vocabulary template | Blank — teacher-assigned |
| Analogy | soothing : smoothing :: flying : trying → **rhyming** (T1) |
| Sentence types | Four definitions + label blanks (T1); labels D/Imp/Int/E (T2, T3) |
| Parts of Speech | Four blanks (T4 proposed: Noun, Verb, Adjective, Adverb) |
| End Mark Flow + The Divide | T3 |
| Sample | S. The two pirate ships appeared quite suddenly! |
| Practice | The music played softly. / The very soothing music played softly tonight. / Several urgent messages arrived very early today. |
| Visuals | Sentence Construction Blueprint, Analogy Codebreaker, Mastering poster |

### Lesson 8 — Vocabulary, Sentence-Type Classification

| Topic | Source |
|-------|--------|
| Vocabulary template | Blank — teacher-assigned |
| Analogy | urgent : important :: answer : reply → **synonym** (T1) |
| Intensifier practice | *extremely*, *very* in practice sentences (T1); Adv→Adj labeling in slides (T3) |
| Practice | A young reporter glanced curiously around. / The stormy winter sky darkened suddenly! / An extremely frightened girl screamed very loudly! |
| Visuals | Sentence Construction Blueprint (classification specimens), Analogy Codebreaker |

### Lesson 9 — Full Classification + Cap/Punct

| Topic | Source |
|-------|--------|
| Practice | Two beautiful butterflies flew slowly away. / An old teapot whistled very loudly today. / Several angry bees circled around nearby! |
| Cap/punct | Rule numbers for bold corrections in: `No, Alex did not go home with John during carpool on Friday.` |
| Bold marks | N, comma, A, J, F, period (T1) |
| Editing model | Classroom Practice 10 editing slide (T3 — **teacher-created example**, not Guided Notes sentence) |
| Visuals | Sentence Construction Blueprint (Classroom Practice 10 preview + editing answers) |

---

## 4. Confirmed Vocabulary

| Item | Status |
|------|--------|
| Assigned vocabulary words | **None confirmed** — Lessons 7–8 blank templates |
| Vocabulary fields | Word, Definition, Synonym, Antonym, Sentence, Drawing box |
| Source analogies | L7 rhyming / L8 synonym — examples only, not vocabulary list |

---

## 5. Classification Item Count

| Lesson | S. | Numbered | Write-Your-Own |
|--------|-----|----------|----------------|
| 1 | 1 | 3 | 1 |
| 2 | 1 | 3 | 1 |
| 3 | 0 | 3 | 1 |
| 4 | 1 | 3 | 1 |
| 5 | 1 | 3 | 1 |
| 6 | 0 | 3 | 0 |
| 7 | 1 | 3 | 0 |
| 8 | 0 | 3 | 0 |
| 9 | 0 | 3 | 0 |

**Total:** 28 classification sentences in Guided Notes.

---

## 6. Question Types in Source

| Type | Lessons |
|------|---------|
| Fill-in (definitions, questions, abbreviations) | 1–2, 4–5, 7 |
| Sentence classification | 1–9 |
| Pattern labeling | 1–5 |
| a/an article selection | 5 |
| Vocabulary template | 7–8 |
| Analogy relationship selection | 7–8 |
| Parts of speech listing | 7 |
| Cap/punct rule-number ID | 9 |
| Write-your-own sentence | 1–5 |
| Drawing box | 7–8 |

**Not in Guided Notes:** separate editing rewrite passage (Ch. 1 style), jingle lyrics, pre-filled vocabulary.

---

## 7. Remaining Unknowns and Gaps

| Gap | Impact | Handling |
|-----|--------|----------|
| Lesson 1 noun/verb fill-in exact wording | Learn section incomplete in DOCX | **STOP** — teacher confirms T2/T3 proposals |
| Adverb "To what extent?" | Slide shows 4th question; Guided Notes has 3 blanks | Teacher chooses 3 vs 4 questions |
| Sentence type labels in Guided Notes | Blanks only | **Confirmed from slides:** D, Imp, Int, E |
| Parts of Speech four words | Blanks only | T4 proposed — teacher verify |
| **Noun Checks** (oral procedure) | Referenced in task; **no slide or Guided Notes title found** | Document as oral classroom step; teacher supply script |
| **Revision strategies** (beyond Mover/Shaker) | No dedicated slide deck | Mover/Shaker confirmed; other strategies **teacher verify** |
| Intensifier formal definition | Shown in practice only | Teach as Adv modifying Adj; no separate label in source |
| Classification marking when fewer than pattern slots | e.g., "The girls giggled loudly." | Teacher convention required |
| Quantifier words (Several, Those, five) | Slides label Several/Those as Adj; five as Adj | Confirm A vs Adj for determiners/quantifiers |
| Three duplicate Adverb decks | Which is canonical? | Use `Adverb_Blueprint.pptx`; archive duplicates |
| Slide Classroom Practice sentences | Some differ from Guided Notes | Slides support instruction; **packet uses Guided Notes sentences only** |
| Classroom Practice 10 editing sentence | Slide-only teacher-created example | Do not embed in packet unless teacher approves |
| Lesson 9 uncorrected baseline | Not in source | Use bold-marked sentence only |
| Jingle lyrics | Not in any source | Hint-only in teacher notes |
| `source-materials/chapter-02/reference/` | Empty | No Ch. 2 reference PDF to embed |

---

## 8. Content That Must Not Be Invented

- Shurley jingle lyrics
- Vocabulary words or definitions (keep blank templates)
- Classification sentences beyond the 28 in Guided Notes
- New analogy examples beyond L7/L8 source lines (slide deck has **teacher-created** extra analogies — do not copy into packet)
- Paraphrased capitalization/punctuation rules
- Slide-only Classroom Practice sentences substituted for Guided Notes items
- "Study Guide" language
- Renamed product title without teacher approval

---

## 9. Proposed Packet Architecture

**Student-facing title:** Chapter 2 Shurley Packet (per `docs/standards/naming-conventions.md` and Ch. 1 precedent)

**Estimated pages:** 24 ± 2 student pages + matching teacher edition

| Block | Pages (est.) | Content |
|-------|--------------|---------|
| Cover | 1 | Name, date, teacher, drawing prompt |
| Reference insert | 1–2 | **The Sentence Blueprint** (proposed — see below; not yet designed) |
| Lessons 1–5 | 14–16 | Learn + Practice Together + Apply + Memory Check + Teacher Check |
| Lessons 6–9 | 8–10 | Classification-heavy; L7–8 vocabulary/analogy; L9 cap/punct |
| In-Class Chapter Review | separate 1–2 pp | Source-only sentences per teacher-approval policy |

**Reference handling (Lesson 9):** Point students to Chapter 1 **Capitalization and Punctuation Reference** — do not re-embed unless teacher requests.

**Visual integration:** Embed or reference Core Five / Sentence Blueprint poster pages early (after cover or end of L1 Learn). Use slide-derived diagrams only after teacher approves T3 content for print.

---

## 10. Proposed Student Reference Section — "The Sentence Blueprint"

**Status:** Planned only — **no page created yet**

Single spread (likely 1–2 pages) synthesizing T1/T2/T3 confirmed content:

| Label | Name | Question(s) | Notes |
|-------|------|-------------|-------|
| SN | Subject Noun | Who? / What? | Ask first in Q&A flow |
| V | Verb | What is being said about the subject? | Ask second |
| Adv | Adverb | How? / When? / Where? | Go to the verb (or adjective for intensifiers) |
| Adj | Adjective | What kind? / Which one? / How many? | Go to the subject noun |
| A | Article Adjective | *(memorize)* a, an, the | Noun markers |

Also include: Pattern 1 (SN V / P1), four sentence kinds (D, Imp, Int, E), 4-step classify checklist, Mover/Shaker rule (brief), slash-before-verb rule.

Source artwork: adapt from `Core_Five_English_Grammar_Guide.png` and `Mastering_the_Sentence_Blueprint.png` — not copy NotebookLM branding.

---

## 11. Proposed Visual Reference Pages (Packet)

| Page | Asset | Placement |
|------|-------|-------------|
| The Sentence Blueprint (Core Five) | `Core_Five_English_Grammar_Guide.png` | After L1 Learn or as reference insert |
| Chapter 2 at-a-glance | `Mastering_the_Sentence_Blueprint.png` | Teacher edition intro or optional student bookmark |
| Pattern 1 diagram | Redraw from slides (avoid NotebookLM watermark) | L1 Practice Together |
| Mover/Shaker diagram | From `The_Grammar_Blueprint-3` slide 3–4 | L3 opening |
| Four Kinds chart | From `Sentence_Construction_Blueprint` slide 6 | L7 Learn |
| Color key | SN=blue, V=red, Adj=yellow, Adv=green/purple, A=yellow/teal | Footer of reference spread |

---

## 12. Slideshow QA Result

**11 Chapter 2 PPTX files found** (9 unique decks + 2 adverb duplicates). All image-only. Full visual QA deferred to `work/chapter-02/slideshow-audit.md` (create at build phase). See `slide-to-packet-map.md` for deck-to-lesson mapping.

---

## 13. Files to Create After Approval

| # | File |
|---|------|
| 1 | `packets/student/chapter-02/chapter-02-shurley-packet.docx` |
| 2 | `packets/teacher-keys/chapter-02/chapter-02-shurley-packet-teacher-edition.docx` |
| 3 | `packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review.docx` |
| 4 | `packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review-key.docx` |
| 5 | `scripts/generate_chapter_02.py` |
| 6 | `scripts/validate_chapter_02.py` |
| 7 | `work/chapter-02/phase-3-build-report.md` |
| 8 | `work/chapter-02/slideshow-audit.md` |
| 9 | `work/chapter-02/pagination-audit.md` |
| 10 | `work/chapter-02/page-pair-audit.md` |

---

## 14. Teacher Approval Required

1. Confirm T2/T3 fill-in answers for Lessons 1–2, 5, 7 (see `teacher-approval-checklist-proposed.md`)
2. Confirm sentence type labels **D / Imp / Int / E** (update prior I → Imp proposal)
3. Classification marking conventions (multi-adv, quantifiers, fewer-than-pattern slots)
4. Lesson 9 rule-number key
5. Student title, reference handling, In-Class Review sentence policy
6. Approve T3 slide content for print adaptation (NotebookLM visuals)
7. Supply **Noun Checks** oral script if required in packet teacher notes

---

**STOP — Awaiting teacher approval before generating Chapter 2 DOCX files.**
