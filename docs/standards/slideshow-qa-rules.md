# Slideshow QA Rules

Applies to every Chapter lesson slideshow (PPTX) now and in future chapters.

## Required QA Workflow

For every PPTX file:

1. Render every slide to images or PDF.
2. Inspect every slide visually.
3. Confirm the deck opens correctly in PowerPoint.
4. Export a PDF backup alongside the PPTX.
5. Record all QA results in a slideshow audit file under `work/chapter-XX/`.

## Slide Inspection Checklist

Verify on every slide:

- [ ] No clipped text
- [ ] No overlapping objects
- [ ] No text outside safe margins
- [ ] No tiny text
- [ ] No unreadable contrast
- [ ] No distorted images
- [ ] No broken icons
- [ ] No empty placeholder boxes
- [ ] No teacher notes accidentally shown to students
- [ ] No answers exposed prematurely
- [ ] No animation-dependent content that becomes missing in PDF export
- [ ] No slide too dense for projector viewing
- [ ] Adequate spacing between prompts, examples, and answer areas
- [ ] Consistent title and footer placement
- [ ] Correct lesson and page references

## Chapter 1 Status

No Chapter 1 slideshow exists in the repository at this time. These requirements are permanent design and content standards. When a Chapter 1 slideshow is created, record results in `work/chapter-01/slideshow-audit.md`.

## Audit File Format

Each slideshow audit should include:

| Field | Content |
|-------|---------|
| File | Path to PPTX |
| Date | QA date |
| Renderer | Tool used (LibreOffice, PowerPoint, etc.) |
| Slide count | Total slides inspected |
| Issues found | List with slide numbers |
| Resolution | Fix applied or open item |
| PDF backup | Path to exported PDF |

## Integration with Packet QA

Slideshow page references must align with the current student packet page numbers. Re-run slideshow QA whenever packet pagination changes.
