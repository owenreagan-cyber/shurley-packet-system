# Chapter 2 Packet Generation Specification

**Status:** LOCKED production specification — governs all Chapter 2 DOCX generation  
**Date:** 2026-07-26  
**Branch:** `phase-3/chapter-02-gold-standard`  
**Version:** 1.0  
**Supersedes:** Informal estimates in `phase-3-source-audit.md` where this document is more specific.

**Authoritative inputs:**

| Document | Role |
|----------|------|
| `work/chapter-02/teacher-manual-alignment.md` | Tier 1 alignment |
| `work/chapter-02/lesson-script-map.md` | Q&A scripts |
| `work/chapter-02/classroom-practice-map.md` | CP boundaries |
| `work/chapter-02/source-conflicts.md` | Conflict resolutions |
| `work/chapter-02/instructional-map.md` | Lesson arc |
| `work/chapter-02/slide-to-packet-map.md` | Slide usage |
| `work/chapter-02/visual-language-guide.md` | Print visuals |
| `work/chapter-02/final-decisions.md` | Locked teacher decisions v1.0 |
| `work/chapter-02/partial-pattern-decision.md` | U-03 partial-pattern display lock |
| `source-materials/chapter-02/Chapter 2 Guided Notes.docx` | Student sentences |
| `docs/standards/*.md` | Project-wide rules |

**Outputs governed (not yet built):**

- `packets/student/chapter-02/chapter-02-shurley-packet.docx`
- `packets/teacher-keys/chapter-02/chapter-02-shurley-packet-teacher-edition.docx`
- `packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review.docx`
- `packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review-key.docx`
- `scripts/generate_chapter_02.py`
- `scripts/validate_chapter_02.py`

---

# 1. Source Authority

## Hierarchy (highest → lowest)

```
Teacher Manual (Tier 1)
        ↓
Guided Notes.docx (Tier 2)
        ↓
Blueprint slide resources (Tier 3)
        ↓
Student Packet (generated)
        ↓
Teacher Edition (generated — keys + notes only)
```

## Rules

1. **Teacher Manual wins** on terminology, Q&A scripts, classification keys, Skill Check wording, label abbreviations (**Imp**, not I), and procedure order.
2. **Guided Notes win** on student-facing practice sentences (all 28 classification items + write-your-own prompts L1–5). No substitution from Classroom Practice, Checkup, or Test sentences without written teacher approval.
3. **Slides win** only for visual layout adaptation and oral-sequence hints. Slide-only sentences, NotebookLM branding, and teacher-created CP preview text **must not** enter the student packet.
4. **Generated content must never override Teacher Manual wording** for definitions, questions, or oral scripts. Paraphrase is forbidden for Shurley instructional language.
5. **Conflicts** are resolved per `source-conflicts.md`. Open conflicts block generation until teacher sign-off (see §10).

## Prohibited sources for packet body text

- Classroom Practice workbook sentences (CP4–CP12)
- Chapter 2 Checkup 11 / Chapter Test sentences
- Slide Classroom Practice preview sentences
- Invented jingle lyrics, vocabulary words, or analogy pairs beyond Guided Notes
- Paraphrased capitalization/punctuation rules

---

# 2. Student Resource Standards

All Chapter 2 student materials comply with `docs/standards/packet-design-rules.md` and these Chapter 2 locks:

| Requirement | Specification |
|-------------|---------------|
| Page size | 8.5 × 11 in, portrait |
| Margins | 0.75 in all sides (0.6 in for In-Class Chapter Review only) |
| Readability | Fourth-grade level; short sentences; no academic jargon without TM definition |
| Handwriting space | Minimum **4** blank 72-char lines per classification item; multi-line fill-ins |
| White space | Purposeful — separate Learn, practice blocks, and checks; no decorative filler |
| Tables | No cramped tables; classification uses **fixed-width layout** (see §4), not dense grids |
| Classification examples | Full word-size labels; never shrink specimens to fit |
| Blank pages | **None** unless required for front/back imposition; no pad pages |
| In-Class Chapter Review | **Maximum 2 pages** student; **maximum 2 pages** key |
| Printing | Design for **front/back** duplex where page pairs align (student ↔ teacher) |
| Product name | **Chapter 2 Shurley Packet** — never "Study Guide" |
| Font | Calibri; body 13 pt; labels legible at print |

