#!/usr/bin/env python3
"""Generate Chapter 1 Guided Notes Redesign packet (Lessons 3–6, 16–18 pages)."""

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

TARGET_PAGES_MIN = 16
TARGET_PAGES_MAX = 18

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
    ("giggle : chuckle :: unhappy : ___________", "Synonym", ["sad"]),
    ("fire : ice :: asleep : ___________", "Antonym", ["awake"]),
    ("hat : cat :: __________ : book", "Rhyming", ["look", "cook", "hook"]),
    ("tree : forest :: page : ___________", "Part-to-Whole", ["book"]),
]

VOCAB_WORDS = [
    ("encourage", "to cheer on"),
    ("magnify", "to make something appear larger"),
    ("community", "a town or group of people"),
    ("fraction", "a part of a whole number"),
]

ANSWER_BLUE = RGBColor(0x1F, 0x4E, 0x79)
NOTE_GRAY = RGBColor(0x66, 0x66, 0x66)
CORRECTION_RED = RGBColor(0xB9, 0x1C, 0x1C)


@dataclass
class TeacherPageNotes:
    title: str
    answers: list[str] = field(default_factory=list)
    alternates: list[str] = field(default_factory=list)
    prompts: list[str] = field(default_factory=list)
    timing: str = ""
    misconceptions: list[str] = field(default_factory=list)
    procedures: list[str] = field(default_factory=list)
    correction_points: list[str] = field(default_factory=list)


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


def add_drawing_box(doc, lines=6):
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


