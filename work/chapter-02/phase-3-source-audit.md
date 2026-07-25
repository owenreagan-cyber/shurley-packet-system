# Phase 3 Source Audit — Chapter 2 Shurley Packet

**Date:** 2026-07-24  
**Branch:** `phase-3/chapter-02-gold-standard`  
**Status:** Source audit complete — **awaiting teacher approval before DOCX generation**

---

## Repository Confirmation

| Check | Result |
|-------|--------|
| Working directory | `/Users/owen/Projects/shurley-packet-system` |
| Branch | `phase-3/chapter-02-gold-standard` |
| Git status | Only untracked Chapter 2 source-audit file present before commit |

---

## 1. Every Chapter 2 Source File Found

| File | Status | Role |
|------|--------|------|
| `source-materials/chapter-02/Chapter 2 Guided Notes.docx` | **Found** | Sole authoritative Chapter 2 source (119 non-empty paragraphs, 12 inline drawing boxes, 1 embedded image) |
| `source-materials/reference/shurley-capitalization-punctuation-reference.pdf` | Found (Chapter 1 protected reference) | Reusable for Lesson 9 rule-number exercise only — do not re-embed unless instructionally required |
| `source-materials/reference/shurley-capitalization-punctuation-reference-transcription.md` | Found | Rule-number lookup for Lesson 9 teacher key |
| `source-materials/reference/shurley-capitalization-punctuation-reference-page-1.png` | Found | Available if reference re-embed is approved |
| `source-materials/reference/shurley-capitalization-punctuation-reference-page-2-oriented.png` | Found | Available if reference re-embed is approved |

### Repository Search Results (Additional Chapter 2 Materials)

| Search | Result |
|--------|--------|
| `source-materials/chapter-02/` | Only `Chapter 2 Guided Notes.docx` |
| `**/chapter-02/**` | No packet outputs, planning docs, or slideshows yet |
| `**/*Chapter*2*` / `**/*chapter*02*` | No additional files |
| `**/*.pptx` | **No Chapter 2 slideshow exists** |
| `archive/` | Only `Ch. 1 Study Guide - Study Sheet.pdf` — no Chapter 2 archive |
| `source-materials/chapter-01/planning/` | Chapter 1 only — no Chapter 2 planning equivalent |

### Gold-Standard Model Files Inspected (Chapter 1)

| File | Role |
|------|------|
| `scripts/generate_chapter_01.py` | Generation pattern, layout helpers, teacher notes structure |
| `scripts/validate_chapter_01.py` | Validation pattern (parity, Study Guide check, protected PDF hash) |
| `scripts/render_qa.py` | LibreOffice render QA workflow |
| `work/chapter-01/phase-2-build-report.md` | Production baseline (27/27/1/1 pages) |
| `work/chapter-01/page-pair-audit.md` | Student/teacher parity method |
| `work/chapter-01/pagination-audit.md` | Overflow correction patterns |
| `docs/standards/*.md` | Naming, content, design, student-resource QA, slideshow QA |

---

## 2. Lesson-by-Lesson Topic Inventory

Chapter 2 Guided Notes contains **9 lessons**. All content below is traced to `Chapter 2 Guided Notes.docx` unless marked **[GAP]**.

### Lesson 1 — Nouns, Verbs, and SN–V Classification

| Topic | Source Detail |
|-------|---------------|
| What nouns name | Four numbered blanks (1–4) — answers **[GAP]** |
| Subject questions | Prompt present; source shows only `2.` — list appears incomplete **[GAP]** |
| Verbs | Fill-in: action verb vs linking verb definitions **[GAP]** |
| Classification pattern | `SN` + `V` |
| Sample (S.) | Ships sailed. |
| Practice items | 1. Plane flew. / 2. Ladybugs crawled. / 3. Boys raced. |
| Apply | Write your own sentence using SN–V pattern |

### Lesson 2 — Adverbs and SN–V–Adv–Adv Classification