---

# 3. Shurley Classification Engine Rules

The generator implements **two distinct orders**. Confusing them is a **validation failure**.

## 3.1 Discovery Order (Question and Answer Flow)

Used orally and in teacher scripts to **find** each word's job. This is **not** the visual left-to-right label order on the classified line.

### Step 1 — Subject Noun (SN)

**Questions:** Who? / What?  
**Rule:** Use **Who?** only when the subject is a person (TM 43a). Otherwise **What?**

### Step 2 — Verb (V)

**Question:** What is being said about the subject?  
*(Substitute the subject word: "What is being said about ships?")*

### Step 3 — Modifiers after the verb (L2+)

Go to the **verb** first. Classify adverbs in **sentence order** as they appear after the verb.

- **How?** → Adv  
- **When?** → Adv  
- **Where?** → Adv  
- **How [adj/adv]?** → Adv (intensifier modifying adjacent Adj or Adv)

**Adverb order rule (TM 48):** Default = order of appearance after verb. When one adverb modifies another, ask the modified adverb's question second (e.g., *Crawled where? around* → *Crawled how? quickly* → *How quickly? very*).

### Step 4 — Adjectives (L4+)

Return to the **subject noun**. Ask:

- What kind? → Adj  
- Which one? → Adj  
- How many? → Adj  

### Step 5 — Article adjective (L5+)

Identify **a**, **an**, or **the** by memorization / sight. Label **A**.  
In Q&A, article is named **after** adjectives, immediately before the pattern declaration (TM Refs 20, 66a).

### Step 6 — Pattern declaration (L1+)

Oral: *"Subject Noun, Verb, Pattern 1."*  
Written pattern column: **SN V / P1** (see §4).

### Step 7 — Skill Check (L7+)

After classification, identify end mark → purpose → sentence type → label **D**, **Imp**, **Int**, or **E**.  
Draw **The Divide** (slash directly before verb). See §5.

### Worked discovery example (TM)

**Sentence:** Cat ran very fast.

| Step | Question | Answer | Label |
|------|----------|--------|-------|
| 1 | What ran? | Cat | SN |
| 2 | What is being said about cat? | ran | V |
| 3 | Ran how? | fast | Adv |
| 4 | How fast? | very | Adv |
| 5 | — | Subject Noun, Verb, Pattern 1 | SN V / P1 |
| 6 | (L7+) Period, statement, declarative sentence | | D |

## 3.2 Display Order (Classified Sentence Layout)

The **final classified sentence ALWAYS preserves original English word order**.

**Never reorder words** to match discovery sequence or pattern-zone diagrams.

### Correct vs incorrect

**Correct display** (words left-to-right as spoken):

```
              SN      V      Adv    Adv
SN V  P1     Cat     ran    very    fast.   D
```

**Incorrect display** (reordered to match discovery):

```
              SN      V      Adv    Adv
SN V  P1     Cat     ran    fast    very.   D
```

### Display label columns

Labels appear **directly above** the word they classify, in **sentence word order**:

| Lesson range | Typical display columns (only label words present) |
|--------------|-----------------------------------------------------|
| L1 | SN, V |
| L2–3 | SN, V, Adv… |
| L4 | Adj…, SN, V, Adv… |
| L5–9 | A, Adj…, SN, V, Adv… |

Pattern zone diagrams (A–Adj–SN–V–Adv) show **label types**, not Q&A discovery sequence. Display line follows **spoken sentence order**.

### The Divide (L7+)

Vertical slash **immediately before the verb** in the classified display:

```
The   very   soothing   music   |   played   softly   tonight.   D
 A     Adv      Adj       SN     |    V       Adv              type
```

---

# 4. Classification Formatting Rules

All classification examples in student packet, teacher edition keys, and review materials **must** comply.

## 4.1 Label placement

- Labels sit **directly above** their word, column-aligned.
- Labels are **visually attached** to the word they classify (no floating labels).
- Use **monospaced text, tables, or fixed tab stops** — never proportional-font space padding alone.
- Minimum label row height: clear separation from sentence text below.

## 4.2 Pattern column (P1)

- Left column shows **SN V** on first line, **P1** centered on second line:

```
SN V
P1
```