def add_lesson_banner(doc, num, title):
    add_para(doc, f"Chapter 1 — Lesson {num}", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_para(doc, title, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)


def add_page_title(doc, title, subtitle=None):
    add_para(doc, title, bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    if subtitle:
        add_para(doc, subtitle, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)


def add_section_separator(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)
    p_pr = p._element.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "CCCCCC")
    p_bdr.append(bottom)
    p_pr.append(p_bdr)


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
    doc.add_paragraph()


def add_analogy_relationship_cards(doc):
    table = doc.add_table(rows=2, cols=2)
    table.style = "Table Grid"
    table.autofit = False
    for row in table.rows:
        _set_row_height(row, 2800)
        for cell in row.cells:
            cell.width = Inches(3.35)
    for idx, (rel, analogy, explanation) in enumerate(ANALOGY_TYPES):
        r, c = divmod(idx, 2)
        _fill_analogy_card(table.rows[r].cells[c], rel, analogy, explanation)
    doc.add_paragraph()


def add_full_page_image(doc, image_path: Path, max_height_inches: float = 8.75, max_width_inches: float = 7.0):
    try:
        from PIL import Image
        im = Image.open(image_path)
        w, h = im.size
        height_in = max_height_inches
        width_in = height_in * (w / h)
        if width_in > max_width_inches:
            width_in = max_width_inches
            height_in = width_in * (h / w)
    except ImportError:
        width_in = max_width_inches
        height_in = max_height_inches

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run()
    run.add_picture(str(image_path), width=Inches(width_in), height=Inches(height_in))


def add_vocab_builder(doc):
    add_section_label(doc, "Vocabulary Builder")
    add_body(doc, "Choose a vocabulary word from the list. Complete every section below.")
    for word, meaning in VOCAB_WORDS:
        add_body(doc, f"• {word} — {meaning}", space_after=2)
    add_body(doc, "Word: _________________________________", space_before=8)
    add_blank_lines(doc, 2, "Definition:")
    add_blank_lines(doc, 1, "Synonym:")
    add_blank_lines(doc, 1, "Antonym:")
    add_blank_lines(doc, 2, "Your sentence:")
    add_body(doc, "Draw a memory picture:")
    add_drawing_box(doc, 5)


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
        add_section_label(doc, "Oral Prompts")
        for pr in notes.prompts:
            add_bullet(doc, pr)
    if notes.correction_points:
        add_section_label(doc, "Correction Points")
        for cp in notes.correction_points:
            add_para(doc, f"• {cp}", color=CORRECTION_RED, space_after=3)
    add_section_label(doc, "Expected Responses")
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


# ── Student pages (17 logical pages) ───────────────────────────────────────────

def page_cover(doc):
    add_para(doc, "Chapter 1", bold=True, size=22, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_para(doc, "Shurley Packet", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    add_body(doc, "Name: _________________________________")
    add_body(doc, "Date: _________________________________")
    add_body(doc, "Teacher: _______________________________")
    add_body(doc, "Draw a picture about something you are learning in Chapter 1:", space_before=12)
    add_drawing_box(doc, 8)


def page_l3_sentences(doc):
    add_lesson_banner(doc, 3, "Complete Sentences")
    add_section_label(doc, "Learn")
    add_body(doc, "What five things does a sentence need? (Hint: Sentence Jingle)")
    add_blank_lines(doc, 4)
    add_knowledge_box(doc, "Capital letter, End mark, Complete sense, Subject, and Verb.")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Check each part when you write:")
    for part in SENTENCE_PARTS:
        add_body(doc, f"☐  {part}")
    add_section_label(doc, "Apply")
    add_body(doc, "Write one complete sentence about your day. Check all five parts.")
    add_blank_lines(doc, 2)


def page_l3_syn_ant(doc):
    add_page_title(doc, "Synonyms and Antonyms", "Chapter 1 — Lesson 3")
    add_section_label(doc, "Learn")
    add_body(doc, "Synonyms are words with almost the same meaning.  Examples: noisy/loud, run/dash")
    add_body(doc, "Antonyms are words with opposite meanings.  Examples: night/day, run/walk")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Circle Synonym or Antonym for each pair:")
    for i, (pair, _) in enumerate(SYN_ANT, 1):
        add_body(doc, f"{i}.  {pair}          Synonym   or   Antonym")
    add_section_label(doc, "Practice Independently")
    add_body(doc, "Write one synonym pair and one antonym pair:")
    add_blank_lines(doc, 1, "Synonym pair:")
    add_blank_lines(doc, 1, "Antonym pair:")


def page_l3_vocab(doc):
    add_page_title(doc, "Vocabulary Builder", "Chapter 1 — Lesson 3")
    add_vocab_builder(doc)


def page_l4_intro(doc):
    add_lesson_banner(doc, 4, "Understanding Analogies")
    add_section_label(doc, "Learn")
    add_body(doc, "An analogy shows how two word pairs are related. It is a special word puzzle.", size=14)
    add_body(doc, "Spoken: boat is to goat as fan is to ___________.", size=16, space_after=8)
    add_body(doc, "Written: front : back :: top : ___________", size=16, space_after=8)
    add_analogy_remember_box(doc)
    add_section_label(doc, "Worked Example")
    add_body(doc, "front : back :: top : bottom", size=16)
    add_body(doc, "Both pairs are opposites — an antonym analogy.", italic=True)


def page_l4_relationships(doc):
    add_page_title(doc, "Four Analogy Relationships", "Chapter 1 — Lesson 4")
    add_body(doc, "Study each card. Read the example using “is to” and “as.”", italic=True, space_after=8)
    add_analogy_relationship_cards(doc)


def page_l4_practice(doc):
    add_page_title(doc, "Analogy Practice", "Chapter 1 — Lesson 4")
    add_section_label(doc, "Practice Together")
    for prompt, _, _ in ANALOGY_PRACTICE:
        add_body(doc, prompt)
        add_body(doc, "Relationship:  synonym   antonym   rhyming   part-to-whole")
        doc.add_paragraph()
    add_section_label(doc, "Practice Independently")
    add_body(doc, "1.  weak : strong :: hot : ________     (weather   cold   warm)")
    add_body(doc, "2.  mouse : house :: ______________     (sold : bold   tall : short)")


def page_ref_intro(doc):
    add_para(doc, "Capitalization and Punctuation Reference", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    add_body(doc, "Use this reference during Lessons 5 and 6.", italic=True, space_after=8)
    add_body(doc, "Reference 9 — Punctuation Rules (next page)")
    add_body(doc, "Reference 7 — Capitalization Rules (following page)")


def page_ref_punctuation(doc):
    add_full_page_image(doc, REF_PUNCT_IMG)


def page_ref_capitalization(doc):
    add_full_page_image(doc, REF_CAP_IMG)


def page_l5_capitalization(doc):
    add_lesson_banner(doc, 5, "Capitalization")
    add_section_label(doc, "Learn")
    add_knowledge_box(doc, "Proper nouns name specific people, places, or things. They begin with a capital letter.")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Write the capital letter above each word that needs one.")
    add_body(doc, "Passage 1:", bold=True)
    add_body(doc, "my friends and i will meet amy at the ford's theater on friday night to see nim's island.")
    add_blank_lines(doc, 2)
    add_body(doc, "Passage 2:", bold=True)
    add_body(doc, "my cousins, reagan and beth, went to the parade on main street in july.")
    add_blank_lines(doc, 2)


def page_l5_editing(doc):
    add_page_title(doc, "Capitalization Editing", "Chapter 1 — Lesson 5")
    add_section_label(doc, "Practice Independently")
    add_body(doc, "Mark capitals above mistakes. Rewrite each sentence correctly.")
    add_body(doc, "1. we drove to lake michigan on saturday with mrs. daniels.", bold=True)
    add_blank_lines(doc, 2, "Rewrite:")
    add_body(doc, "2. yes, sam and i work on saturdays at quickfill gas on jasper road in denver.", bold=True)
    add_blank_lines(doc, 2, "Rewrite:")


def page_l6_punctuation(doc):
    add_lesson_banner(doc, 6, "Punctuation")
    add_section_label(doc, "Learn")
    add_body(doc, "Sentences need correct end marks, commas, periods, question marks, exclamation marks, and apostrophes.")
    add_section_label(doc, "Practice Together")
    add_body(doc, "Read each model sentence. Notice the capitals, commas, and end marks.")
    add_body(doc, "1. May I walk to Central Park with Jeff, Lonny, and Tina?")
    add_body(doc, "2. Class, I would like you to meet Ally Mona, our new student.")
    add_blank_lines(doc, 1, "What did you notice?")


def page_l6_editing(doc):
    add_page_title(doc, "Editing Practice", "Chapter 1 — Lesson 6")
    add_section_label(doc, "Practice Independently")
    add_body(doc, "Correct capitals and punctuation. Rewrite each sentence.")
    add_body(doc, "1. yes mr green will move to denver colorado on june 18 2024", bold=True)
    add_blank_lines(doc, 2, "Rewrite:")
    add_body(doc, "2. did your teacher ms coleman read charlottes web to your class today", bold=True)
    add_blank_lines(doc, 2, "Rewrite:")


def add_review_page1(doc):
    add_para(doc, "Chapter 1 — Review", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_body(doc, "Name: _________________     Date: _________________", space_after=8)
    add_section_label(doc, "Part A — Complete Sentences")
    add_body(doc, "Name the five parts of a complete sentence:")
    add_blank_lines(doc, 1)
    add_section_label(doc, "Part B — Vocabulary")
    add_body(doc, "Match each word to its meaning. Write the letter.")
    for i, (word, _) in enumerate(VOCAB_WORDS):
        letter = chr(65 + i)
        add_body(doc, f"____ {word}")
    add_body(doc, "A. to cheer on    B. to make something appear larger")
    add_body(doc, "C. a town or group of people    D. a part of a whole number")
    add_section_label(doc, "Part C — Synonyms and Antonyms")
    add_body(doc, "1. Synonyms are words that _______________________________.")
    add_body(doc, "2. Antonyms are words that _______________________________.")
    add_body(doc, "3. hot/warm = Synonym or Antonym?     run/walk = Synonym or Antonym?")


def add_review_page2(doc):
    add_section_label(doc, "Part D — Analogy Relationships")
    add_body(doc, "1. List the four analogy relationship types:")
    add_blank_lines(doc, 1)
    add_body(doc, "2. Nice : Kind :: Mad : Angry   (relationship: ___________)")
    add_body(doc, "3. Finger : Hand :: Tree : ___________   (relationship: ___________)")
    add_section_label(doc, "Part E — Analogy Practice")
    add_body(doc, "4. big : small :: hot : ___________   (relationship: ___________)")
    add_body(doc, "5. leaf : tree :: paw : ___________   (relationship: ___________)")
    add_section_label(doc, "Part F — Editing")
    add_body(doc, "Rewrite correctly: kevin asked bobby bill and tonya to his birthday party")
    add_blank_lines(doc, 1)


def page_review1(doc):
    add_review_page1(doc)


def page_review2(doc):
    add_review_page2(doc)


def page_enrichment(doc):
    add_page_title(doc, "Application and Enrichment", "Chapter 1 — Optional")
    add_section_label(doc, "Create Your Own")
    add_body(doc, "Write two analogies of your own. Label each relationship.")
    add_blank_lines(doc, 1, "1.")
    add_blank_lines(doc, 1, "2.")
    add_section_separator(doc)
    add_section_label(doc, "Apply")
    add_body(doc, "Write a complete sentence using your vocabulary word. Check all five sentence parts.")
    add_blank_lines(doc, 2)


# ── Teacher notes (one per page) ───────────────────────────────────────────────

TEACHER_NOTES = [
    TeacherPageNotes("Page 1 — Cover",
                     answers=["Student illustration — no fixed answer."],
                     prompts=["What will you learn in Chapter 1?"]),
    TeacherPageNotes("Page 2 — Lesson 3: Complete Sentences",
                     answers=["Five parts: Capital letter, End mark, Complete sense, Subject, Verb."],
                     prompts=["Chant the Sentence Jingle.", "What part is missing if there is no end mark?"],
                     timing="12–15 minutes",
                     misconceptions=["Students list parts but don't apply them when writing."],
                     correction_points=["Capital must be first letter.", "Every sentence needs a subject and verb."]),
    TeacherPageNotes("Page 3 — Synonyms and Antonyms",
                     answers=["1.Antonym 2.Synonym 3.Synonym 4.Antonym 5.Synonym 6.Synonym 7.Antonym 8.Synonym"],
                     alternates=["Accept valid student-created pairs."],
                     prompts=["Say a synonym pair aloud.", "Say an antonym pair aloud."],
                     timing="12–15 minutes",
                     misconceptions=["Students confuse synonyms and antonyms."],
                     correction_points=["Synonym = almost same. Antonym = opposite."]),
    TeacherPageNotes("Page 4 — Vocabulary Builder",
                     answers=["Teacher-assigned word — answers vary."],
                     prompts=["Which word strategy helps you remember new vocabulary?"],
                     timing="15–20 minutes",
                     correction_points=["Sentence must use the word correctly.", "Drawing should connect to meaning."]),
    TeacherPageNotes("Page 5 — Lesson 4: Understanding Analogies",
                     answers=["Worked example: bottom (Antonym). Quick check: man (Rhyming)."],
                     prompts=["Read spoken and written examples aloud.", "Point to each Remember box item."],
                     timing="10 minutes",
                     misconceptions=["Students confuse : and ::."],
                     correction_points=["Use Remember box for symbol meanings."]),
    TeacherPageNotes("Page 6 — Four Analogy Relationships",
                     answers=["Cards: Synonym, Antonym, Rhyming, Part-to-Whole."],
                     prompts=["Read one card using “is to” and “as.”"],
                     timing="10 minutes"),
    TeacherPageNotes("Page 7 — Analogy Practice",
                     answers=[
                         "1. sad (Synonym)", "2. awake (Antonym)", "3. look/cook/hook (Rhyming)", "4. book (Part-to-Whole)",
                         "MC: 1. cold   2. tall : short",
                     ],
                     alternates=["For #3 accept cook or hook if labeled Rhyming."],
                     timing="15–20 minutes",
                     correction_points=["Each answer must match the labeled relationship."]),
    TeacherPageNotes("Reference — Capitalization and Punctuation Reference",
                     answers=["Official reference — pages match student edition."],
                     procedures=["Direct students to use during Lessons 5 and 6."]),
    TeacherPageNotes("Reference 9 — Punctuation Rules",
                     answers=["Protected embedded image — rules 1–13."],
                     procedures=["Do not alter rule wording."]),
    TeacherPageNotes("Reference 7 — Capitalization Rules",
                     answers=["Protected embedded image — rules 1–8."],
                     procedures=["Do not alter rule wording."]),
    TeacherPageNotes("Page 11 — Lesson 5: Capitalization",
                     answers=[
                         "Passage 1: My, I, Amy, Ford's, Theater, Friday, Nim's, Island",
                         "Passage 2: My, Reagan, Beth, Main, Street, July",
                     ],
                     misconceptions=["Students capitalize common nouns like 'friends' or 'night'."],
                     correction_points=["Only proper nouns get capitals."]),
    TeacherPageNotes("Page 12 — Capitalization Editing",
                     answers=[
                         "1. We drove to Lake Michigan on Saturday with Mrs. Daniels.",
                         "2. Yes, Sam and I work on Saturdays at Quickfill Gas on Jasper Road in Denver.",
                     ],
                     timing="15 minutes"),
    TeacherPageNotes("Page 13 — Lesson 6: Punctuation",
                     answers=["Model 1: question mark, commas in list, proper nouns capitalized.",
                              "Model 2: comma after direct address, proper noun capitalized."],
                     prompts=["What end mark does a question need?"],
                     timing="10 minutes"),
    TeacherPageNotes("Page 14 — Editing Practice",
                     answers=[
                         "1. Yes, Mr. Green will move to Denver, Colorado, on June 18, 2024.",
                         "2. Did your teacher, Ms. Coleman, read Charlotte's Web to your class today?",
                     ],
                     alternates=["Accept ! on Sentence 1 if student treats 'Yes' as strong emotion."],
                     correction_points=["Count capitals, commas, end marks, apostrophe before accepting."]),
    TeacherPageNotes("Page 15 — Chapter Review (Part 1)",
                     answers=["See review key for full answers."],
                     procedures=["Use as in-class activity — not homework."],
                     timing="15 minutes (Part 1)"),
    TeacherPageNotes("Page 16 — Chapter Review (Part 2)",
                     answers=["See review key for full answers."],
                     timing="15 minutes (Part 2)"),
    TeacherPageNotes("Page 17 — Application and Enrichment (Optional)",
                     answers=["Student analogies and sentences will vary — check labeled relationships and five sentence parts."],
                     prompts=["Share one analogy with a partner."],
                     timing="10–15 minutes optional"),
]

MIRROR_LAYOUT = frozenset({
    page_l4_intro, page_l4_relationships, page_ref_intro, page_ref_punctuation, page_ref_capitalization,
})

STUDENT_PAGES = [
    page_cover,
    page_l3_sentences, page_l3_syn_ant, page_l3_vocab,
    page_l4_intro, page_l4_relationships, page_l4_practice,
    page_ref_intro, page_ref_punctuation, page_ref_capitalization,
    page_l5_capitalization, page_l5_editing,
    page_l6_punctuation, page_l6_editing,
    page_review1, page_review2,
    page_enrichment,
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
        if builder in MIRROR_LAYOUT:
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
    add_body(doc, "Name: _________________     Date: _________________", space_after=8)
    add_body(doc, "Complete in class with your teacher's directions.", italic=True, space_after=10)
    add_review_page1(doc)
    add_page_break(doc)
    section = doc.add_section()
    set_margins(section, t=0.6, b=0.6, l=0.6, r=0.6)
    add_para(doc, "Chapter 1 — In-Class Chapter Review (continued)", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_review_page2(doc)
    return doc


def build_review_key():
    doc = Document()
    set_margins(doc.sections[0], t=0.6, b=0.6, l=0.6, r=0.6)
    add_para(doc, "Chapter 1 — In-Class Chapter Review Key", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    page1 = [
        ("Part A — Complete Sentences", "Capital letter, End mark, Complete sense, Subject, Verb"),
        ("Part B — Vocabulary", "encourage=C  magnify=D  community=B  fraction=A"),
        ("Part C — Synonyms and Antonyms",
         "1. have almost the same meanings\n2. have opposite meanings\n3. hot/warm=Synonym; run/walk=Antonym"),
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
        ("Part F — Editing",
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
        print(f"Created: {path} ({page_count} logical pages)")


if __name__ == "__main__":
    main()