| Topic | Source Detail |
|-------|---------------|
| Adverb questions | Three blanks **[GAP]** |
| What adverbs modify | Three blanks **[GAP]** |
| Abbreviation | Blank for adverb label (pattern elsewhere uses `Adv`) |
| Classification pattern | `SN` + `V` + `Adv` + `Adv` |
| Sample (S.) | Ships sailed slowly away today. |
| Practice items | 1. Planes flew. / 2. Planes flew quickly away today. / 3. Spiders crawled around very quickly. |
| Apply | Write your own sentence using SN–V–Adv–Adv pattern |

### Lesson 3 — Adverb Classification (Continued)

| Topic | Source Detail |
|-------|---------------|
| Classification only | No new Learn content in source |
| Practice items | 1. Bees buzzed angrily around today. / 2. Rabbits hopped around everywhere. / 3. Anthony listened very carefully yesterday. |
| Apply | Write your own sentence using SN–V–Adv–Adv pattern |

### Lesson 4 — Adjectives and Adj–Adj–SN–V–Adv–Adv Classification

| Topic | Source Detail |
|-------|---------------|
| Adjective definition | **Confirmed:** "An adjective describes a noun or a pronoun." |
| Adjective questions | **Confirmed prompts:** What ___? / Which ___? / How ___? (answers blank) |
| Abbreviation | Blank for adjective label (pattern elsewhere uses `Adj`) |
| Classification pattern | `Adj` + `Adj` + `SN` + `V` + `Adv` + `Adv` |
| Sample (S.) | Those five cargo ships sailed slowly away today. |
| Practice items | 1. That owl flew silently. / 2. That large white owl flew silently overhead tonight. / 3. Several little red ladybugs crawled everywhere yesterday. |
| Apply | Write your own sentence using full pattern |

### Lesson 5 — Article Adjectives, a/an, and A–Adj–Adj–SN–V–Adv–Adv Classification

| Topic | Source Detail |
|-------|---------------|
| Article adjectives | Three blanks **[GAP]** (expected: a, an, the — not confirmed in source text) |
| Abbreviation | Blank **[GAP]** (pattern elsewhere uses `A`) |
| Also known as | Two blanks **[GAP]** |
| a/an practice | **Confirmed sentences:** a tall tree; an unhappy baby; a flying owl; an owl; Did you find an oily cloth…; Would you like a fresh peach?; We saw a large animal…; We saw an anteater…; We saw a movie / an exciting movie |
| Classification pattern | `A` + `Adj` + `Adj` + `SN` + `V` + `Adv` + `Adv` |
| Sample (S.) | The five cargo ships sailed slowly away. |
| Practice items | 1. The girls giggled loudly. / 2. The four happy girls giggled loudly today. / 3. A huge whale swam very slowly away. |
| Apply | Write your own sentence using full pattern |

### Lesson 6 — Full-Pattern Classification Practice

| Topic | Source Detail |
|-------|---------------|
| Classification only | No new Learn content in source |
| Practice items | 1. The nice young doctor spoke very kindly today. / 2. A little yellow duck waddled slowly away. / 3. An enormous black bug flew around today. |

### Lesson 7 — Vocabulary, Sentence Types, and Extended Classification

| Topic | Source Detail |
|-------|---------------|
| Vocabulary | **Blank template** (word, definition, synonym, antonym, sentence, drawing box) |
| Source analogy | **Confirmed:** `soothing : smoothing :: flying : trying` |
| Analogy relationship | Circle: synonym / antonym / rhyming / part-to-whole → **rhyming** |
| Sentence types | **Confirmed definitions:** Declarative (statement), Imperative (command), Interrogative (question), Exclamatory (strong feeling) |
| Sentence type labels | Four blanks for abbreviations **[GAP]** |
| Classification | S. The two pirate ships appeared quite suddenly! / 1. The music played softly. / 2. The very soothing music played softly tonight. / 3. Several urgent messages arrived very early today. |
| Parts of Speech | Four blanks **[GAP]** |

### Lesson 8 — Vocabulary and Sentence-Type Classification

| Topic | Source Detail |
|-------|---------------|
| Vocabulary | **Blank template** (same fields as Lesson 7) |
| Source analogy | **Confirmed:** `urgent : important :: answer : reply` → **synonym** |
| Classification | 1. A young reporter glanced curiously around. / 2. The stormy winter sky darkened suddenly! / 3. An extremely frightened girl screamed very loudly! |