- Written inline as **SN V  P1** with P1 under SN V (Teacher Manual convention).
- **P1 never appears at the end of the sentence.**
- **P1 never replaces** word labels above tokens.

## 4.3 Sentence type labels (L7+)

Sentence type abbreviation appears **at the END** of the classified line, after the end mark:

| Type | Label |
|------|-------|
| Declarative | **D** |
| Imperative | **Imp** |
| Interrogative | **Int** |
| Exclamatory | **E** |

## 4.4 Correct vs incorrect formatting

**Correct:**

```
              SN        V
SN V  P1     Ships    sailed.
```

**Incorrect:**

```
SN V Ships sailed. P1
```

**Correct (L7+ with type):**

```
              SN      V      Adv    Adv
SN V  P1     Cat     ran     very    fast.   D
```

## 4.5 Partial-pattern sentences (LOCKED — U-03)

**Rule:** Partial-pattern sentences display **only** the labels for words that actually exist in the sentence.

The classification engine creates labels from **actual classified tokens**, not from the expected maximum Chapter 2 pattern (`A Adj Adj SN V Adv Adv`).

### Generator requirements (mandatory)

| Requirement | Rule |
|-------------|------|
| Word order | Preserve original sentence word order |
| Missing modifiers | Never add missing modifiers |
| Pattern forcing | Never force every sentence into the largest Chapter 2 pattern |
| Empty labels | Never display empty label columns |
| Placeholders | Never add placeholder words |
| P1 | Keep **P1** below **SN V** in the left pattern column |
| Sentence type | Keep **D / Imp / Int / E** at the end (L7+) |

### Locked examples

**Example 1 — SN V only**

```
             SN      V

SN V  P1    Cats    ran.
```

**Example 2 — SN V Adv**

```
             SN      V      Adv

SN V  P1    Cats    ran    quickly.
```

**Example 3 — A Adj SN V Adv**

```
             A       Adj     SN      V      Adv

SN V  P1    The     small   cat     ran    quickly.
```

**Example 4 — Two adverbs (discovery ≠ display order)**

Sentence: *The cat ran very fast.*

Discovery: cat → SN; ran → V; fast → Adv; very → Adv.

```
             A       SN      V      Adv    Adv

SN V  P1    The     cat     ran    very   fast.
```

Append **D / Imp / Int / E** after the end mark on L7+ items (examples above omit type when not applicable).

### Implementation

`generate_chapter_02.py` builds the label row from the classified token list only — **no padding** to lesson maximum pattern width. See `work/chapter-02/partial-pattern-decision.md` for full rationale and validation notes.

Teacher edition Procedure notes document Q&A for **actual words only** — no questions for absent modifiers.

## 4.6 Generator implementation note

`generate_chapter_02.py` must render classification via **Word tables** or **Courier New / monospaced paragraphs** with explicit column widths — matching Chapter 1 precedent for fixed layout.

---

# 5. Question and Answer Flow Rules

## 5.1 Exact question wording (locked)

| Label | Questions |
|-------|-----------|
| **SN** | Who? / What? |
| **V** | What is being said about the subject? |
| **Adv** | How? / When? / Where? |
| **Adj** | What kind? / Which one? / How many? |
| **A** | *(memorize)* a, an, the |

**Locked (§11):** Do **not** include *To what extent?* in student materials. Student reference: **How? / When? / Where?** only. Fourth question is teacher enrichment only.

## 5.2 Question order (discovery — locked)

1. SN  
2. V  
3. Adv (all, at verb, in TM adverb order rules)  
4. Adj (at subject noun)  
5. A (if present)  
6. Pattern declaration  
7. Skill Check (L7+)  
8. Noun Check oral follow-up (L8+ teacher modeling; L9 student reminder)

## 5.3 Teacher script expectations

- Read sentence **in unison** before classifying (TM all Q&A keys).
- Recite **both questions and answers** — not labels alone.
- Upbeat rhythm; increase tempo with mastery.
- Four Steps to Classify (Ref 13): Ask → Name → Identify → Label.

## 5.4 Skill Check scripts (L7+ — verbatim from TM Ref 26)

| Type | Script | Label |
|------|--------|-------|
| Declarative | Period, statement, declarative sentence. | D |
| Imperative | Period, command, imperative sentence. | Imp |
| Interrogative | Question mark, question, interrogative sentence. | Int |
| Exclamatory | Exclamation point, strong feeling, exclamatory sentence. | E |

