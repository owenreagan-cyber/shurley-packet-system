# U-03 Partial-Pattern Classification Display — LOCKED

**Date:** 2026-07-26  
**Branch:** `phase-3/chapter-02-gold-standard`  
**Status:** LOCKED  
**Governing spec:** `work/chapter-02/packet-generation-spec.md` §4.5  
**Conflict ID:** U-03 (`source-conflicts.md`)

---

## Decision

Partial-pattern sentences display **only** the labels for words that actually exist in the sentence.

The classification engine creates labels from **actual classified tokens**, not from the expected maximum Chapter 2 pattern (e.g. `A Adj Adj SN V Adv Adv`).

### Generator requirements (mandatory)

| Rule | Requirement |
|------|-------------|
| Word order | Preserve original sentence word order |
| Missing modifiers | Never add missing modifiers |
| Pattern forcing | Never force every sentence into the largest Chapter 2 pattern |
| Empty labels | Never display empty label columns |
| Placeholders | Never add placeholder words |
| P1 | Keep **P1** below **SN V** in the left pattern column |
| Sentence type | Keep **D / Imp / Int / E** at the end (L7+) |

---

## Reason

Chapter 2 lessons introduce the full pattern diagram (`A Adj Adj SN V Adv Adv`) as a **label-type reference**, not as a fixed column template for every sentence. Early and mid-chapter Guided Notes sentences often contain fewer modifiers (e.g. L1 `Cats ran.`, L2 one adverb, L5 *The girls giggled loudly.* with one Adv and no Adj).

Forcing empty Adv/Adj/A columns would misrepresent the sentence, confuse students, and contradict Teacher Manual marking, which labels only words present while still declaring **SN V / P1**.

Discovery order (SN → V → Adv → Adj → A) governs **Q&A procedure**; display order follows **spoken word order** with labels only above tokens that exist.

---

## Source supporting decision

| Source | Evidence |
|--------|----------|
| `source-conflicts.md` U-03 | *The girls giggled loudly.* — one Adv; full pattern diagram not filled |
| `teacher-manual-alignment.md` L1–L5 | Pattern zone shows label types; GN sentences vary in modifier count |
| `packet-generation-spec.md` §3.2 | "only label words present"; never reorder words |
| `packet-generation-spec.md` §4.5 (prior draft) | Label only words present; no blank columns for missing slots |
| TM Ref 20 / L5 screenshots | Classification marks actual words; P1 under SN V |

---

## Effect on packet generation

- **`generate_chapter_02.py`:** Build label row dynamically from classified token list per sentence; column count = classified word count (+ pattern column + optional type).
- **`validate_chapter_02.py`:** Fail if label columns exceed classified tokens; fail on empty label cells; fail on inserted placeholder words; fail if P1 appears at sentence end.
- **Student packet, teacher keys, In-Class Review:** All classification displays follow this rule.
- **Teacher edition Procedure notes:** Q&A documents questions for **actual words only** — no oral questions for absent modifiers.
- **Resolves U-03** — no longer a blocking uncertainty in §10.5.

---

## Locked examples

### Example 1 — SN V only (L1)

**Sentence:** Cats ran.

**Display:**

```
             SN      V

SN V  P1    Cats    ran.    D
```

*(D shown when sentence-type labeling applies — L7+ items; early lessons omit type.)*

---

### Example 2 — SN V Adv (L2)

**Sentence:** Cats ran quickly.

**Display:**

```
             SN      V      Adv

SN V  P1    Cats    ran    quickly.    D
```

---

### Example 3 — A Adj SN V Adv (L5 partial)

**Sentence:** The small cat ran quickly.

**Display:**

```
             A       Adj     SN      V      Adv

SN V  P1    The     small   cat     ran    quickly.    D
```

---

### Example 4 — Two adverbs, word order preserved (TM specimen)

**Sentence:** The cat ran very fast.

**Discovery:**

| Step | Answer | Label |
|------|--------|-------|
| What ran? | cat | SN |
| What is being said about cat? | ran | V |
| Ran how? | fast | Adv |
| How fast? | very | Adv |

**Display:**

```
             A       SN      V      Adv    Adv

SN V  P1    The     cat     ran    very   fast.    D
```

**Note:** Discovery finds *fast* before *very*, but display keeps spoken order (*very fast*).

---

## Implementation rule

```text
labels[] = classify_tokens(sentence)   # only tokens present
display_columns = [label for (word, label) in labels in sentence word order]
pattern_column = ["SN V", "P1"]          # always left column
type_suffix = sentence_type if L7+ else none
render(pattern_column, display_columns, words, type_suffix)
```

The engine must **not** pad `display_columns` to match the lesson's maximum pattern width.

---

**Document control:** Locked. Changes require teacher approval and spec version increment.