### Lesson 9 — Full Classification and Capitalization/Punctuation Rules

| Topic | Source Detail |
|-------|---------------|
| Classification | 1. Two beautiful butterflies flew slowly away. / 2. An old teapot whistled very loudly today. / 3. Several angry bees circled around nearby! |
| Cap/punct application | **Confirmed heading:** "Using Capitalization and Punctuation Rules" |
| Instruction | Write rule numbers for each correction in bold |
| Sentence | `No, Alex did not go home with John during carpool on Friday.` |
| Bold corrections (extracted from source formatting) | **N**, **,**, **A**, **J**, **F**, **.** |

---

## 3. Confirmed Vocabulary

| Item | Status |
|------|--------|
| Assigned vocabulary words | **None confirmed** — Lessons 7 and 8 use blank templates only |
| Vocabulary fields in source | Word, Definition, Synonym, Antonym, Sentence, Drawing box |
| Source analogy examples (not vocabulary assignments) | L7: `soothing : smoothing :: flying : trying` / L8: `urgent : important :: answer : reply` |

**Inclusion rule:** Do not pre-fill vocabulary words or definitions. Teacher assigns vocabulary per Chapter 1 precedent and `packet-content-rules.md`.

---

## 4. Confirmed Sentence-Classification Content

### Pattern Progression (Confirmed from Source Labels)

| Lesson | Pattern |
|--------|---------|
| 1 | SN – V |
| 2–3 | SN – V – Adv – Adv |
| 4 | Adj – Adj – SN – V – Adv – Adv |
| 5–9 | A – Adj – Adj – SN – V – Adv – Adv |

### Classification Item Count

| Lesson | Sample (S.) | Numbered Items | Write-Your-Own |
|--------|-------------|----------------|----------------|
| 1 | 1 | 3 | 1 |
| 2 | 1 | 3 | 1 |
| 3 | 0 | 3 | 1 |
| 4 | 1 | 3 | 1 |
| 5 | 1 | 3 | 1 |
| 6 | 0 | 3 | 0 |
| 7 | 1 | 3 | 0 |
| 8 | 0 | 3 | 0 |
| 9 | 0 | 3 | 0 |

**Total source classification sentences:** 28 (including samples)

### Sentence Types (Lessons 7–9)

| Type | Definition (Confirmed) | Label Abbreviation |
|------|------------------------|-------------------|
| Declarative | Makes a statement | **[GAP]** |
| Imperative | Gives a command | **[GAP]** |
| Interrogative | Asks a question | **[GAP]** |
| Exclamatory | Expresses strong feeling | **[GAP]** |

Sentence type can be inferred from end punctuation on practice sentences (period, exclamation mark) but official Shurley label abbreviations are not in the source text.

### Chapter 2 Classification Standard (Production Requirement)

Each classification item in the generated packet must include, where appropriate:

1. **Sentence** — exact wording from source
2. **Classification Workspace** — large bordered area for fourth-grade marking/labeling
3. **Pattern** — lesson pattern string (e.g., `A Adj Adj SN V Adv Adv`)
4. **Sentence Type** — from Lesson 7 onward (Declarative / Imperative / Interrogative / Exclamatory)
5. **Skill or Rule Focus** — lesson skill being practiced
6. **Memory Check** — 1–3 retrieval questions at lesson end

Lessons 1–6: Sentence Type field omitted or marked N/A until Lesson 7 introduces the concept.

---

## 5. Confirmed Jingles, Rules, Examples, Editing, Analogies, and Writing Work

### Jingles

| Jingle | Status |
|--------|--------|
| Noun Jingle | **Not in source** — do not invent |
| Verb Jingle | **Not in source** — do not invent |
| Adverb Jingle | **Not in source** — do not invent |
| Adjective Jingle | **Not in source** — do not invent |
| Sentence Jingle | **Not in source** — do not reproduce (Chapter 1 precedent) |

Source may expect oral classroom jingles; Guided Notes contain fill-in blanks only.

### Rules and Definitions (Confirmed Wording)