**Follow-up (Ref 27):** *Go back to the verb. Divide the complete subject from the complete predicate.*

## 5.5 Noun Check (L8+ — Ref 29)

> Subject Noun [word], yes, it is a noun.

Student packet: brief **Remember** box in L8 Learn; reminder in L9. Full procedure in teacher edition only.

---

# 6. Sentence Blueprint Requirements

## 6.1 Placement

- **Pages 2–3** of student packet (after cover), unless pagination audit proves 1 page sufficient.
- Same content mirrored in teacher edition (without collapsing student layout).
- Title: **The Sentence Blueprint** (not "Grammar Guide" or "Study Guide").

## 6.2 Required content blocks

| Block | Content (TM/poster locked) |
|-------|----------------------------|
| SN | Subject Noun — **Who? / What?** |
| V | Verb — **What is being said about the subject?** |
| Adv | Adverb — **How? / When? / Where?** |
| Adj | Adjective — **What kind? / Which one? / How many?** |
| A | Article Adjective — **a, an, the** (noun markers) |
| P1 | Pattern 1: **SN V** |
| Sentence types | Declarative **D**, Imperative **Imp**, Interrogative **Int**, Exclamatory **E** (one-line definitions) |
| Four steps | Ask the question → Name the word → Identify its job → Label with abbreviation |
| Mover & Shaker | Move a modifier to the front for variety; comma after moved adverb; **not for classification** |
| The Divide | Slash directly before the verb (L7+) |

## 6.3 Artwork

- Adapt from `Core_Five_English_Grammar_Guide.png` and `Mastering_the_Sentence_Blueprint.png`.
- Strip NotebookLM / third-party branding.
- Color key optional; must pass grayscale print test (`visual-language-guide.md`).

## 6.4 Not on reference page

- Jingle lyrics  
- Vocabulary lists  
- Classroom Practice sentences  
- Full Q&A scripts (those live in teacher edition appendix reference to `lesson-script-map.md`)

---

# 7. Lesson-by-Lesson Packet Rules

Standard footer every lesson: **Memory Check** + **Teacher Check**.

| Lesson | Title (banner) | Objectives (TM) | Learn / Notes | Guided examples | Classification practice | Independent / Apply | Memory Check focus | CP relationship | Slides |
|--------|----------------|-----------------|---------------|-----------------|-------------------------|---------------------|-------------------|-----------------|--------|
| **1** | Nouns, Verbs, Pattern 1 | Jingles 3–4; SN/V; Q&A; P1 | Fill-ins: noun categories, subject Q, verb types; **Remember** Q&A steps | S. Ships sailed. (labeled specimen) | 3 numbered + write-your-own | Apply: write SN V sentence | SN, V, P1, subject Q | **CP4** oral only — Water/Clowns | Operation Pattern 1, Sentence Blueprint |
| **2** | Adverbs | Jingle 5; Adv Q; modify targets | Adv definition, 3 Q, modifies list | S. Ships sailed slowly away today. | 3 numbered + write-your-own | Apply: SN V Adv Adv | Adv questions | **CP5** oral — Cats/Father | Adverb Blueprint |
| **3** | Adverb Practice | Classify; 5 parts; blueprint intro | **Remember** Mover & Shaker (comma rule); 5 parts checklist | — | 3 sentences (Bees/Rabbits/Anthony) | Apply: write-your-own | Mover & Shaker comma | **CP6** blueprint — student-built | Grammar Blueprint-3 |
| **4** | Adjectives | Jingle 6; Adj Q | Adj definition + 3 Q (full wording) | S. Those five cargo ships… | 3 owl/ladybug + write-your-own | Apply: full Adj Adj SN V Adv Adv | Adj questions | **CP7** oral | Building Adjective Blueprints |
| **5** | Article Adjectives | Jingle 7; a/an/the | A, **noun markers** (§11: "Article adjectives are also known as noun markers." — no determiners) | S. The five cargo ships… | **a/an drill (9)** + 3 classify + write-your-own | Apply: full pattern | Articles a, an, the | **CP8** oral | Article Adjective Blueprint |
| **6** | Full-Pattern Fluency | Classify full pattern | — (no new Learn) | Optional one-line pattern **Remember** | 3 sentences (doctor/duck/bug) | — | Full pattern A Adj Adj SN V Adv Adv | **CP9** blueprint | The Sentence Blueprint |
| **7** | Sentence Types | Four kinds; Skill Check; parts of speech | Type defs + label blanks; Parts of Speech row; **Remember** Skill Check | S. pirate ships + Skill Check demo | 3 sentences + **D** labels | — | D/Imp/Int/E + Divide | **CP10** oral | Sentence Construction, Analogy Codebreaker |
| **8** | Noun Check & Intensifiers | Noun Check; intensifiers | Vocab template + analogy; **Remember** Noun Check + intensifier rule | — | 3 sentences + **D/E** labels | — | Intensifier = Adv; Noun Check | **Checkup 11** — not in packet body | Sentence Construction, Analogy Codebreaker |
| **9** | Cap/Punct & Review | Classify; cap/punct; revision (TE) | Cap/punct pointer to **Ch.1 Reference** | — | 3 sentences + **D/E** | Cap/punct exercise (Alex sentence) | Point to Ch.1 reference | **CP12** revision — TE only | Sentence Construction |

