# Student Resource QA Rules

Applies to all student-facing packet pages, reference sheets, reviews, and workbook sections.

## Protected Source Material

When integrating official Shurley reference content:

1. Preserve rule numbers, rule sequence, rule wording, headings, examples, capitalization, punctuation, quoted words, italicized or underlined titles, abbreviations, names, dates, addresses, sentence examples, and category groupings.
2. Do not paraphrase, shorten, modernize, simplify, correct, combine, renumber, or silently fix official content.
3. Create a protected transcription file for every reference PDF.
4. Visually compare transcription against rendered PNG pages — do not rely on OCR alone.
5. If exact textual preservation cannot be guaranteed in DOCX, embed the original source pages as full-page images.
6. Flag uncertain characters with `[VERIFY]` notes in the transcription; never substitute inferred wording.

## Page Layout (8.5 × 11 in)

- Use readable fourth-grade fonts (approximately 12–14 pt body text).
- Provide generous handwriting lines and vertical space between questions.
- Size drawing and response boxes appropriately for fourth-grade work.
- Avoid cramped word banks, narrow matching columns, and tightly packed answer choices.
- Avoid tiny text used only to force content onto fewer pages.
- Avoid large unused blank areas and decorative elements that consume student work space.
- Use white space as functional writing and thinking space.

## Fill-in-the-Blank

- Writing lines must be long enough for the expected answer.
- Allow enough vertical spacing for fourth-grade handwriting.
- Do not place multiple blanks too close together.
- Keep the prompt and its answer line together.
- Do not split a fill-in item across pages.

## Matching

- Provide clear separation between columns.
- Use readable labels.
- Provide enough vertical spacing so students can draw or write answers cleanly.
- Avoid crossing lines through neighboring items.
- Use a word-bank or answer-letter format when direct line matching would be visually confusing.

## Word Banks

- Use a clearly bounded box.
- Distribute words evenly.
- Avoid tightly packed comma-separated strings.
- Use multiple rows or columns when appropriate.
- Maintain enough spacing for quick visual scanning.

## Quiz and Reading Checks

Every quiz, reading check, chapter check, or similar assessment must be **no more than two physical pages** (front-to-back on one sheet).

- Maintain readable font size and generous response spacing.
- Do not remove necessary directions.
- Do not compress matching or word banks excessively.
- Use both pages fully and evenly.
- Place the answer key in a separate teacher file.
- Verify physical page count with LibreOffice-rendered PDF and `pdfinfo`.

## Notes and Workbook-Packet Flow

- A new lesson may begin on the remaining portion of a page.
- Insert clear visual separation before a new lesson.
- Do not force every lesson to begin on a new page.
- Do not leave half pages blank merely to preserve lesson boundaries.
- Do not begin a lesson if there is not enough room for its heading plus a meaningful first section.
- Never leave a lesson heading stranded at the bottom of a page.
- Keep related examples and questions together.
- Use controlled page breaks only where instructionally necessary.

## Visual QA Process

1. Render DOCX to PDF via LibreOffice (`soffice --headless`).
2. Record physical page counts with `pdfinfo`.
3. Render every PDF page to PNG with `pdftoppm`.
4. Inspect every page for clipping, crowding, excessive blank space, undersized fonts, cramped handwriting lines, poorly spaced matching/word banks, awkward page breaks, and stranded headings.
5. Re-render and reinspect after every correction.

## Prohibited Labels

Never use **Study Guide** in student-facing titles, headers, footers, or body text.

Approved reference title: **Capitalization and Punctuation Reference**.
