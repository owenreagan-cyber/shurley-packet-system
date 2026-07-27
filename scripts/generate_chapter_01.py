#!/usr/bin/env python3
"""Generate Chapter 1 Gold Standard Shurley Packet system."""

from __future__ import annotations

from dataclasses import dataclass, field
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REF_PUNCT_IMG = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference-page-1.png"
REF_CAP_IMG = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference-page-2-oriented.png"
REF_SOURCE_PDF = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference.pdf"

STUDENT_OUT = ROOT / "packets/student/chapter-01/chapter-01-shurley-packet.docx"
TEACHER_OUT = ROOT / "packets/teacher-keys/chapter-01/chapter-01-shurley-packet-teacher-edition.docx"
REVIEW_OUT = ROOT / "packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review.docx"
REVIEW_KEY_OUT = ROOT / "packets/chapter-reviews/chapter-01/chapter-01-in-class-chapter-review-key.docx"

SENTENCE_PARTS = ["Capital letter", "End mark", "Complete sense", "Subject", "Verb"]

SYN_ANT = [
    ("remember, forget", "Antonym"),
    ("give, share", "Synonym"),
    ("hurry, rush", "Synonym"),
    ("clumsy, graceful", "Antonym"),
    ("shy, bashful", "Synonym"),
    ("soar, fly", "Synonym"),
    ("cautious, hasty", "Antonym"),
    ("often, frequent", "Synonym"),
]

ANALOGY_TYPES = [
    ("Synonym", "big : large :: sound : noise", "The words in each pair mean almost the same."),
    ("Antonym", "big : small :: fast : slow", "The words in each pair are opposites."),
    ("Rhyming", "near : deer :: jump : stump", "The words in each pair rhyme."),
    ("Part-to-Whole", "leaf : tree :: paw : dog", "The first word is part of the second."),
]

ANALOGY_PRACTICE = [
    ("giggle : chuckle :: unhappy : ___________", "Synonym", ["sad", "gloomy", "miserable"]),
    ("fire : ice :: asleep : ___________", "Antonym", ["awake"]),
    ("hat : cat :: __________ : book", "Rhyming", ["look", "cook", "hook"]),
    ("tree : forest :: page : ___________", "Part-to-Whole", ["book"]),
]

GOAL_SORT = [
    ("Learn all multiplication facts by December", "L", "A"),
    ("Read for 20 minutes tonight", "S", "A"),
    ("Make the school basketball team this year", "L", "P"),
    ("Clean my room before dinner", "S", "P"),
    ("Improve my handwriting this semester", "L", "A"),
    ("Write a letter to my future self", "S", "A"),
]

MODEL_LETTER = """Dear Future Me,

Right now I am a fourth grader who loves drawing, playing soccer, and reading adventure books. My favorite food is mac and cheese, and my best friend is Maya. Something important to me is being a kind friend.

Fourth grade feels exciting and a little new. I am excited about science experiments and the class read-aloud. I feel nervous about harder math, but I plan to ask for help and keep practicing.

One academic goal is to read 20 chapter books this year. A short-term step is to read for 20 minutes four nights each week. One personal goal is to keep my room tidy. A short-term step is to put away my clothes every night.

I hope you remember how hard you worked and how much you grew. Keep being curious, keep being kind, and keep trying even when something feels tough.

Your friend,
Alex"""

ANSWER_BLUE = RGBColor(0x1F, 0x4E, 0x79)
NOTE_GRAY = RGBColor(0x66, 0x66, 0x66)


@dataclass
class TeacherPageNotes:
    title: str
    answers: list[str] = field(default_factory=list)
    alternates: list[str] = field(default_factory=list)
    prompts: list[str] = field(default_factory=list)
    timing: str = ""
    misconceptions: list[str] = field(default_factory=list)
    procedures: list[str] = field(default_factory=list)


# ── Document helpers ─────────────────────────────────────────────────────────

def set_margins(section, t=0.75, b=0.75, l=0.75, r=0.75):
    section.top_margin = Inches(t)
    section.bottom_margin = Inches(b)
    section.left_margin = Inches(l)
    section.right_margin = Inches(r)


def style_run(run, size=13, bold=False, italic=False, color=None):
    run.font.name = "Calibri"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color


def add_run(p, text, **kw):
    run = p.add_run(text)
    style_run(run, **kw)
    return run


def add_para(doc, text="", bold=False, italic=False, size=13, align=None, space_after=6, space_before=0, color=None):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    if text:
        add_run(p, text, size=size, bold=bold, italic=italic, color=color)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    return p


def add_heading(doc, text, size=16):
    return add_para(doc, text, bold=True, size=size, space_after=8)


def add_section_label(doc, text):
    return add_para(doc, text, bold=True, size=13, space_before=8, space_after=4)


def add_body(doc, text, **kw):
    return add_para(doc, text, **kw)


def add_bullet(doc, text):
    return add_body(doc, f"• {text}", space_after=3)


def add_blank_lines(doc, count=3, label=None):
    if label:
        add_body(doc, label, bold=True, space_after=4)
    for _ in range(count):
        p = doc.add_paragraph()
        add_run(p, "_" * 72, size=13)
        p.paragraph_format.space_after = Pt(7)


def add_page_break(doc):
    doc.add_page_break()


def add_page_footer(section, num):
    footer = section.footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.clear()
    add_run(p, f"Page {num}", size=10)


def add_knowledge_box(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "8")
        b.set(qn("w:space"), "4")
        b.set(qn("w:color"), "999999")
        pBdr.append(b)
    pPr.append(pBdr)
    add_run(p, "Remember: ", bold=True, size=13)
    add_run(p, text, size=13)