| Rule/Definition | Source |
|-----------------|--------|
| Adjective definition | "An adjective describes a noun or a pronoun." |
| Adjective questions (prompts) | What ___? / Which ___? / How ___? |
| Declarative sentence | "makes a statement" |
| Imperative sentence | "gives a command" |
| Interrogative sentence | "asks a question" |
| Exclamatory sentence | "expresses strong feeling" |
| Capitalization/punctuation | Use official Reference 7 and Reference 9 rule numbers (protected transcription) |

### Examples (Confirmed Sentences — Do Not Alter)

All 28 classification sentences listed in Section 4, plus all a/an practice sentences in Lesson 5, plus Lesson 9 cap/punct sentence.

### Editing Work

| Item | Detail |
|------|--------|
| Lesson 9 cap/punct | Identify rule numbers for bold corrections in: `No, Alex did not go home with John during carpool on Friday.` |
| Bold correction points | N, comma, A, J, F, period (from source bold formatting) |
| Original uncorrected sentence | **Not in source** — only corrected form with bold marks present |

### Analogies (Confirmed)

| Lesson | Analogy | Relationship |
|--------|---------|--------------|
| 7 | soothing : smoothing :: flying : trying | Rhyming |
| 8 | urgent : important :: answer : reply | Synonym |

### Writing Work

| Type | Lessons | Count |
|------|---------|-------|
| Write your own sentence (pattern) | 1–5 | 5 prompts |
| Vocabulary sentence lines | 7–8 | 2 blank templates |
| Drawing boxes | 7–8 | 2 (inline shapes in source) |

---

## 6. Existing Question Types

| Question Type | Lessons | Notes |
|---------------|---------|-------|
| Fill-in-the-blank (definitions, questions, abbreviations) | 1–2, 4–5, 7 | Many answers missing from source |
| Sentence classification (S. + numbered) | 1–9 | Core Chapter 2 activity |
| Pattern labeling | 1–5 | SN/V/Adv/Adj/A row labels in source |
| a/an article selection | 5 | 9 prompts confirmed |
| Vocabulary template | 7–8 | Blank — teacher-assigned |
| Analogy relationship selection | 7–8 | Circle one of four types |
| Parts of speech listing | 7 | Four blanks |
| Cap/punct rule-number identification | 9 | Map bold corrections to rule numbers |
| Write-your-own sentence | 1–5 | One per lesson |
| Drawing box | 7–8 | Memory picture for vocabulary |

**Not present in source:** multiple choice, matching columns, word banks, synonym/antonym circling (Chapter 1 skills), separate editing rewrite passages (Chapter 1 style).

---

## 7. Missing or Uncertain Source Content

| Gap | Impact | Proposed Handling |
|-----|--------|-------------------|
| Noun naming categories (4 answers) | Lesson 1 Learn incomplete | **[STOP]** — Request teacher input (person, place, thing, idea?) |
| Subject questions (complete list) | Lesson 1 Learn incomplete; source shows only `2.` | **[STOP]** — Request teacher input or classroom Shurley materials |
| Action vs linking verb fill-ins | Lesson 1 Learn incomplete | **[STOP]** — Request teacher input |
| Adverb questions (3 answers) | Lesson 2 Learn incomplete | **[STOP]** — Request teacher input |
| What adverbs modify (3 answers) | Lesson 2 Learn incomplete | **[STOP]** — Request teacher input |
| Adverb abbreviation answer | Blank in source | Likely `Adv` from pattern labels — confirm with teacher |
| Adjective abbreviation answer | Blank in source | Likely `Adj` from pattern labels — confirm with teacher |
| Article adjectives list | Three blanks | Likely a, an, the — confirm with teacher |
| Article abbreviation | Blank | Likely `A` from pattern — confirm with teacher |
| "Also known as" terms | Two blanks | Possibly "determiners" / "noun markers" — **[STOP]** |
| Sentence type abbreviations | Four blanks | Likely D, I, Int, E — **[STOP]** |
| Parts of speech four words | Four blanks | Likely Noun, Verb, Adjective, Adverb — **[STOP]** |
| Shurley jingle lyrics | Not in source | Reference hint only; do not reproduce |
| Vocabulary word list | Templates blank | Teacher-assigned per content rules |
| Lesson 9 uncorrected sentence | Not in source | Use bold-marked corrected sentence; teacher key maps rules to bold marks |
| Lesson 9 rule-number answer key | Requires rule-to-correction mapping | Derive from protected transcription after teacher confirms abbreviations |
| Classification marking conventions | Source shows pattern rows, not full marked answers | Teacher edition must show SN/Adj/Adv labels per word — derivable from sentences but needs Shurley convention confirmation |
| README.md | Empty | Out of scope |
| Chapter 2 planning doc | None | Not required — all 9 lessons in Guided Notes |
| Chapter 2 slideshow (PPTX) | None found | Report clearly; do not invent |

