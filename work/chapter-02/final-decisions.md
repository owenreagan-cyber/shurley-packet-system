# Chapter 2 Final Teacher Decisions v1.0

**Date:** 2026-07-26  
**Branch:** `phase-3/chapter-02-gold-standard`  
**Status:** LOCKED  
**Governing spec:** `work/chapter-02/packet-generation-spec.md` §11

---

## 1. L9 Capitalization/Punctuation Rule Numbers

### Decision

Do not invent or guess rule numbers.

- **Student packet:** Students use the Chapter 1 protected Capitalization and Punctuation Reference; student materials do not provide guessed rule numbers.
- **Teacher edition:** Provide rule numbers only when directly confirmed; otherwise mark **Verify against protected reference.**
- **L9 practice sentence:** Guided Notes Alex sentence remains the student practice sentence. Teacher Manual and test sentences are separate assessment resources.

### Reason

Guided Notes bold corrections (N, comma, A, J, F, period) are confirmed but do not map to numbered rules in the student source. Teacher Manual and Chapter Test use different sentences (Nancy, Lindsey) with explicit rule numbers that do not transfer to the Alex sentence without verification against the protected Ch.1 reference.

### Source supporting decision

| Source | Evidence |
|--------|----------|
| `source-conflicts.md` C-05, E-01 | GN Alex sentence vs TM/test Nancy/Lindsey sentences; GN has no rule numbers |
| `teacher-manual-alignment.md` L9 | TM editing examples and test keys use alternate sentences with numbered rules |
| `packet-generation-spec.md` §7 Cap/punct | Cross-reference to `source-materials/reference/shurley-capitalization-punctuation-reference.pdf` |
| `docs/standards/packet-content-rules.md` | No paraphrased or invented reference material |

### Effect on packet generation

- Student L9 cap/punct exercise prints Alex sentence with bold-letter corrections only; pointer to Ch.1 protected reference — no rule-number column.
- Teacher key for L9 cap/punct includes confirmed rule numbers where verified against the PDF; unverified items show **Verify against protected reference.**
- `validate_chapter_02.py` must reject invented rule numbers in student output.
- Resolves blocking items C-05 and E-01 in `source-conflicts.md`.

---

## 2. L5 Article Adjective Terminology

### Decision

Use exactly:

> Article adjectives are also known as noun markers.

Do not include **determiners** or alternate grammar terminology unless directly introduced in the Teacher Manual.

### Reason

Teacher Manual Jingle 7 and Reference 20 oral Q5 use **noun markers**. The term **determiners** does not appear in Chapter 2 Teacher Manual materials. Guided Notes provide two blanks for "also known as"; only one TM-confirmed answer exists.

### Source supporting decision

| Source | Evidence |
|--------|----------|
| `source-conflicts.md` F-08 | TM: noun markers; determiners not in TM Ch.2 |
| `lesson-script-map.md` L5 | Jingle 7 / Ref 20: memorize a, an, the as noun markers |
| `teacher-manual-alignment.md` L5 | Article adjective introduction aligns with noun-marker language |
| `visual-language-guide.md` | Poster terminology: noun markers |

### Effect on packet generation

- L5 Learn section fills the "also known as" blank with **noun markers** (single answer line).
- Generator and validator must not emit **determiners** in student or teacher inline answers for L5.
- Resolves blocking item F-08 in `source-conflicts.md`.

---

## 3. Vocabulary

### Decision

Do not pre-fill vocabulary unless assigned by Teacher Manual or Guided Notes.

**Unassigned vocabulary sections:**

| Edition | Content |
|---------|---------|
| Student packet | Blank template: word, definition, synonym, antonym, sentence, drawing box |
| Teacher edition | **Teacher-assigned word** label — no model fill for TM-only words |

### Reason

Guided Notes L7–8 use blank vocabulary templates. Teacher Manual assigns words (**soothing**, **urgent**) for oral instruction and Classroom Practice but does not authorize printing those words as pre-filled student answers without explicit GN assignment.

### Source supporting decision

| Source | Evidence |
|--------|----------|
| `source-conflicts.md` V-01 | TM supplies soothing; GN blank template |
| `teacher-manual-alignment.md` L7, L8 | TM vocabulary words vs GN blank fields |
| `classroom-practice-map.md` | CP10 vocabulary oral — not packet body |
| `packet-generation-spec.md` §1 | TM wins on terminology; GN wins on student-facing structure |