### Section label rules by lesson

| Lessons | Required sections |
|---------|-------------------|
| 1–5 | Learn → Practice Together → Apply → Memory Check → Teacher Check |
| 3 | Learn (Mover callout) → Practice Together → Apply → checks |
| 6 | Practice Together → Memory Check → Teacher Check *(no Apply)* |
| 7–8 | Vocabulary & Analogy block → Learn → Practice Together → checks |
| 9 | Practice Together → Cap/Punct → Memory Check → Teacher Check |

### Vocabulary (L7–8)

- **Locked (§11):** Do not pre-fill vocabulary unless assigned by Teacher Manual or Guided Notes.
- **Student packet (unassigned sections):** word, definition, synonym, antonym, sentence, drawing box — all blank.
- **Teacher edition (unassigned sections):** label **Teacher-assigned word**; no invented model vocabulary.
- Analogy lines from Guided Notes: L7 rhyming; L8 synonym — relationship choices formatted as separate options (fix GN run-together).

### Cap/punct (L9)

- **Sentence (locked GN):** *No, Alex did not go home with John during carpool on Friday.*
- Bold corrections: N, comma, A, J, F, period.
- **Locked (§11):** Do not invent or guess rule numbers. Students use the Chapter 1 protected Capitalization and Punctuation Reference; student materials do not provide guessed rule numbers. Teacher edition provides rule numbers only when directly confirmed; otherwise mark **Verify against protected reference.**
- TM/test cap/punct sentences (e.g. Nancy, Lindsey) are separate assessment resources — not student packet substitutes.
- Do **not** embed full Ch.1 reference pages in Ch.2 packet; cross-reference only.

### Write-your-own (L1–5)

- Minimum **4** blank lines.
- Pattern hint in section header only (SN V, etc.) — not a second classified example.

---

# 8. Teacher Edition Rules

Mirror `docs/standards/packet-content-rules.md` and Chapter 1 precedent:

1. **Identical page count and page order** to student packet.
2. **Physical page parity** — page N of teacher aligns with page N of student for duplex printing.
3. **Preserve all student writing spaces** — answers fill blanks without removing lines.
4. **Classification keys** use §3–§4 formatting; discovery order documented in **Procedure** notes where display differs from Q&A sequence.
5. **Answers in bold blue** `#1F4E79`; procedures/timing in **italic gray** `#666666`.
6. **Separate content types:**
   - Inline model answers (same position as student blanks)
   - Margin/sidebar **Procedure** (Q&A oral scripts — cite `lesson-script-map.md`)
   - **Also Accept** alternates when TM allows
7. **Not in student packet:** jingle lyrics (hint only), CP sentence keys, revision strategy tables (L9), Power Words, Noun Check full oral script.
8. **Teacher appendix (optional end matter):** CP4–CP12 quick keys — clearly labeled *Classroom Practice — oral/assessment only*.

---

# 9. Assessment Rules

## 9.1 In-Class Chapter Review