---

## 8. Content That Must Not Be Invented

- Shurley jingle lyrics (Noun, Verb, Adverb, Adjective, Sentence)
- Noun/adverb/adjective question answers not confirmed in source
- Vocabulary words or definitions (keep blank templates)
- Sentence type label abbreviations without teacher confirmation
- Parts of speech list without teacher confirmation
- Additional classification sentences beyond the 28 in source
- New analogy examples beyond the two source examples
- Paraphrased capitalization/punctuation rules
- Re-numbered or altered rule wording from protected reference
- "Study Guide" or test-prep language
- Chapter 2 slideshow content
- Textbook page references or rule systems not in official reference

New practice items may be created **only** when they exercise a confirmed skill — Chapter 2 source is largely fixed-sentence classification; minimal new item creation expected.

---

## 9. Proposed Packet Page Order

**Student-facing title:** Chapter 2 Shurley Language Journal (workbook continuity with Chapter 1 Shurley Packet identity)

Target: **22–26 student pages** (estimate; LibreOffice render will finalize). Teacher edition mirrors exactly.

| Page(s) | Section | Primary Source |
|---------|---------|----------------|
| 1 | Cover — Chapter 2 Shurley Language Journal, name/date/teacher, drawing prompt | New (matches Ch. 1 cover pattern) |
| 2 | Lesson 1 — Learn: nouns, subject questions, verbs; Remember box | Guided Notes L1 **[pending gap fills]** |
| 3 | Lesson 1 — Practice Together: S. + items 1–3 classification workspaces | Guided Notes L1 |
| 4 | Lesson 1 — Apply: write-your-own SN–V; Memory Check; Teacher Check | Guided Notes L1 |
| 5 | Lesson 2 — Learn: adverb questions, modifies, abbreviation; Remember box | Guided Notes L2 **[pending gap fills]** |
| 6 | Lesson 2 — Practice Together: S. + items 1–3 classification | Guided Notes L2 |
| 7 | Lesson 2 — Apply: write-your-own; Memory Check; Teacher Check | Guided Notes L2 |
| 8 | Lesson 3 — Practice Together/Independently: items 1–3 classification | Guided Notes L3 |
| 9 | Lesson 3 — Apply: write-your-own; Memory Check; Teacher Check | Guided Notes L3 |
| 10 | Lesson 4 — Learn: adjective definition and questions; Remember box | Guided Notes L4 |
| 11 | Lesson 4 — Practice Together: S. + items 1–3 classification | Guided Notes L4 |
| 12 | Lesson 4 — Apply: write-your-own; Memory Check; Teacher Check | Guided Notes L4 |
| 13 | Lesson 5 — Learn: article adjectives, a/an rules; Practice: a/an blanks | Guided Notes L5 **[pending gap fills]** |
| 14 | Lesson 5 — Practice Together: S. + items 1–3 classification | Guided Notes L5 |
| 15 | Lesson 5 — Apply: write-your-own; Memory Check; Teacher Check | Guided Notes L5 |
| 16 | Lesson 6 — Practice Together/Independently: items 1–3 classification | Guided Notes L6 |
| 17 | Lesson 6 — Memory Check; Teacher Check | Guided Notes L6 |
| 18 | Lesson 7 — Learn: sentence types; Parts of Speech; Remember box | Guided Notes L7 **[pending gap fills]** |
| 19 | Lesson 7 — Apply: vocabulary template + analogy | Guided Notes L7 |
| 20 | Lesson 7 — Practice Together: S. + items 1–3 (with sentence type) | Guided Notes L7 |
| 21 | Lesson 7 — Memory Check; Teacher Check | Guided Notes L7 |
| 22 | Lesson 8 — Apply: vocabulary template + analogy | Guided Notes L8 |
| 23 | Lesson 8 — Practice Together: items 1–3 classification + sentence type | Guided Notes L8 |
| 24 | Lesson 8 — Memory Check; Teacher Check | Guided Notes L8 |
| 25 | Lesson 9 — Practice Together: items 1–3 classification + sentence type | Guided Notes L9 |
| 26 | Lesson 9 — Apply: cap/punct rule numbers; Memory Check; Teacher Check | Guided Notes L9 |