def add_analogy_lesson_banner(doc, title: str):
    add_para(
        doc,
        "Chapter 1 — Lesson 4",
        bold=True,
        size=18,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=4,
    )
    add_para(
        doc,
        title,
        bold=True,
        size=16,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=12,
    )


def add_analogy_section_label(doc, text: str):
    return add_para(doc, text, bold=True, size=18, space_before=4, space_after=8)


def add_analogy_body(doc, text: str, **kw):
    defaults = {"size": 14, "space_after": 8}
    defaults.update(kw)
    return add_para(doc, text, **defaults)


def add_analogy_example(doc, text: str, **kw):
    defaults = {"size": 16, "space_after": 10, "space_before": 2}
    defaults.update(kw)
    return add_para(doc, text, **defaults)


def _paragraph_border(p, color: str = "999999", size: str = "8", space: str = "6"):
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), size)
        b.set(qn("w:space"), space)
        b.set(qn("w:color"), color)
        pBdr.append(b)
    pPr.append(pBdr)


def add_analogy_remember_box(doc):
    table = doc.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    cell = table.rows[0].cells[0]
    _set_cell_margins(cell, top=140, start=180, bottom=140, end=180)
    _clear_cell(cell)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(10)
    add_run(p, "Remember — Analogy Symbols", bold=True, size=15)
    for text in (
        "Colon (:) — separates the two words in each pair.",
        "Double colon (::) — means “is to ___ as”.",
        "“Is to” — connects the first word pair.",
        "“As” — connects the first pair to the second pair.",
    ):
        lp = cell.add_paragraph()
        lp.paragraph_format.space_after = Pt(8)
        add_run(lp, text, size=14)
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(6)


def add_analogy_student_check(doc, prompt: str):
    add_analogy_section_label(doc, "Quick Check")
    add_analogy_body(doc, prompt, space_after=6)
    add_blank_lines(doc, 1)


def _set_cell_margins(cell, top=100, start=140, bottom=100, end=140):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = OxmlElement("w:tcMar")
    for side, val in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = OxmlElement(f"w:{side}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tc_mar.append(node)
    tc_pr.append(tc_mar)


def _set_row_height(row, twips: int = 2200):
    tr_pr = row._tr.get_or_add_trPr()
    tr_height = OxmlElement("w:trHeight")
    tr_height.set(qn("w:val"), str(twips))
    tr_height.set(qn("w:hRule"), "atLeast")
    tr_pr.append(tr_height)


def _clear_cell(cell):
    cell.text = ""
    for p in cell.paragraphs:
        p.clear()


def _fill_analogy_card(cell, relationship: str, analogy: str, explanation: str):
    _clear_cell(cell)
    _set_cell_margins(cell)
    p1 = cell.paragraphs[0]
    p1.paragraph_format.space_after = Pt(8)
    add_run(p1, relationship, bold=True, size=16)
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(8)
    add_run(p2, analogy, size=16)
    p3 = cell.add_paragraph()
    p3.paragraph_format.space_after = Pt(4)
    add_run(p3, explanation, size=14)


def add_analogy_relationship_cards(doc):
    table = doc.add_table(rows=2, cols=2)
    table.style = "Table Grid"
    table.autofit = False
    for row in table.rows:
        _set_row_height(row, 2800)
        for cell in row.cells:
            cell.width = Inches(3.35)

    cards = list(ANALOGY_TYPES)
    for idx, (rel, analogy, explanation) in enumerate(cards):
        r, c = divmod(idx, 2)
        _fill_analogy_card(table.rows[r].cells[c], rel, analogy, explanation)
    doc.add_paragraph()


def add_full_page_image(doc, image_path: Path, max_height_inches: float = 8.75, max_width_inches: float = 7.0):
    try:
        from PIL import Image
    except ImportError:
        from docx.shared import Inches as _Inches
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture(str(image_path), width=_Inches(max_width_inches))
        return

    im = Image.open(image_path)
    w, h = im.size
    height_in = max_height_inches
    width_in = height_in * (w / h)
    if width_in > max_width_inches:
        width_in = max_width_inches
        height_in = width_in * (h / w)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run()
    run.add_picture(str(image_path), width=Inches(width_in), height=Inches(height_in))


def add_drawing_box(doc, lines=8):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "12")
        b.set(qn("w:space"), "4")
        b.set(qn("w:color"), "999999")
        pBdr.append(b)
    pPr.append(pBdr)
    for _ in range(lines):
        p.add_run("\n")


def add_memory_check(doc, questions):
    add_section_label(doc, "MEMORY CHECK")
    add_body(doc, "Without looking back, answer these questions:", italic=True, space_after=4)
    for i, q in enumerate(questions, 1):
        add_body(doc, f"{i}. {q}", space_after=2)
        add_blank_lines(doc, 1)


def add_teacher_check(doc):
    add_section_label(doc, "TEACHER CHECK")
    add_body(doc, "Complete: □     Date: __________     Initials: ________", space_after=12)