| Rule | Specification |
|------|---------------|
| Files | Separate DOCX: review + review-key |
| Page limit | **≤ 2 pages** each |
| Print | Front/back friendly |
| Content | **Locked (§11):** Review sentences from **confirmed Guided Notes classification sentences only** — no Classroom Practice, test, or teacher-created examples unless specifically approved |
| Naming | `chapter-02-in-class-chapter-review.docx` / `…-key.docx` |
| Language | Never "Study Guide," "test prep," or "take-home study" |

## 9.2 Suggested review skill coverage

- SN/V/P1 classification (2 items)  
- Full-pattern classify with D/E (2 items)  
- Adverb + adjective questions (fill-in)  
- a/an (2 items)  
- One analogy style (rhyming or synonym)  
- Optional: one cap/punct item using Alex GN sentence (rule numbers per §11 — no guessed numbers in student materials)

## 9.3 Classroom Practice / Checkup / Test

- **Not duplicated** inside Shurley Packet body.
- Documented in `classroom-practice-map.md` for oral assessment only.

---

# 10. Validation Requirements

`scripts/validate_chapter_02.py` must fail on any critical error. Modeled on `validate_chapter_01.py`.

## 10.1 Structural checks (automated)

| Check | Pass criteria |
|-------|---------------|
| Page parity | Student page count == Teacher page count |
| Review limit | In-Class review ≤ 2 pages; key ≤ 2 pages |
| Study Guide ban | No "Study Guide" string in any output |
| File existence | All four DOCX paths present after generation |
| Protected reference | Ch.1 cap/punct PDF hash unchanged if referenced |

## 10.2 Classification checks (automated + semi-automated)

| Check | Pass criteria |
|-------|---------------|
| Sentence source | Every practice sentence matches Guided Notes corpus (28 + write-your-own prompts) |
| Word order | Classified display preserves original token order (token-level compare) |
| P1 placement | P1 only in pattern column under SN V — never trailing sentence |
| Type placement | D/Imp/Int/E only after end mark (L7+ items) |
| Label set | Only SN, V, Adv, Adj, A, P1, D, Imp, Int, E |
| Imperative abbrev | **Imp** — not I |
| Partial pattern (U-03) | Label count equals classified token count; no empty label columns; no placeholder words |

## 10.3 Visual / layout checks (render QA)

After LibreOffice render (`soffice --headless` + `pdftoppm`):

| Check | Pass criteria |
|-------|---------------|
| Clipped text | None |
| Tiny text | Body ≥ 11 pt effective; labels readable |
| Classification alignment | Labels visually above words on spot-check pages |
| PNG visuals | Reference pages inspected — no branding, no clip |
| Cramped tables | No classification table below minimum row height |
| Blank pages | Zero unintended blank pages |
| Page pairs | Pagination audit doc confirms student/teacher alignment |

## 10.4 Manual audit artifacts (required before release)

| File | Purpose |
|------|---------|
| `work/chapter-02/pagination-audit.md` | Page map |
| `work/chapter-02/page-pair-audit.md` | Student/teacher duplex pairs |
| `work/chapter-02/phase-3-build-report.md` | Build summary |
| `work/chapter-02/slideshow-audit.md` | Slide QA (parallel track) |

## 10.5 Blocking uncertainties

From `source-conflicts.md`. All former blockers are resolved:

| ID | Resolution |
|----|------------|
| C-05 / E-01 | §11 — L9 cap/punct rule numbers |
| F-08 | §11 — L5 noun markers terminology |
| S-04 | §11 — Adverb fourth question |
| U-03 | §4.5 — Partial-pattern display (`partial-pattern-decision.md`) |

**No blocking uncertainties remain** for specification lock. Build scripts may proceed when teacher authorizes generation.

---

# 11. Final Teacher Decisions v1.0

**Status:** LOCKED — 2026-07-26  
**Supersedes:** Open items C-05, E-01, F-08, S-04, and teacher sign-off rows formerly in §10.5.

### L9 Capitalization/Punctuation Rule Numbers

**Decision:** Do not invent or guess rule numbers.

**Student packet:**
- Students use the Chapter 1 protected Capitalization and Punctuation Reference.
- Student materials do not provide guessed rule numbers.

**Teacher edition:**
- Provide rule numbers only when directly confirmed.
- Otherwise mark: **Verify against protected reference.**

**Document:**
- L9 Guided Notes sentence remains the student practice sentence.
- Teacher Manual/test sentences are separate assessment resources.

---

### L5 Article Adjective Terminology