### Effect on packet generation

- L7–8 vocabulary blocks render empty fields in student packet.
- Teacher edition shows **Teacher-assigned word** placeholder; optional sidebar may cite TM model (soothing/urgent) as oral reference only — not as inline student answer.
- Validator rejects pre-filled vocabulary words not present in Guided Notes assignment text.

---

## 4. In-Class Chapter Review

### Decision

Select review sentences only from confirmed Guided Notes classification sentences.

Do not use Classroom Practice sentences, test sentences, or teacher-created examples unless specifically approved.

### Reason

Guided Notes corpus (28 classification sentences + write-your-own prompts) is the Tier-2 authority for student-facing practice. CP, Checkup, and test sentences are Tier-1 oral/assessment resources documented separately and must not substitute for GN sentences in printed review materials.

### Source supporting decision

| Source | Evidence |
|--------|----------|
| `packet-generation-spec.md` §1, §9.1 | GN wins on student sentences; CP/test prohibited in packet body |
| `source-conflicts.md` S-01–S-03 | Practice sentence set boundaries |
| `classroom-practice-map.md` | CP4–CP12 oral-only scope |
| `teacher-manual-alignment.md` | GN sentence inventory per lesson |

### Effect on packet generation

- `chapter-02-in-class-chapter-review.docx` draws only from the 28 GN classification sentences (subset per §9.2 skill coverage).
- Review key uses the same GN-sourced sentences with TM-aligned classification keys.
- Generator must not pull CP10/CP12 or test editing sentences into review DOCX without explicit approval flag.

---

## 5. Adverb Fourth Question

### Decision

Do not include **To what extent?** in student materials.

**Student reference (locked):**

- How?
- When?
- Where?

Fourth question is teacher enrichment only.

### Reason

Guided Notes L2 provide three adverb question blanks. Teacher Manual enrichment mentions a fourth question in some contexts; one slide title may show *To what extent?* — but this is not Tier-2 student content and would introduce inconsistency with GN fill-ins.

### Source supporting decision

| Source | Evidence |
|--------|----------|
| `source-conflicts.md` S-04, F-04 | TM: How/When/Where; fourth question enrichment only |
| `lesson-script-map.md` L2 | Three adverb questions locked |
| `phase-3-source-audit.md` | Slide-only fourth question flagged T3 |
| `packet-generation-spec.md` §5.1 | Student adverb reference locked to three questions |

### Effect on packet generation

- L2 Learn and reference pages print three adverb questions only.
- Teacher edition Procedure notes may mention *To what extent?* as oral enrichment — not in student-visible inline text.
- Validator fails if *To what extent?* appears in student packet body.
- Resolves blocking item S-04 in `source-conflicts.md`.

---

## 6. Partial-Pattern Classification Display (U-03)

### Decision

Partial-pattern sentences display **only** the labels for words that actually exist in the sentence. The classification engine creates labels from actual classified tokens, not from the expected maximum Chapter 2 pattern.

**Generator must:**

- preserve original sentence word order
- never add missing modifiers
- never force every sentence into the largest Chapter 2 pattern
- never display empty labels
- never add placeholder words
- keep P1 below SN V
- keep sentence type at the end

### Reason

The full pattern diagram (`A Adj Adj SN V Adv Adv`) is a label-type reference, not a fixed column template. Guided Notes sentences through L1–9 vary in modifier count; TM marking labels only words present while still declaring SN V / P1.

### Source supporting decision

| Source | Evidence |
|--------|----------|
| `source-conflicts.md` U-03 | *The girls giggled loudly.* — partial Adv slot |
| `teacher-manual-alignment.md` | Pattern zone vs actual GN sentence modifier counts |
| `packet-generation-spec.md` §3.2, §4.5 | Word-order preservation; label only present words |
| `partial-pattern-decision.md` | Full examples and implementation rule |

### Effect on packet generation

- Dynamic label rows in all classification displays (student, teacher, review).
- Validator rejects empty columns, placeholder words, and padded pattern widths.
- Resolves the last §10.5 blocking uncertainty.

---

## Blocking status

**All specification blockers resolved** as of U-03 lock (2026-07-26). DOCX generation not started — awaiting teacher authorization to run build scripts.

---

**Document control:** Amendments require teacher approval and version increment.