def add_lesson_banner(doc, num, title):
    add_para(doc, f"Chapter 1 — Lesson {num}", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_para(doc, title, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)


def add_blank_vocab_template(doc, include_analogy_example=None, analogy_relationship=None):
    add_section_label(doc, "Apply — Vocabulary")
    add_body(doc, "Word: _________________________________")
    add_blank_lines(doc, 2, "Definition:")
    add_blank_lines(doc, 1, "Kid-friendly meaning (in your own words):")
    add_blank_lines(doc, 1, "Synonym:")
    add_blank_lines(doc, 1, "Antonym:")
    add_blank_lines(doc, 2, "Your sentence:")
    add_body(doc, "Memory picture — draw something that helps you remember this word:")
    add_drawing_box(doc, 4)
    if include_analogy_example:
        add_body(doc, f"Example analogy from this lesson: {include_analogy_example}", space_before=6)
        add_body(doc, f"Relationship: {analogy_relationship}")
        add_body(doc, "Your Turn — Create two analogies using your vocabulary word:", bold=True, space_before=6)
        add_blank_lines(doc, 1, "1.")
        add_blank_lines(doc, 1, "2.")


def add_teacher_answer_block(doc, notes: TeacherPageNotes):
    add_heading(doc, notes.title)
    if notes.procedures:
        add_section_label(doc, "Procedure")
        for proc in notes.procedures:
            add_para(doc, proc, italic=True, color=NOTE_GRAY, space_after=4)
    if notes.timing:
        add_section_label(doc, "Timing")
        add_para(doc, notes.timing, italic=True, color=NOTE_GRAY)
    if notes.prompts:
        add_section_label(doc, "Suggested Oral Prompts")
        for pr in notes.prompts:
            add_bullet(doc, pr)
    add_section_label(doc, "Model Answers")
    for ans in notes.answers:
        add_para(doc, ans, bold=True, color=ANSWER_BLUE, space_after=3)
    if notes.alternates:
        add_section_label(doc, "Also Accept")
        for alt in notes.alternates:
            add_para(doc, alt, italic=True, color=ANSWER_BLUE, space_after=3)
    if notes.misconceptions:
        add_section_label(doc, "Common Misconceptions")
        for m in notes.misconceptions:
            add_para(doc, f"• {m}", italic=True, color=NOTE_GRAY, space_after=3)


# ── Student pages ──────────────────────────────────────────────────────────────

def page_cover(doc):
    add_para(doc, "Chapter 1", bold=True, size=22, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_para(doc, "Shurley Packet", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    add_body(doc, "Name: _________________________________")
    add_body(doc, "Date: _________________________________")
    add_body(doc, "Teacher: _______________________________")
    add_body(doc, "Draw a picture about something you are learning in Chapter 1:", space_before=12)
    add_drawing_box(doc, 9)


def page_l1a(doc):
    add_lesson_banner(doc, 1, "Discussion and Goal Setting")
    add_section_label(doc, "Learn")
    add_body(doc, "Good discussions help us learn together. When you share in class, follow these expectations:")
    for rule in ["Listen respectfully.", "Wait for an appropriate turn.", "Stay on topic.",
                 "Link your comment to what another speaker said."]:
        add_bullet(doc, rule)
    add_knowledge_box(doc, "Linking a comment means connecting your idea to what someone else shared.")
    add_section_label(doc, "Learn — Linking Comment Starters")
    for s in ["I agree with ___ because...", "I would like to add to what ___ said...",
              "I have a different idea because...", "When ___ said ___, it made me think...",
              "Can you explain what you meant by...?"]:
        add_bullet(doc, s)
    add_section_label(doc, "Learn — Goals")
    add_body(doc, "A long-term goal takes a longer period of time to achieve.")
    add_body(doc, "A short-term goal can be achieved soon and can serve as a step toward a long-term goal.")
    add_body(doc, "Academic goals focus on learning and schoolwork.")
    add_body(doc, "Personal goals focus on habits, character, relationships, hobbies, and responsibilities.")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Sort the goals below. Write S for short-term or L for long-term. Write A for academic or P for personal.")
    for i, (g, _, _) in enumerate(GOAL_SORT, 1):
        add_body(doc, f"{i}. _____ / _____   {g}")


def page_l1b(doc):
    add_lesson_banner(doc, 1, "Discussion and Goal Setting (continued)")
    add_section_label(doc, "Practice Independently")
    add_body(doc, "Choose one academic long-term goal. Write it below, then write two or three short-term action steps.", bold=True)
    add_blank_lines(doc, 1, "My academic long-term goal:")
    add_blank_lines(doc, 1, "Short-term action steps:")
    add_body(doc, "Choose one personal long-term goal. Write it below, then write two or three short-term action steps.", bold=True, space_before=8)
    add_blank_lines(doc, 1, "My personal long-term goal:")
    add_blank_lines(doc, 1, "Short-term action steps:")
    add_section_label(doc, "Apply")
    add_body(doc, "Write one linking comment you could use during a class discussion. Use a sentence starter from this lesson.")
    add_blank_lines(doc, 1)
    add_memory_check(doc, [
        "Name two discussion expectations.",
        "What is the difference between a short-term goal and a long-term goal?",
    ])
    add_teacher_check(doc)


def page_l2a(doc):
    add_lesson_banner(doc, 2, "Journaling and Letter to Future Me")
    add_section_label(doc, "Learn")
    add_knowledge_box(doc, "A journal is a personal written record of thoughts, feelings, experiences, plans, and imagined stories.")
    add_body(doc, "You may write about:", space_before=6)
    for topic in ["Family", "Friends", "Pets", "Hobbies", "Favorite activities", "Important events",
                  "Future plans", "Worries", "Goals", "Made-up stories"]:
        add_bullet(doc, topic)
    add_section_label(doc, "Practice Together")
    add_body(doc, "Choose one journal topic from the list. Write a short journal entry below.")
    add_blank_lines(doc, 3)
    add_section_label(doc, "Learn — Letter to Future Me")
    add_body(doc, "You will write a letter to yourself to read during the last week of school. Include these four parts:")
    for part in ["1. Who I Am Right Now", "2. My Thoughts About Fourth Grade",
                 "3. My Goals and Action Steps", "4. A Message to My Future Self"]:
        add_body(doc, part)


def page_l2b(doc):
    add_lesson_banner(doc, 2, "Planning Organizer — Part 1")
    add_body(doc, "You may combine sections naturally into paragraphs. You do not need exactly three paragraphs.", italic=True, space_after=8)
    add_section_label(doc, "Practice Independently — Planning Organizer")
    for title, prompts in [
        ("Who I Am Right Now", ["What are your favorite hobbies?", "What are your favorite foods, games, books, or activities?", "What is important to you right now?"]),
        ("My Thoughts About Fourth Grade", ["What are you excited about?", "What feels new?", "What makes you nervous?", "How will you handle challenges?"]),
    ]:
        add_body(doc, title, bold=True, space_before=6)
        for pr in prompts:
            add_body(doc, f"  • {pr}", space_after=2)
        add_blank_lines(doc, 1)


def page_l2b2(doc):
    add_lesson_banner(doc, 2, "Planning Organizer — Part 2")
    add_section_label(doc, "Practice Independently — Planning Organizer (continued)")
    for title, prompts in [
        ("My Goals and Action Steps", ["What is one academic goal?", "What short-term actions will help you reach it?", "What is one personal goal?", "What short-term actions will help you reach it?"]),
        ("A Message to My Future Self", ["What do you hope you accomplished?", "What do you want your future self to remember?", "What encouragement would you give yourself?"]),
    ]:
        add_body(doc, title, bold=True, space_before=6)
        for pr in prompts:
            add_body(doc, f"  • {pr}", space_after=2)
        add_blank_lines(doc, 1)


def page_l2c(doc):
    add_lesson_banner(doc, 2, "Model Letter to Future Me")
    add_section_label(doc, "Learn — Model Letter")
    add_body(doc, "Read this fourth-grade model letter. Notice how it includes all four parts.", italic=True)
    for line in MODEL_LETTER.split("\n"):
        add_body(doc, line, space_after=1)


def page_l2d(doc):
    add_lesson_banner(doc, 2, "Letter to Future Me — Supported Writing")
    add_section_label(doc, "Apply — Supported Writing Template")
    add_body(doc, "Use your planning organizer to write your letter. The lines below give you extra support.", italic=True)
    add_blank_lines(doc, 1, "Dear Future Me,")
    add_blank_lines(doc, 4)
    add_blank_lines(doc, 1, "Sincerely,")
    add_blank_lines(doc, 1, "[Your Name]")


def page_l2e(doc):
    add_lesson_banner(doc, 2, "Letter to Future Me — Final Draft")
    add_section_label(doc, "Apply — Write Your Letter")
    add_body(doc, "Write your final letter on the lines below. Use your planning organizer and model letter for ideas.")
    add_blank_lines(doc, 5)
    add_section_label(doc, "Apply — Envelope Directions")
    add_body(doc, "When your letter is finished, fold it and place it in an envelope. Write on the envelope:")
    add_bullet(doc, "Your first and last name")
    add_bullet(doc, "Teacher or class")
    add_bullet(doc, '"Do Not Open Until the Last Week of School"')
    add_memory_check(doc, [
        "What is a journal?",
        "What are the four parts of your Letter to Future Me?",
    ])
    add_teacher_check(doc)


def page_l3a(doc):
    add_lesson_banner(doc, 3, "Complete Sentences, Synonyms, and Antonyms")
    add_section_label(doc, "Learn")
    add_body(doc, "What five things does a sentence need to make it complete? (Hint: Think about the Sentence Jingle.)")
    add_blank_lines(doc, 5)
    add_knowledge_box(doc, "The five parts of a complete sentence are: Capital letter, End mark, Complete sense, Subject, and Verb.")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Check each part when you write a sentence:")
    for part in SENTENCE_PARTS:
        add_body(doc, f"☐  {part}")
    add_section_label(doc, "Learn — Synonyms and Antonyms")
    add_body(doc, "Synonyms are words that have almost the same meanings.")
    add_body(doc, "Examples: noisy and loud, run and dash, yell and shout")
    add_body(doc, "Antonyms are words that have opposite meanings.")
    add_body(doc, "Examples: night and day, run and walk, yell and whisper")


def page_l3b(doc):
    add_lesson_banner(doc, 3, "Synonyms and Antonyms Practice")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Look at each pair. Circle Synonym or Antonym.")
    for i, (pair, _) in enumerate(SYN_ANT, 1):
        add_body(doc, f"{i}.  {pair}          Synonym   or   Antonym")
    add_section_label(doc, "Practice Independently")
    add_body(doc, "Write one synonym pair and one antonym pair of your own.")
    add_blank_lines(doc, 1, "Synonym pair:")
    add_blank_lines(doc, 1, "Antonym pair:")


def page_l3c(doc):
    add_lesson_banner(doc, 3, "Vocabulary and Memory Check")
    add_blank_vocab_template(doc)
    add_memory_check(doc, [
        "Name the five parts of a complete sentence.",
        "What is a synonym?",
    ])
    add_teacher_check(doc)


def page_l4a(doc):
    add_analogy_lesson_banner(doc, "Understanding Analogies")
    add_analogy_section_label(doc, "Learn")
    add_analogy_body(
        doc,
        "An analogy is a way of thinking about how pairs of words are related. "
        "It is a special word puzzle.",
    )
    add_analogy_example(doc, "Spoken example: boat is to goat as fan is to ___________.")
    add_analogy_example(doc, "Written example: front : back :: top : ___________")
    add_analogy_remember_box(doc)
    add_analogy_section_label(doc, "Worked Example")
    add_analogy_example(doc, "front : back :: top : bottom")
    add_analogy_body(
        doc,
        "The first pair shows opposites. The second pair shows opposites too. "
        "That is an antonym analogy.",
        italic=True,
    )
    add_analogy_student_check(
        doc,
        "Try it: boat is to goat as fan is to ___________. "
        "Write the word that completes the rhyme.",
    )


def page_l4a2(doc):
    add_analogy_lesson_banner(doc, "Four Common Analogy Relationships")
    add_analogy_section_label(doc, "Learn — Four Relationship Types")
    add_analogy_body(
        doc,
        "Study each relationship card below. Notice the large example and the short explanation.",
        space_after=10,
    )
    add_analogy_relationship_cards(doc)
    add_analogy_body(
        doc,
        "Tip: Read the relationship name first, then read the example aloud using “is to” and “as.”",
        italic=True,
        space_before=4,
    )


def page_l4b(doc):
    add_lesson_banner(doc, 4, "Analogy Practice")
    add_section_label(doc, "Practice Together")
    for prompt, _, _ in ANALOGY_PRACTICE:
        add_body(doc, prompt)
        add_body(doc, "Circle relationship:  synonym   antonym   rhyming   part-to-whole")
        doc.add_paragraph()
    add_section_label(doc, "Practice Independently")
    add_body(doc, "Circle the word or pair that best fits each analogy.", bold=True)
    add_body(doc, "1.  weak : strong :: hot : ________")
    add_body(doc, "       weather     cold     warm")
    add_body(doc, "2.  mouse : house :: ______________")
    add_body(doc, "       sold : bold     tall : short")


def page_l4c(doc):
    add_lesson_banner(doc, 4, "Vocabulary and Analogy Example")
    add_blank_vocab_template(doc, "encourage : cheer :: easy : simple", "Synonym")


def page_l4d(doc):
    add_lesson_banner(doc, 4, "Create-Your-Own Analogies")
    add_section_label(doc, "Apply — Create Your Own")
    add_body(doc, "Write two analogies of your own. Label the relationship for each.")
    add_blank_lines(doc, 1, "1.")
    add_blank_lines(doc, 1, "2.")
    add_memory_check(doc, [
        "What does :: mean in an analogy?",
        "Name the four analogy relationship types.",
        "Give one example of a synonym analogy.",
    ])
    add_teacher_check(doc)


def page_ref_intro(doc):
    add_para(
        doc,
        "Capitalization and Punctuation Reference",
        bold=True,
        size=18,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=10,
    )
    add_body(
        doc,
        "Use this reference during Lessons 5 and 6. The next pages show the official "
        "Shurley punctuation and capitalization rules.",
        italic=True,
        space_after=8,
    )
    add_body(doc, "Reference 9 — Punctuation Rules (next page)", space_before=8)
    add_body(doc, "Reference 7 — Capitalization Rules (following page)")


def page_ref_punctuation(doc):
    add_full_page_image(doc, REF_PUNCT_IMG)


def page_ref_capitalization(doc):
    add_full_page_image(doc, REF_CAP_IMG)


def page_l5a(doc):
    add_lesson_banner(doc, 5, "Vocabulary and Analogy Example")
    add_blank_vocab_template(doc, "fraction : whole :: wing : bird", "Part-to-Whole")


def page_l5a2(doc):
    add_lesson_banner(doc, 5, "Capitalization Practice")
    add_section_label(doc, "Learn")
    add_knowledge_box(doc, "Proper nouns name specific people, places, or things. Proper nouns begin with a capital letter.")
    add_section_label(doc, "Practice Together — Capitalization")
    add_body(doc, "Write the correct capital letter above each word that should be capitalized.")
    add_body(doc, "Passage 1:", bold=True)
    add_body(doc, "my friends and i will meet amy at the ford's theater on friday night to see nim's island.")
    add_blank_lines(doc, 2)
    add_body(doc, "Passage 2:", bold=True)
    add_body(doc, "my cousins, reagan and beth, went to the parade on main street in july.")
    add_blank_lines(doc, 2)


def page_l5b(doc):
    add_lesson_banner(doc, 5, "Editing Practice — Capitals")
    add_section_label(doc, "Practice Independently — Editing")
    add_body(doc, "Each sentence below needs capital letters. Write the correct capital letter above each mistake. Then rewrite the sentence correctly.")
    add_body(doc, "Sentence 1:", bold=True)
    add_body(doc, "we drove to lake michigan on saturday with mrs. daniels.")
    add_blank_lines(doc, 2, "Rewrite:")
    add_body(doc, "Sentence 2:", bold=True)
    add_body(doc, "yes, sam and i work on saturdays at quickfill gas on jasper road in denver.")
    add_blank_lines(doc, 2, "Rewrite:")
    add_memory_check(doc, [
        "What is a proper noun?",
        "What letter should a proper noun begin with?",
    ])
    add_teacher_check(doc)


def page_l6a(doc):
    add_lesson_banner(doc, 6, "Vocabulary and Analogy Example")
    add_blank_vocab_template(doc, "individual : community :: bird : flock", "Part-to-Whole")


def page_l6a2(doc):
    add_lesson_banner(doc, 6, "Capitalization and Punctuation")
    add_section_label(doc, "Learn")
    add_body(doc, "Sentences need correct capital letters, commas, periods, question marks, exclamation marks, and apostrophes.")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Read each sentence. Look for correct capitalization and punctuation.")
    add_body(doc, "1. May I walk to Central Park with Jeff, Lonny, and Tina?")
    add_body(doc, "2. Class, I would like you to meet Ally Mona, our new student.")
    add_blank_lines(doc, 1, "What did you notice about capitals, commas, and end marks?")


def page_l6b(doc):
    add_lesson_banner(doc, 6, "Editing Practice — Mixed Skills")
    add_section_label(doc, "Practice Independently — Editing")
    add_body(doc, "Correct each capitalization and punctuation mistake. Rewrite each sentence on the lines below.")
    add_body(doc, "Sentence 1:", bold=True)
    add_body(doc, "yes mr green will move to denver colorado on june 18 2024")
    add_blank_lines(doc, 2, "Rewrite:")
    add_body(doc, "Sentence 2:", bold=True)
    add_body(doc, "did your teacher ms coleman read charlottes web to your class today")
    add_blank_lines(doc, 2, "Rewrite:")
    add_memory_check(doc, [
        "Name three punctuation marks used in complete sentences.",
        "What is one thing you check when you edit a sentence?",
    ])
    add_teacher_check(doc)


def add_review_content(doc):
    add_section_label(doc, "Part A — Complete Sentences")
    add_body(doc, "Name the five parts of a complete sentence:")
    add_blank_lines(doc, 1)
    add_section_label(doc, "Part B — Vocabulary")
    add_body(doc, "Match each word to its meaning. Write the letter on the line.")
    add_body(doc, "____ encourage          A. a part of a whole number")
    add_body(doc, "____ magnify             B. a town or group of people")
    add_body(doc, "____ community           C. to cheer on")
    add_body(doc, "____ fraction            D. to make something appear larger")
    add_section_label(doc, "Part C — Synonyms and Antonyms")
    add_body(doc, "1. Synonyms are words that _______________________________.")
    add_body(doc, "2. Antonyms are words that _______________________________.")
    add_body(doc, "3. Circle:  hot/warm = Synonym or Antonym?     run/walk = Synonym or Antonym?")


def add_review_content_page2(doc):
    add_section_label(doc, "Part D — Analogy Relationships")
    add_body(doc, "1. List the four analogy relationship types:")
    add_blank_lines(doc, 1)
    add_body(doc, "2. Nice : Kind :: Mad : Angry   (relationship: ___________)")
    add_body(doc, "3. Finger : Hand :: Tree : ___________   (relationship: ___________)")
    add_section_label(doc, "Part E — Analogy Practice")
    add_body(doc, "4. big : small :: hot : ___________   (relationship: ___________)")
    add_body(doc, "5. leaf : tree :: paw : ___________   (relationship: ___________)")
    add_section_label(doc, "Part F — Capitalization and Punctuation")
    add_body(doc, "Rewrite correctly. Add capitals, commas, and an end mark:")
    add_body(doc, "kevin asked bobby bill and tonya to his birthday party")
    add_blank_lines(doc, 1)


def page_review(doc):
    add_para(doc, "Chapter 1 — In-Class Chapter Review", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    add_body(doc, "Complete this review in class with your teacher's directions.")
    add_review_content(doc)
    add_teacher_check(doc)


# ── Teacher notes per page ─────────────────────────────────────────────────────

TEACHER_NOTES = [
    TeacherPageNotes("Page 1 — Cover",
                     answers=["Student-drawn illustration. No fixed answer."],
                     prompts=["Invite students to draw something representing Chapter 1 learning so far."],
                     procedures=["Teacher Edition mirrors the student packet page for page. Model answers appear in bold blue."]),
    TeacherPageNotes("Page 2 — Lesson 1: Discussion and Goal Setting",
                     answers=[f"{i}. {t}/{a}" for i, (_, t, a) in enumerate(GOAL_SORT, 1)],
                     alternates=["Accept reasonable goal classifications with brief justification."],
                     prompts=["Why do discussion rules help everyone learn?", "Turn and tell a partner one long-term goal."],
                     timing="15–20 minutes for Learn and Practice Together",
                     misconceptions=["Students may think any comment is 'on topic' even when it does not connect to the discussion."],
                     procedures=[
                         "Ball-Passing Discussion Activity: Form a circle with students. Use a soft ball or stuffed object. "
                         "The student who holds the ball shares one linking comment using a sentence starter from the page. "
                         "Before tossing the ball, the student must link to what the previous speaker said. "
                         "The next student repeats the pattern. Coach students who share without linking to use a starter. "
                         "Run 2–3 rounds, then transition to written goal work.",
                     ]),
    TeacherPageNotes("Page 3 — Lesson 1 (continued)",
                     answers=["Academic and personal goals with action steps will vary.",
                              "Linking comment will vary — check for use of a sentence starter."],
                     alternates=["Also accept: goals that are realistic for fourth grade with 2–3 concrete steps."],
                     prompts=["Share one action step with your table group."],
                     timing="10–15 minutes",
                     misconceptions=["Students may write goals that are too vague ('be good') without action steps."]),
    TeacherPageNotes("Page 4 — Lesson 2: Journaling",
                     answers=["Journal entry will vary. Check that student chose a topic and wrote thoughtfully."],
                     prompts=["What topic did you choose and why?"],
                     timing="10 minutes for journal warm-up",
                     misconceptions=["Students may confuse a journal with a formal essay — remind them journals are personal."]),
    TeacherPageNotes("Page 5 — Lesson 2: Planning Organizer (Part 1)",
                     answers=["Planning notes for Who I Am / Fourth Grade sections will vary."],
                     prompts=["Read one planning note to a partner."],
                     timing="8–10 minutes"),
    TeacherPageNotes("Page 6 — Lesson 2: Planning Organizer (Part 2)",
                     answers=["Planning notes for Goals / Future Self sections will vary."],
                     timing="8–10 minutes"),
    TeacherPageNotes("Page 7 — Lesson 2: Model Letter",
                     answers=["No student response required — model is provided for study."],
                     prompts=["Which part of the model letter sounds most like you? Why?"],
                     timing="5–8 minutes to read and discuss model"),
    TeacherPageNotes("Page 8 — Lesson 2: Supported Writing",
                     answers=["Draft letter will vary. Check for all four parts somewhere in the letter."],
                     alternates=["Students may combine sections into fewer paragraphs — that is acceptable."],
                     timing="15–20 minutes"),
    TeacherPageNotes("Page 9 — Lesson 2: Final Draft, Envelope, and Memory Check",
                     answers=["Final letter and envelope label will vary.",
                              "Memory Check: journal = personal record; four letter parts listed on student page."],
                     procedures=[
                         "Letter to Future Me — Presentation and Storage: Collect sealed envelopes labeled with "
                         "student first and last name, teacher/class, and 'Do Not Open Until the Last Week of School.' "
                         "Store in a secure, dry location. Return envelopes during the last week of school.",
                     ],
                     timing="15–20 minutes for final draft; 5 minutes for envelope labeling",
                     misconceptions=["Students may forget one of the four letter parts — use the organizer as a checklist."]),
    TeacherPageNotes("Page 10 — Lesson 3: Complete Sentences and Synonyms/Antonyms",
                     answers=["Five parts: Capital letter, End mark, Complete sense, Subject, Verb (order may vary)."],
                     prompts=["Chant the Sentence Jingle together."],
                     timing="15 minutes",
                     misconceptions=["Students may list parts but not apply them when writing sentences."]),
    TeacherPageNotes("Page 11 — Lesson 3: Synonyms and Antonyms Practice",
                     answers=["Syn/Ant: 1.Antonym 2.Synonym 3.Synonym 4.Antonym 5.Synonym 6.Synonym 7.Antonym 8.Synonym"],
                     alternates=["Accept any valid synonym/antonym pairs students create independently."]),
    TeacherPageNotes("Page 12 — Lesson 3: Vocabulary and Memory Check",
                     answers=["Vocabulary word, definition, synonym, antonym, and sentence: teacher-assigned — answers will vary."],
                     prompts=["What strategy helps you remember a new vocabulary word?"]),
    TeacherPageNotes("Page 13 — Lesson 4: Understanding Analogies",
                     answers=["Quick Check: man (rhyming). Worked example: bottom (antonym)."],
                     prompts=["Read the spoken and written examples aloud.", "Point to each Remember box item."],
                     timing="10 minutes for pages 13–14",
                     misconceptions=["Students may confuse : and :: — use the Remember box."]),
    TeacherPageNotes("Page 14 — Lesson 4: Four Common Analogy Relationships",
                     answers=["Cards match student page: Synonym, Antonym, Rhyming, Part-to-Whole."],
                     prompts=["Have students read one card aloud using “is to” and “as.”"],
                     timing="Included in 10-minute intro block"),
    TeacherPageNotes("Page 15 — Lesson 4: Analogy Practice",
                     answers=[
                         "1. unhappy : sad (Synonym)", "2. asleep : awake (Antonym)",
                         "3. look : book (Rhyming)", "4. page : book (Part-to-Whole)",
                         "Multiple choice: 1. cold   2. tall : short",
                     ],
                     alternates=["For #3, also accept: cook, hook if relationship is labeled Rhyming."],
                     timing="15–20 minutes"),
    TeacherPageNotes("Page 16 — Lesson 4: Vocabulary and Analogy Example",
                     answers=[
                         "Example analogy relationship: Synonym (source: encourage : cheer :: easy : simple).",
                         "Vocabulary fields: teacher-assigned — answers will vary.",
                     ]),
    TeacherPageNotes("Page 17 — Lesson 4: Create-Your-Own Analogies",
                     answers=["Student-created analogies will vary — check that each has a labeled relationship."],
                     prompts=["Share one analogy with a partner and explain the relationship."]),
    TeacherPageNotes("Reference — Capitalization and Punctuation Reference",
                     answers=["Official Shurley reference section — student and teacher pages match."],
                     procedures=[
                         "Place this reference immediately before Lesson 5. "
                         "Direct students to use it during Lessons 5 and 6 editing practice.",
                     ]),
    TeacherPageNotes("Reference 9 — Punctuation Rules",
                     answers=["Protected source page — punctuation rules 1–13 embedded as image."],
                     procedures=["Content embedded from official PDF page 1. Do not alter rule wording or examples."]),
    TeacherPageNotes("Reference 7 — Capitalization Rules",
                     answers=["Protected source page — capitalization rules 1–8 embedded as image."],
                     procedures=["Content embedded from official PDF page 2. Do not alter rule wording or examples."]),
    TeacherPageNotes("Page 20 — Lesson 5: Vocabulary and Analogy Example",
                     answers=[
                         "Example analogy relationship: Part-to-Whole (source: fraction : whole :: wing : bird).",
                         "Vocabulary: teacher-assigned — answers will vary.",
                     ]),
    TeacherPageNotes("Page 21 — Lesson 5: Capitalization Practice",
                     answers=[
                         "Passage 1 capitals: My, I, Amy, Ford's, Theater, Friday, Nim's, Island",
                         "Passage 2 capitals: My, Reagan, Beth, Main, Street, July",
                     ],
                     misconceptions=["Students may capitalize common nouns like 'friends' or 'night.'"]),
    TeacherPageNotes("Page 22 — Lesson 5: Editing — Capitals",
                     answers=[
                         "1. We drove to Lake Michigan on Saturday with Mrs. Daniels.",
                         "2. Yes, Sam and I work on Saturdays at Quickfill Gas on Jasper Road in Denver.",
                     ]),
    TeacherPageNotes("Page 23 — Lesson 6: Vocabulary and Analogy Example",
                     answers=[
                         "Example analogy relationship: Part-to-Whole (source: individual : community :: bird : flock).",
                         "Vocabulary: teacher-assigned — answers will vary.",
                     ]),
    TeacherPageNotes("Page 24 — Lesson 6: Capitalization and Punctuation",
                     answers=["Sample observations: question mark/end mark, commas in a list, proper nouns capitalized."]),
    TeacherPageNotes("Page 25 — Lesson 6: Editing — Mixed Skills",
                     answers=[
                         "1. Yes, Mr. Green will move to Denver, Colorado, on June 18, 2024.",
                         "2. Did your teacher, Ms. Coleman, read Charlotte's Web to your class today?",
                     ],
                     alternates=["Also accept exclamation mark on Sentence 1 if student treats 'Yes' as strong emotion."]),
    TeacherPageNotes("Page 26 — In-Class Chapter Review",
                     answers=["See In-Class Chapter Review Key for full review answers."],
                     procedures=["Use as an end-of-chapter classroom activity. Do not assign as homework or test prep."],
                     timing="25–35 minutes in class"),
]


REFERENCE_PAGE_BUILDERS = frozenset({page_ref_intro, page_ref_punctuation, page_ref_capitalization})
MIRROR_STUDENT_LAYOUT_BUILDERS = REFERENCE_PAGE_BUILDERS | frozenset({page_l4a, page_l4a2})

STUDENT_PAGES = [
    page_cover, page_l1a, page_l1b, page_l2a, page_l2b, page_l2b2, page_l2c, page_l2d, page_l2e,
    page_l3a, page_l3b, page_l3c, page_l4a, page_l4a2, page_l4b, page_l4c, page_l4d,
    page_ref_intro, page_ref_punctuation, page_ref_capitalization,
    page_l5a, page_l5a2, page_l5b, page_l6a, page_l6a2, page_l6b, page_review,
]


def build_student_packet():
    doc = Document()
    for i, builder in enumerate(STUDENT_PAGES, 1):
        section = doc.sections[0] if i == 1 else doc.add_section()
        set_margins(section)
        add_page_footer(section, i)
        builder(doc)
    return doc, len(STUDENT_PAGES)


def build_teacher_edition():
    doc = Document()
    for i, (builder, notes) in enumerate(zip(STUDENT_PAGES, TEACHER_NOTES), 1):
        section = doc.sections[0] if i == 1 else doc.add_section()
        set_margins(section)
        add_page_footer(section, i)
        if i == 1:
            add_para(doc, "Chapter 1 — Shurley Packet", bold=True, size=20, align=WD_ALIGN_PARAGRAPH.CENTER)
            add_para(doc, "Teacher Edition", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
        if builder in MIRROR_STUDENT_LAYOUT_BUILDERS:
            builder(doc)
            if builder is page_ref_intro:
                add_teacher_answer_block(doc, notes)
        else:
            add_teacher_answer_block(doc, notes)
    return doc, len(TEACHER_NOTES)


def build_review():
    doc = Document()
    set_margins(doc.sections[0], t=0.6, b=0.6, l=0.6, r=0.6)
    add_para(doc, "Chapter 1 — In-Class Chapter Review", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_body(doc, "Name: _________________     Date: _________________")
    add_body(doc, "Complete this review in class. Work with a partner when your teacher says to do so.", italic=True, space_after=10)
    add_review_content(doc)
    add_page_break(doc)
    section = doc.add_section()
    set_margins(section, t=0.6, b=0.6, l=0.6, r=0.6)
    add_para(doc, "Chapter 1 — In-Class Chapter Review (continued)", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_body(doc, "Name: _________________", space_after=8)
    add_review_content_page2(doc)
    add_teacher_check(doc)
    return doc


def build_review_key():
    doc = Document()
    set_margins(doc.sections[0], t=0.6, b=0.6, l=0.6, r=0.6)
    add_para(doc, "Chapter 1 — In-Class Chapter Review Key", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    page1 = [
        ("Part A — Complete Sentences", "Capital letter, End mark, Complete sense, Subject, Verb"),
        ("Part B — Vocabulary", "encourage = C   magnify = D   community = B   fraction = A"),
        ("Part C — Synonyms and Antonyms",
         "1. have almost the same meanings\n2. have opposite meanings\n3. hot/warm = Synonym; run/walk = Antonym"),
    ]
    for title, ans in page1:
        add_heading(doc, title)
        for line in ans.split("\n"):
            add_para(doc, line, bold=True, color=ANSWER_BLUE, space_after=3)
    add_page_break(doc)
    section = doc.add_section()
    set_margins(section, t=0.6, b=0.6, l=0.6, r=0.6)
    add_para(doc, "Chapter 1 — In-Class Chapter Review Key (continued)", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    page2 = [
        ("Part D — Analogy Relationships",
         "1. Synonym, Antonym, Rhyming, Part-to-Whole\n2. Synonym\n3. Part-to-Whole (Forest)"),
        ("Part E — Analogy Practice",
         "4. hot : cold (Antonym)\n5. paw : dog (Part-to-Whole)"),
        ("Part F — Capitalization and Punctuation",
         "Kevin asked Bobby, Bill, and Tonya to his birthday party."),
    ]
    for title, ans in page2:
        add_heading(doc, title)
        for line in ans.split("\n"):
            add_para(doc, line, bold=True, color=ANSWER_BLUE, space_after=3)
    return doc


def main():
    for path in (REF_PUNCT_IMG, REF_CAP_IMG, REF_SOURCE_PDF):
        if not path.exists():
            raise FileNotFoundError(f"Missing protected reference asset: {path}")
    assert len(TEACHER_NOTES) == len(STUDENT_PAGES), (
        f"Teacher notes ({len(TEACHER_NOTES)}) must match student pages ({len(STUDENT_PAGES)})"
    )
    outputs = [
        (STUDENT_OUT, *build_student_packet()),
        (TEACHER_OUT, *build_teacher_edition()),
        (REVIEW_OUT, build_review(), 2),
        (REVIEW_KEY_OUT, build_review_key(), 2),
    ]
    for path, document, page_count in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        document.save(str(path))
        print(f"Created: {path} ({page_count} pages)")


if __name__ == "__main__":
    main()