**Decision:** Use:

> Article adjectives are also known as noun markers.

**Do not include:**
- determiners
- alternate grammar terminology

unless directly introduced in the Teacher Manual.

---

### Vocabulary

**Decision:** Do not pre-fill vocabulary unless assigned by Teacher Manual or Guided Notes.

**For unassigned vocabulary sections:**

| Edition | Fields |
|---------|--------|
| **Student packet** | word, definition, synonym, antonym, sentence, drawing box (all blank) |
| **Teacher edition** | **Teacher-assigned word** |

---

### In-Class Chapter Review

**Decision:** Select review sentences only from confirmed Guided Notes classification sentences.

**Do not use:**
- Classroom Practice sentences
- Test sentences
- Teacher-created examples

unless specifically approved.

---

### Adverb Fourth Question

**Decision:** Do not include *To what extent?* in student materials.

**Student reference:**

- How?
- When?
- Where?

**Teacher enrichment only.**

---

### Partial-Pattern Classification Display (U-03)

**Decision:** Partial-pattern sentences display only labels for words that actually exist in the sentence.

**Generator must:** preserve word order; never add missing modifiers, empty labels, or placeholder words; never force the largest pattern; keep P1 below SN V; keep sentence type at the end.

**Implementation:** Classification engine builds labels from actual classified tokens, not the maximum pattern diagram.

**Full detail:** `work/chapter-02/partial-pattern-decision.md` §4.5 locked examples.

---

# Appendix A — Locked Abbreviation Table

| Abbrev | Name | Introduced |
|--------|------|------------|
| SN | Subject Noun | L1 |
| V | Verb | L1 |
| P1 | Pattern 1 (SN V) | L1 |
| Adv | Adverb | L2 |
| Adj | Adjective | L4 |
| A | Article Adjective | L5 |
| D | Declarative | L7 |
| Imp | Imperative | L7 |
| Int | Interrogative | L7 |
| E | Exclamatory | L7 |

---

# Appendix A.1 — Pagination Optimization Rules

**Status:** LOCKED guidance for post-QA pagination passes
**Goal:** Reduce unnecessary blank space by allowing lessons to share pages when appropriate, without compromising usability.

## Constraints (never violate)

| Rule | Requirement |
|------|-------------|
| Font size | Do not shrink body or label fonts |
| Writing space | Preserve apply blocks (4 lines), memory-check lines, vocab fields |
| Classification workspace | Keep 3 blank classification lines per practice item |
| Student reflection | Preserve apply, memory check, teacher check, drawing boxes |
| Lesson integrity | Do not split a single practice activity across pages |
| Parity | Student and teacher editions must render the same page count |

## Allowed

- Lesson headings after a clear section separator on the same logical page
- Short note sections sharing space when combined content fits one rendered sheet
- Memory checks following lesson content when room allows
- Moving final practice item onto a prior under-filled practice page (same lesson)
- Apply + checks on a dedicated lighter follow-on page

## Not allowed

- Stranded headings (banner with no content below)
- Split classification examples mid-item
- Cramped writing or classification areas
- Section merges that overflow to an extra rendered page (net zero or negative savings)
- Teacher/student page-count mismatch

## Validation

After any pagination change:

1. `python3 scripts/validate_chapter_02.py` — parity, classification keys, review limits
2. LibreOffice PDF render — confirm rendered page count, not just logical section count
3. Visual QA on merged or redistributed pages — classification alignment, no clipping

---

# Appendix B — Estimated Page Budget (non-binding target)

| Block | Pages |
|-------|-------|
| Cover | 1 |
| Sentence Blueprint reference | 1–2 |
| Lessons 1–5 | 14–16 |
| Lessons 6–9 | 8–10 |
| **Total student packet** | **24 ± 2** |

In-Class Chapter Review: **+0** inside packet (separate file, ≤ 2 pp).

---

# Appendix C — Generation Command Sequence (future)

**This specification governs the generation command sequence below.** DOCX build has not been started; run only when teacher authorizes.

```bash
python3 scripts/generate_chapter_02.py
python3 scripts/validate_chapter_02.py
# Manual: LibreOffice PDF render + PNG inspection per §10.3
```

---

**Document control:** Changes to §3 (Classification Engine), §4 (Formatting), or §1 (Authority) require teacher approval and version increment.
