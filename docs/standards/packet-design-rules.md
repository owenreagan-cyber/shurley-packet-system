# Shurley Packet Design Rules

## Page Setup

| Setting | Value |
|---------|-------|
| Paper size | 8.5 × 11 inches (Letter) |
| Orientation | Portrait |
| Margins | 0.75 in top/bottom/left/right (0.6 in for condensed review) |
| Print mode | Clean black-and-white; restrained accent colors optional |

## Typography

| Element | Size | Weight |
|---------|------|--------|
| Chapter title | 20–22 pt | Bold |
| Lesson banner | 16 pt | Bold |
| Lesson subtitle | 14 pt | Bold |
| Section label (Learn, Apply, etc.) | 13 pt | Bold |
| Body text | 13 pt | Regular |
| Footer page number | 10 pt | Regular |
| Teacher edition answers | 13 pt | Bold, blue (#1F4E79) |

Font: Calibri (system default, prints cleanly).

## Layout Principles

- Generous handwriting space — multi-line blanks, not single underscores.
- Large editing workspaces with room to write corrections above and below.
- Vocabulary drawing boxes: minimum 2.0 in height (6+ blank lines inside border).
- Use full page well — avoid large blank areas and decorative clutter.
- No dark full-page backgrounds.
- No excessive ink use.
- Controlled page breaks — no isolated headings at page bottoms.
- No answer lines split awkwardly across pages when avoidable.

## Visual Components

### Lesson Banner

Centered bold header:

```
Chapter 1 — Lesson N
[Lesson Title]
```

### Remember / Knowledge Box

Light gray border (`#999999`), single-line weight. Brief text inside. No fill color.

### Drawing Box

Bordered empty area with minimum height. No background fill.

### Answer Lines

72-character underscore lines with 7–8 pt spacing between lines.

### Teacher Check Block

Always at lesson end:

```
TEACHER CHECK
Complete: □    Date: __________    Initials: ________
```

## Footer

Restrained centered footer: `Page N` at 10 pt.

## Teacher Edition Visual Distinction

- Model answers in bold blue (`#1F4E79`).
- Teacher notes, timing, and misconceptions in italic gray (`#666666`).
- Alternate acceptable answers noted under **Also Accept**.
- Procedures (ball-passing, letter storage) under **Procedure**.

## Quality Assurance Process

After generating each DOCX:

1. Render to page images via LibreOffice (`soffice --headless`) and `pdftoppm`.
2. Inspect every rendered page for clipping, overlap, broken tables, awkward breaks, cramped space, excessive blank space, isolated headings, and student/teacher page misalignment.
3. Correct generator and re-render until clean.
4. Delete temporary render files before completion.
5. Verify structurally: no "Study Guide" label, matching page order and count, source files unchanged.