**Pagination notes:**

- Lessons 3 and 6 may share a page tail if classification workspaces fit with clear separation (source is classification-heavy but shorter on Learn content).
- Lesson 5 a/an practice may require a full page due to 9 items and handwriting spacing rules.
- **No re-embedded Capitalization and Punctuation Reference** — Lesson 9 directs students to use the reference from their Chapter 1 packet (or classroom copy). Re-embed only if teacher requests.
- Final page count subject to overflow QA; estimate **24 ± 2 pages**.

---

## 10. Proposed Teacher Edition Structure

Mirror student packet **page for page** (same count, order, question numbering, workspace footprint).

| Element | Approach |
|---------|----------|
| Classification answers | Bold blue word-by-word labels (SN, V, Adv, Adj, A) beneath each workspace |
| Sentence type answers | Bold blue abbreviations from Lesson 7 onward (after teacher confirms labels) |
| Fill-in Learn blanks | Model answers in bold blue; `[teacher-assigned]` where gaps unresolved |
| Vocabulary | "Teacher-assigned — answers will vary" |
| Analogies | L7: Rhyming / L8: Synonym |
| a/an practice | Full answer key for all 9 items |
| Lesson 9 rule numbers | Map each bold correction to Reference 7/9 rule number |
| Teacher notes | Oral prompts for jingles (reference classroom delivery, no lyrics), timing, common classification errors |
| Misconceptions | e.g., confusing adjective and adverb; article vs adjective |
| Procedures | None confirmed in source (unlike Ch. 1 ball-passing / letter storage) |

Teacher notes appear in fixed reserved areas **below** student workspaces — never collapsing handwriting space.

---

## 11. Proposed In-Class Chapter Review Structure

**Separate files** (not embedded in main packet), max **2 physical pages**, printable front-to-back.

### Page 1 (Proposed)

| Part | Content |
|------|---------|
| A | Pattern recall — label SN, V, Adv, Adj, A |
| B | One SN–V classification item (new sentence exercising confirmed skill — **only if teacher approves**) |
| C | One full-pattern classification item from confirmed sentence bank |
| D | Sentence type — identify four types / match type to definition |

### Page 2 (Proposed)

| Part | Content |
|------|---------|
| E | a/an — 3–4 items from Lesson 5 confirmed sentences |
| F | Analogy — one relationship question using confirmed examples as models |
| G | Vocabulary — one teacher-assigned recall prompt |
| H | Cap/punct — one rule-number or rewrite item referencing protected reference |
| I | Application — write one sentence using full A–Adj–Adj–SN–V–Adv–Adv pattern |

**Constraints:** No "Study Guide" language. Same question order in key file. Only confirmed Chapter 2 skills. Generous spacing, 12–14 pt body.

---

## 12. Estimated Physical Page Count

| Document | Estimated Pages |
|----------|-----------------|
| Student Shurley Language Journal | 24 (range 22–26 after QA) |
| Teacher Edition | 24 (must match student exactly) |
| In-Class Chapter Review | 2 (target; may fit 1 if spacing allows) |
| In-Class Chapter Review Key | 2 (must match review) |

Chapter 1 baseline for comparison: 27 / 27 / 1 / 1.

Chapter 2 has more lessons (9 vs 6) but less multi-page writing work (no letter unit), so total length may be comparable or slightly shorter despite classification workspace requirements.

