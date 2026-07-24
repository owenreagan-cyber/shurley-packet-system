# Shurley Packet Naming Conventions

## Product Name

The final instructional resource is called the **Shurley Packet**. It is a complete instructional workbook, not guided notes.

## Prohibited Names

Never use **Study Guide** in titles, headers, footers, or body text of newly generated materials.

## Approved Resource Names

| Name | Use |
|------|-----|
| Shurley Packet | Full student instructional workbook |
| Teacher Edition | Page-for-page teacher key with notes |
| Chapter Review | Cumulative end-of-chapter review within the student packet |
| In-Class Chapter Review | Condensed classroom review activity (separate file) |
| Classroom Checkpoint | Short in-lesson check (future use) |
| Skill Review | Focused skill practice page (future use) |

## Directory Structure

```
packets/
  student/chapter-XX/chapter-XX-shurley-packet.docx
  teacher-keys/chapter-XX/chapter-XX-shurley-packet-teacher-edition.docx
  chapter-reviews/chapter-XX/chapter-XX-in-class-chapter-review.docx
  chapter-reviews/chapter-XX/chapter-XX-in-class-chapter-review-key.docx
source-materials/chapter-XX/          # Original teacher materials (never overwrite)
archive/                              # Historical reference only
work/chapter-XX/                      # Planning and build reports
docs/standards/                       # Project standards
scripts/                              # Generation scripts
```

## Filename Pattern

`chapter-{NN}-{resource-type}.docx`

- Use two-digit chapter numbers (`01`, `02`, …).
- Use lowercase kebab-case.
- Student packet: `chapter-01-shurley-packet.docx`
- Teacher edition: `chapter-01-shurley-packet-teacher-edition.docx`
- In-class review: `chapter-01-in-class-chapter-review.docx`
- Review key: `chapter-01-in-class-chapter-review-key.docx`

## Lesson Labels

Use consistent lesson headers:

```
Chapter 1 — Lesson N
[Lesson Title]
```

Instructional section labels (use exactly):

- Learn
- Practice Together
- Practice Independently
- Apply
- Memory Check
- Teacher Check