---

## 13. Exact Files to Create (After Approval)

| # | File |
|---|------|
| 1 | `packets/student/chapter-02/chapter-02-shurley-packet.docx` |
| 2 | `packets/teacher-keys/chapter-02/chapter-02-shurley-packet-teacher-edition.docx` |
| 3 | `packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review.docx` |
| 4 | `packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review-key.docx` |
| 5 | `scripts/generate_chapter_02.py` |
| 6 | `scripts/validate_chapter_02.py` |
| 7 | `work/chapter-02/phase-3-build-report.md` |
| 8 | `work/chapter-02/pagination-audit.md` |
| 9 | `work/chapter-02/page-pair-audit.md` |

**Optional (shared refactor):**

| File | Condition |
|------|-----------|
| `scripts/shurley_packet_common.py` | Only if extracting helpers from `generate_chapter_01.py` reduces duplication without Chapter 1 regression |

**Slideshow audit (conditional):**

| File | Condition |
|------|-----------|
| `work/chapter-02/slideshow-audit.md` | Only if a Chapter 2 PPTX appears — **none found now** |

---

## 14. Risks Carried Forward from Chapter 1

| Risk | Chapter 1 Precedent | Chapter 2 Mitigation |
|------|---------------------|----------------------|
| Physical page overflow | Lesson 1 orphan TEACHER CHECK; Lesson 2 orphan note | Pre-size classification workspaces; test early with LibreOffice render |
| Student/teacher page drift | Prior build 25 vs 23 pages | Mandatory parity check in `validate_chapter_02.py` |
| Cramped layout | Lesson 4 analogy table overflow | Use large classification boxes, 14 pt examples, no narrow columns |
| Protected reference handling | PDF orientation, image embed | Do not re-embed unless approved; reference Ch. 1 packet |
| Shared code regression | N/A for Ch. 2 v1 | If `shurley_packet_common.py` created, rerun Ch. 1 gen + validate (27/27/1/1) |
| Vocabulary pre-fill | Archive words must not auto-fill | Keep blank templates in Lessons 7–8 |
| Jingle/reference content | Do not reproduce lyrics | Hint-only references in Learn sections |
| Visual QA workload | 27 pages × 2 editions | Budget time for 24+ pages × 2 + review PNG inspection |
| Incomplete source gaps | Ch. 1 had missing reference sheet | Ch. 2 has **more numerous fill-in gaps** — higher invention risk |
| Classification workspace size | New requirement for Ch. 2 | Must not reduce to single blank line — largest layout risk |
| "Study Guide" prohibition | Validated in Ch. 1 | Same check in `validate_chapter_02.py` |
| Temporary QA files | validate render dir under work/ | Clean up tracked temp files after validation |

---

## Slideshow QA Result

**No Chapter 2 PPTX file exists in the repository.** Slideshow audit deferred. Per `docs/standards/slideshow-qa-rules.md`, record result in build report when PPTX is supplied.

---

## Teacher Approval Required Before Generation

The following must be confirmed or supplied before DOCX generation:

1. **Fill-in answers** for Lessons 1–2, 5, 7 (noun categories, subject/adverb questions, verb types, article adjectives, sentence type labels, parts of speech)
2. **Sentence classification marking conventions** (exact label format, multi-adjective/adverb handling)
3. **Lesson 9 rule-number key** (which Reference 7/9 rule applies to each bold correction)
4. **Student-facing title** — approve "Chapter 2 Shurley Language Journal" vs "Chapter 2 Shurley Packet"
5. **Reference handling** — refer back to Chapter 1 reference vs re-embed in Chapter 2 packet
6. **In-Class Review** — approve use of any new practice sentences (vs source-only sentences)

---

## Validation Commands (Post-Generation)

```bash
python3 scripts/generate_chapter_02.py
python3 scripts/validate_chapter_02.py
```

If shared helpers are introduced:

```bash
python3 scripts/generate_chapter_01.py
python3 scripts/validate_chapter_01.py
```

---

**STOP — Awaiting teacher approval before generating Chapter 2 DOCX files.**
