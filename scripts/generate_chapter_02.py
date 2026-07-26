#!/usr/bin/env python3
"""Generate Chapter 2 Gold Standard Shurley Packet system."""

from __future__ import annotations

from dataclasses import dataclass, field
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BLUEPRINT_IMG = ROOT / "source-materials/chapter-02/visuals/Mastering_the_Sentence_Blueprint.png"
CORE_FIVE_IMG = ROOT / "source-materials/chapter-02/visuals/Core_Five_English_Grammar_Guide.png"
REF_SOURCE_PDF = ROOT / "source-materials/reference/shurley-capitalization-punctuation-reference.pdf"

STUDENT_OUT = ROOT / "packets/student/chapter-02/chapter-02-shurley-packet.docx"
TEACHER_OUT = ROOT / "packets/teacher-keys/chapter-02/chapter-02-shurley-packet-teacher-edition.docx"
REVIEW_OUT = ROOT / "packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review.docx"
REVIEW_KEY_OUT = ROOT / "packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review-key.docx"

ANSWER_BLUE = RGBColor(0x1F, 0x4E, 0x79)
NOTE_GRAY = RGBColor(0x66, 0x66, 0x66)
MONO = "Courier New"


@dataclass
class ClassifiedSentence:
    """Display-order tokens; labels only for words present (U-03)."""

    tokens: list[tuple[str, str]]
    sentence_type: str | None = None
    divide: bool = False

    @property
    def words(self) -> list[str]:
        return [w for w, _ in self.tokens]

    @property
    def labels(self) -> list[str]:
        return [lb for _, lb in self.tokens]

    def display_text(self) -> str:
        return " ".join(self.words)


def cs(*pairs: tuple[str, str], sentence_type: str | None = None, divide: bool = False) -> ClassifiedSentence:
    return ClassifiedSentence(list(pairs), sentence_type=sentence_type, divide=divide)


# ── Classification keys (TM / lesson-script-map; display word order) ───────────

CLASSIFICATION_KEYS: dict[str, ClassifiedSentence] = {
    "l1_s": cs(("Ships", "SN"), ("sailed.", "V")),
    "l1_1": cs(("Plane", "SN"), ("flew.", "V")),
    "l1_2": cs(("Ladybugs", "SN"), ("crawled.", "V")),
    "l1_3": cs(("Boys", "SN"), ("raced.", "V")),
    "l2_s": cs(("Ships", "SN"), ("sailed", "V"), ("slowly", "Adv"), ("away", "Adv"), ("today.", "Adv")),
    "l2_1": cs(("Planes", "SN"), ("flew.", "V")),
    "l2_2": cs(("Planes", "SN"), ("flew", "V"), ("quickly", "Adv"), ("away", "Adv"), ("today.", "Adv")),
    "l2_3": cs(("Spiders", "SN"), ("crawled", "V"), ("around", "Adv"), ("very", "Adv"), ("quickly.", "Adv")),
    "l3_1": cs(("Bees", "SN"), ("buzzed", "V"), ("angrily", "Adv"), ("around", "Adv"), ("today.", "Adv")),
    "l3_2": cs(("Rabbits", "SN"), ("hopped", "V"), ("around", "Adv"), ("everywhere.", "Adv")),
    "l3_3": cs(("Anthony", "SN"), ("listened", "V"), ("very", "Adv"), ("carefully", "Adv"), ("yesterday.", "Adv")),
    "l4_s": cs(("Those", "Adj"), ("five", "Adj"), ("cargo", "Adj"), ("ships", "SN"), ("sailed", "V"),
               ("slowly", "Adv"), ("away", "Adv"), ("today.", "Adv")),
    "l4_1": cs(("That", "Adj"), ("owl", "SN"), ("flew", "V"), ("silently.", "Adv")),
    "l4_2": cs(("That", "Adj"), ("large", "Adj"), ("white", "Adj"), ("owl", "SN"), ("flew", "V"),
               ("silently", "Adv"), ("overhead", "Adv"), ("tonight.", "Adv")),
    "l4_3": cs(("Several", "Adj"), ("little", "Adj"), ("red", "Adj"), ("ladybugs", "SN"), ("crawled", "V"),
               ("everywhere", "Adv"), ("yesterday.", "Adv")),
    "l5_s": cs(("The", "A"), ("five", "Adj"), ("cargo", "Adj"), ("ships", "SN"), ("sailed", "V"),
               ("slowly", "Adv"), ("away.", "Adv")),
    "l5_1": cs(("The", "A"), ("girls", "SN"), ("giggled", "V"), ("loudly.", "Adv")),
    "l5_2": cs(("The", "A"), ("four", "Adj"), ("happy", "Adj"), ("girls", "SN"), ("giggled", "V"),
               ("loudly", "Adv"), ("today.", "Adv")),
    "l5_3": cs(("A", "A"), ("huge", "Adj"), ("whale", "SN"), ("swam", "V"), ("very", "Adv"),
               ("slowly", "Adv"), ("away.", "Adv")),
    "l6_1": cs(("The", "A"), ("nice", "Adj"), ("young", "Adj"), ("doctor", "SN"), ("spoke", "V"),
               ("very", "Adv"), ("kindly", "Adv"), ("today.", "Adv")),
    "l6_2": cs(("A", "A"), ("little", "Adj"), ("yellow", "Adj"), ("duck", "SN"), ("waddled", "V"),
               ("slowly", "Adv"), ("away.", "Adv")),
    "l6_3": cs(("An", "A"), ("enormous", "Adj"), ("black", "Adj"), ("bug", "SN"), ("flew", "V"),
               ("around", "Adv"), ("today.", "Adv")),
    "l7_s": cs(("The", "A"), ("two", "Adj"), ("pirate", "Adj"), ("ships", "SN"), ("appeared", "V"),
               ("quite", "Adv"), ("suddenly!", "Adv"), sentence_type="E", divide=True),
    "l7_1": cs(("The", "A"), ("music", "SN"), ("played", "V"), ("softly.", "Adv"), sentence_type="D", divide=True),
    "l7_2": cs(("The", "A"), ("very", "Adv"), ("soothing", "Adj"), ("music", "SN"), ("played", "V"),
               ("softly", "Adv"), ("tonight.", "Adv"), sentence_type="D", divide=True),
    "l7_3": cs(("Several", "Adj"), ("urgent", "Adj"), ("messages", "SN"), ("arrived", "V"), ("very", "Adv"),
               ("early", "Adv"), ("today.", "Adv"), sentence_type="D", divide=True),
    "l8_1": cs(("A", "A"), ("young", "Adj"), ("reporter", "SN"), ("glanced", "V"), ("curiously", "Adv"),
               ("around.", "Adv"), sentence_type="D", divide=True),
    "l8_2": cs(("The", "A"), ("stormy", "Adj"), ("winter", "Adj"), ("sky", "SN"), ("darkened", "V"),
               ("suddenly!", "Adv"), sentence_type="E", divide=True),
    "l8_3": cs(("An", "A"), ("extremely", "Adv"), ("frightened", "Adj"), ("girl", "SN"), ("screamed", "V"),
               ("very", "Adv"), ("loudly!", "Adv"), sentence_type="E", divide=True),
    "l9_1": cs(("Two", "Adj"), ("beautiful", "Adj"), ("butterflies", "SN"), ("flew", "V"), ("slowly", "Adv"),
               ("away.", "Adv"), sentence_type="D", divide=True),
    "l9_2": cs(("An", "A"), ("old", "Adj"), ("teapot", "SN"), ("whistled", "V"), ("very", "Adv"),
               ("loudly", "Adv"), ("today.", "Adv"), sentence_type="D", divide=True),
    "l9_3": cs(("Several", "Adj"), ("angry", "Adj"), ("bees", "SN"), ("circled", "V"), ("around", "Adv"),
               ("nearby!", "Adv"), sentence_type="E", divide=True),
}

AAN_DRILL = [
    ("____ tall tree.", "a"),
    ("____ unhappy baby.", "an"),
    ("____ flying owl. / ____ owl.", "a / a"),
    ("Did you find ____ oily cloth in the garage?", "an"),
    ("Would you like ____ fresh peach?", "a"),
    ("We saw ____ large animal yesterday.", "a"),
    ("We saw ____ anteater at the zoo yesterday.", "an"),
    ("We saw ____ movie yesterday.", "a"),
    ("We saw ____ exciting movie yesterday.", "an"),
]

REVIEW_ITEMS = [
    ("review_1", "1. Plane flew.", "l1_1"),
    ("review_2", "2. Boys raced.", "l1_3"),
    ("review_3", "3. The music played softly.", "l7_1"),
    ("review_4", "4. The stormy winter sky darkened suddenly!", "l8_2"),
    ("review_fill_adv", "Adverb questions (write all three):", None),
    ("review_fill_adj", "Adjective questions (write all three):", None),
    ("review_aan_1", "5. ____ unhappy baby.", "aan_an"),
    ("review_aan_2", "6. We saw ____ anteater at the zoo yesterday.", "aan_an2"),
    ("review_analogy", "7. soothing : smoothing :: flying : trying", "analogy_rhyming"),
]

AAN_KEY = {"aan_an": "an", "aan_an2": "an", "analogy_rhyming": "rhyming"}


@dataclass
class TeacherPageNotes:
    title: str
    answers: list[str] = field(default_factory=list)
    alternates: list[str] = field(default_factory=list)
    prompts: list[str] = field(default_factory=list)
    timing: str = ""
    misconceptions: list[str] = field(default_factory=list)
    procedures: list[str] = field(default_factory=list)
    classifications: list[str] = field(default_factory=list)


# ── Document helpers ─────────────────────────────────────────────────────────

def set_margins(section, t=0.75, b=0.75, l=0.75, r=0.75):
    section.top_margin = Inches(t)
    section.bottom_margin = Inches(b)
    section.left_margin = Inches(l)
    section.right_margin = Inches(r)


def style_run(run, size=13, bold=False, italic=False, color=None, mono=False):
    run.font.name = MONO if mono else "Calibri"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), MONO if mono else "Calibri")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color


def add_run(p, text, **kw):
    run = p.add_run(text)
    style_run(run, **kw)
    return run


def add_para(doc, text="", bold=False, italic=False, size=13, align=None, space_after=6, space_before=0, color=None, mono=False):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    if text:
        add_run(p, text, size=size, bold=bold, italic=italic, color=color, mono=mono)
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
    section.footer.is_linked_to_previous = False
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
    """Cover-page drawing area (paragraph-border style)."""
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
        lp = doc.add_paragraph()
        lp.paragraph_format.space_after = Pt(10)


def _set_row_height(row, twips: int):
    tr_pr = row._tr.get_or_add_trPr()
    tr_height = OxmlElement("w:trHeight")
    tr_height.set(qn("w:val"), str(twips))
    tr_height.set(qn("w:hRule"), "atLeast")
    tr_pr.append(tr_height)


def _set_cell_width(cell, width_inches: float):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_w = OxmlElement("w:tcW")
    tc_w.set(qn("w:w"), str(int(width_inches * 1440)))
    tc_w.set(qn("w:type"), "dxa")
    tc_pr.append(tc_w)


def _set_cell_no_wrap(cell):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_pr.append(OxmlElement("w:noWrap"))


def _set_cell_borders(cell, color="999999", size="8"):
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), size)
        b.set(qn("w:space"), "0")
        b.set(qn("w:color"), color)
        borders.append(b)
    tc_pr.append(borders)


def add_fixed_drawing_area(doc, height_inches: float = 1.2):
    """Fixed-height bordered box for vocabulary memory pictures (L7/L8)."""
    table = doc.add_table(rows=1, cols=1)
    table.autofit = False
    row = table.rows[0]
    cell = row.cells[0]
    _set_row_height(row, int(height_inches * 1440))
    _set_cell_width(cell, 6.5)
    _set_cell_borders(cell)
    cell.text = ""
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(6)


def add_full_page_image(doc, image_path: Path, max_height=8.0, max_width=7.0):
    try:
        from PIL import Image
        im = Image.open(image_path)
        w, h = im.size
        height_in = max_height
        width_in = height_in * (w / h)
        if width_in > max_width:
            width_in = max_width
            height_in = width_in * (h / w)
    except ImportError:
        width_in = max_width
        height_in = max_height
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(str(image_path), width=Inches(width_in), height=Inches(height_in))


def add_lesson_banner(doc, num, title, space_after=10):
    add_para(doc, f"Chapter 2 — Lesson {num}", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_para(doc, title, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=space_after)


def add_section_separator(doc):
    """Visual break between subsections sharing one printed page."""
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


def add_memory_check(doc, questions: list[str], teacher: bool = False, answers: list[str] | None = None):
    add_section_label(doc, "MEMORY CHECK")
    add_body(doc, "Without looking back, answer briefly:", italic=True, space_after=4)
    ans_list = answers or []
    for i, q in enumerate(questions):
        add_body(doc, q)
        if teacher and i < len(ans_list):
            add_para(doc, ans_list[i], bold=True, color=ANSWER_BLUE, size=11, space_after=4)
        else:
            add_blank_lines(doc, 1)


def add_teacher_learn_answers(doc, lines: list[str]):
    for line in lines:
        add_para(doc, line, bold=True, color=ANSWER_BLUE, size=11, space_after=2)


def add_teacher_aan_answers(doc):
    add_section_label(doc, "Model Answers — a or an")
    for item, ans in AAN_DRILL:
        add_para(doc, f"{item}  →  {ans}", bold=True, color=ANSWER_BLUE, size=11, space_after=1)


def add_teacher_margin(doc, notes: TeacherPageNotes | None):
    if not notes:
        return
    if notes.procedures:
        add_para(doc, notes.procedures[0], italic=True, color=NOTE_GRAY, size=10, space_before=4)
    if notes.alternates:
        add_para(doc, notes.alternates[0], italic=True, color=ANSWER_BLUE, size=10, space_after=2)


def add_teacher_check(doc):
    add_section_label(doc, "TEACHER CHECK")
    add_body(doc, "Complete: □     Date: __________     Initials: ________", space_after=12)


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
    if notes.classifications:
        add_section_label(doc, "Classification Keys")
        for cid in notes.classifications:
            if cid in CLASSIFICATION_KEYS:
                render_classification(doc, CLASSIFICATION_KEYS[cid], answer=True)
            else:
                add_para(doc, cid, bold=True, color=ANSWER_BLUE, space_after=4)
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


# ── Classification engine (display order; U-03 partial patterns) ─────────────

def _cell_text(cell, text, bold=False, color=None, mono=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=10):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    add_run(p, text, size=size, bold=bold, color=color, mono=mono)


def _render_classification_table(
    doc,
    classified: ClassifiedSentence,
    *,
    answer: bool = False,
    compact: bool = False,
    label_prefix: str = "",
):
    """SN V / P1 table; labels above words; reserved no-wrap type column at end."""
    tokens = classified.tokens
    stype = classified.sentence_type
    token_count = len(tokens)
    if compact:
        font_size = 9
    elif token_count >= 7:
        font_size = 8
    else:
        font_size = 10
    tail_space = 3 if compact else 6
    cols = 1 + len(tokens) + (1 if stype else 0)
    table = doc.add_table(rows=2, cols=cols)
    table.autofit = False

    pattern_cell_top = table.rows[0].cells[0]
    pattern_cell_bot = table.rows[1].cells[0]
    _set_cell_width(pattern_cell_top, 0.55)
    _set_cell_width(pattern_cell_bot, 0.55)
    _set_cell_no_wrap(pattern_cell_top)
    _set_cell_no_wrap(pattern_cell_bot)
    _cell_text(pattern_cell_top, "SN V", bold=answer, color=ANSWER_BLUE if answer else None, size=font_size)
    _cell_text(pattern_cell_bot, "P1", bold=answer, color=ANSWER_BLUE if answer else None, size=font_size)

    verb_idx = next((i for i, (_, lb) in enumerate(tokens) if lb == "V"), None)

    for i, (word, label) in enumerate(tokens):
        col = i + 1
        top_cell = table.rows[0].cells[col]
        bot_cell = table.rows[1].cells[col]
        _set_cell_no_wrap(top_cell)
        _set_cell_no_wrap(bot_cell)
        display_word = word
        if classified.divide and verb_idx is not None and i == verb_idx:
            display_word = "| " + word
        _cell_text(top_cell, label, bold=answer, color=ANSWER_BLUE if answer else None, size=font_size)
        _cell_text(
            bot_cell,
            display_word,
            bold=answer,
            color=ANSWER_BLUE if answer else None,
            align=WD_ALIGN_PARAGRAPH.LEFT,
            size=font_size,
        )

    if stype:
        col = len(tokens) + 1
        type_top = table.rows[0].cells[col]
        type_bot = table.rows[1].cells[col]
        _set_cell_width(type_top, 0.55)
        _set_cell_width(type_bot, 0.55)
        _set_cell_no_wrap(type_top)
        _set_cell_no_wrap(type_bot)
        _cell_text(type_top, "type", bold=answer, color=ANSWER_BLUE if answer else None, size=font_size)
        _cell_text(type_bot, stype, bold=answer, color=ANSWER_BLUE if answer else None, size=font_size)

    if label_prefix:
        add_body(doc, label_prefix, space_before=4)
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(tail_space)


def render_classification(doc, classified: ClassifiedSentence, answer: bool = False, label_prefix: str = ""):
    """Render SN V / P1 table with labels above words; optional divide and sentence type."""
    _render_classification_table(doc, classified, answer=answer, compact=False, label_prefix=label_prefix)


def render_classification_compact(doc, classified: ClassifiedSentence):
    """Teacher inline key: tokens line; type reserved on right-aligned line below."""
    parts = "   ".join(f"{w}={lb}" for w, lb in classified.tokens)
    add_para(
        doc,
        f"SN V / P1   {parts}",
        bold=True,
        color=ANSWER_BLUE,
        size=9,
        mono=True,
        space_after=0,
    )
    if classified.sentence_type:
        stype = classified.sentence_type.replace(" ", "\u00a0")
        add_para(
            doc,
            f"type\u00a0{stype}",
            bold=True,
            color=ANSWER_BLUE,
            size=9,
            mono=True,
            align=WD_ALIGN_PARAGRAPH.RIGHT,
            space_after=3,
        )
    else:
        spacer = doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(3)


def add_classification_practice(doc, number: str, sentence: str, key_id: str | None = None, teacher: bool = False):
    add_body(doc, f"{number}___________ {sentence}", space_after=4)
    add_body(doc, "Classify this sentence. Label each word. Write SN V / P1.", italic=True, space_after=4)
    add_blank_lines(doc, 3)
    if teacher and key_id and key_id in CLASSIFICATION_KEYS:
        render_classification_compact(doc, CLASSIFICATION_KEYS[key_id])


def add_fill_line(doc, prompt: str, width=40):
    add_body(doc, f"{prompt}{'_' * width}")


def add_vocab_template(doc):
    add_section_label(doc, "Vocabulary & Analogy Words")
    add_fill_line(doc, "Word: ")
    add_blank_lines(doc, 2, "Definition:")
    add_fill_line(doc, "Synonym: ")
    add_fill_line(doc, "Antonym: ")
    add_blank_lines(doc, 2, "Sentence:")
    add_body(doc, "Draw a picture in the box to help you remember the word:")
    add_fixed_drawing_area(doc)


def add_analogy_block(doc, analogy: str):
    add_body(doc, f"Analogy:   {analogy}", space_before=6)
    add_body(doc, "Relationship:    synonym        antonym         rhyming        part-to-whole")
    add_blank_lines(doc, 1)


def add_chapter_review_section(doc):
    add_para(doc, "Chapter 2 — In-Class Chapter Review", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_body(doc, "Your teacher will use the separate In-Class Chapter Review during class.", italic=True, space_after=8)
    add_body(doc, "Skills to review: SN/V/P1 classification, full-pattern sentences, sentence types (D/Imp/Int/E), "
              "adverb and adjective questions, articles a/an, analogies, capitalization and punctuation (Chapter 1 Reference).")


# ── Student page builders (teacher=False mirrors for student; teacher=True adds keys) ──

def page_cover(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_para(doc, "Chapter 2", bold=True, size=22, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_para(doc, "Shurley Packet" + (" — Teacher Edition" if teacher else ""), bold=True, size=18,
             align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    add_body(doc, "Name: _________________________________")
    add_body(doc, "Date: _________________________________")
    add_body(doc, "Draw a picture about sentence patterns you are learning:", space_before=12)
    add_drawing_box(doc, 8)
    add_teacher_margin(doc, notes)


def page_blueprint(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_para(doc, "The Sentence Blueprint", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    if CORE_FIVE_IMG.exists():
        add_full_page_image(doc, CORE_FIVE_IMG, max_height=3.2)
    add_section_label(doc, "Question and Answer Flow")
    add_body(doc, "Four Steps to Classify: Ask → Name → Identify → Label.", space_after=4)
    for label, qs in [
        ("SN", "Who? / What?"), ("V", "What is being said about the subject?"),
        ("Adv", "How? / When? / Where?"), ("Adj", "What kind? / Which one? / How many?"),
        ("A", "a, an, the (noun markers)"), ("P1", "SN V"),
    ]:
        add_bullet(doc, f"{label}: {qs}")
    add_teacher_margin(doc, notes)


def page_blueprint_2(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_para(doc, "The Sentence Blueprint (continued)", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    if BLUEPRINT_IMG.exists():
        add_full_page_image(doc, BLUEPRINT_IMG, max_height=3.5)
    add_section_label(doc, "Sentence Types (Lesson 7+)")
    for text in ["Declarative (D)", "Imperative (Imp)", "Interrogative (Int)", "Exclamatory (E)"]:
        add_bullet(doc, text)
    add_knowledge_box(doc, "The Divide: slash directly before the verb. Mover and Shaker: front-move + comma — not for classification.")
    add_teacher_margin(doc, notes)


def page_l1a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 1, "Nouns, Verbs, Pattern 1")
    add_section_label(doc, "Learn")
    add_body(doc, "What does a noun name?")
    for i in range(1, 5):
        add_fill_line(doc, f"{i}. ")
    if teacher:
        add_teacher_learn_answers(doc, ["person, place, thing, idea"])
    add_body(doc, "What are the subject questions?", space_before=4)
    add_fill_line(doc, "1. ")
    add_fill_line(doc, "2. ")
    if teacher:
        add_teacher_learn_answers(doc, ["Who?, What?"])
    add_body(doc, "A verb shows _______________ (called an _______________ verb) or "
              "__________________ (called a _________________ verb).", space_before=4)
    if teacher:
        add_teacher_learn_answers(doc, ["action / action verb; being / linking verb"])
    add_knowledge_box(doc, "Subject Noun first, then Verb. Declare: Subject Noun, Verb, Pattern 1.")
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "S. ", "Ships sailed.", "l1_s", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l1b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 1, "Nouns, Verbs, Pattern 1", space_after=6)
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "1. ", "Plane flew.", "l1_1", teacher=teacher)
    add_classification_practice(doc, "2. ", "Ladybugs crawled.", "l1_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "Boys raced.", "l1_3", teacher=teacher)
    add_memory_check(doc, ["What are the subject questions?", "What is Pattern 1?"],
                     teacher=teacher, answers=["Who?, What?", "Pattern 1 = SN V"] if teacher else None)
    add_teacher_margin(doc, notes)


def page_l1c(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 1, "Nouns, Verbs, Pattern 1", space_after=6)
    add_section_label(doc, "Apply")
    add_body(doc, "Write your own sentence using Pattern 1 (SN V):", bold=True)
    add_blank_lines(doc, 4)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l2b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 2, "Adverbs", space_after=6)
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "1. ", "Planes flew.", "l2_1", teacher=teacher)
    add_classification_practice(doc, "2. ", "Planes flew quickly away today.", "l2_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "Spiders crawled around very quickly.", "l2_3", teacher=teacher)
    add_memory_check(doc, ["Name the three adverb questions.", "Name three things adverbs can modify."],
                     teacher=teacher, answers=["How?, When?, Where?", "verbs, adjectives, adverbs"] if teacher else None)
    add_teacher_margin(doc, notes)


def page_l2c(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 2, "Adverbs", space_after=6)
    add_section_label(doc, "Apply")
    add_body(doc, "Write your own sentence using SN V Adv Adv:", bold=True)
    add_blank_lines(doc, 4)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l4b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 4, "Adjectives", space_after=6)
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "1. ", "That owl flew silently.", "l4_1", teacher=teacher)
    add_classification_practice(doc, "2. ", "That large white owl flew silently overhead tonight.", "l4_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "Several little red ladybugs crawled everywhere yesterday.", "l4_3", teacher=teacher)
    add_memory_check(doc, ["Name the three adjective questions."],
                     teacher=teacher, answers=["What kind?, Which one?, How many?"] if teacher else None)
    add_teacher_margin(doc, notes)


def page_l4c(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 4, "Adjectives", space_after=6)
    add_section_label(doc, "Apply")
    add_body(doc, "Write your own sentence using Adj Adj SN V Adv Adv:", bold=True)
    add_blank_lines(doc, 4)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l3(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 3, "Adverb Practice + Sentence Blueprint")
    add_section_label(doc, "Learn")
    add_knowledge_box(doc, "Mover and Shaker: Move an adverb to the front of the sentence and put a comma after it.")
    add_body(doc, "Five parts of a complete sentence: subject, verb, complete sense, capital letter, end mark.")
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "1. ", "Bees buzzed angrily around today.", "l3_1", teacher=teacher)
    add_classification_practice(doc, "2. ", "Rabbits hopped around everywhere.", "l3_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "Anthony listened very carefully yesterday.", "l3_3", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l3b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 3, "Adverb Practice", space_after=6)
    add_section_label(doc, "Apply")
    add_body(doc, "Write your own sentence using SN V Adv Adv:", bold=True)
    add_blank_lines(doc, 4)
    add_memory_check(doc, ["What punctuation follows a Mover and Shaker adverb at the front?"],
                     teacher=teacher, answers=["comma"] if teacher else None)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l6a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 6, "Full-Pattern Classification")
    add_knowledge_box(doc, "Full pattern: A Adj Adj SN V Adv Adv — label only the words that are present.")
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "1. ", "The nice young doctor spoke very kindly today.", "l6_1", teacher=teacher)
    add_classification_practice(doc, "2. ", "A little yellow duck waddled slowly away.", "l6_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "An enormous black bug flew around today.", "l6_3", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l6b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 6, "Full-Pattern Classification", space_after=6)
    add_memory_check(doc, ["What is Pattern 1?", "Where do you place labels for words that are not in the sentence?"],
                     teacher=teacher, answers=["SN V", "Do not add empty labels — partial patterns only"] if teacher else None)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l7a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 7, "Sentence Types + Skill Check")
    add_vocab_template(doc)
    if teacher:
        add_para(doc, "Teacher-assigned word", bold=True, color=ANSWER_BLUE, size=11)
    add_teacher_margin(doc, notes)


def page_l7a2(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 7, "Sentence Types", space_after=6)
    add_analogy_block(doc, "soothing : smoothing :: flying : trying")
    if teacher:
        add_para(doc, "Relationship: rhyming", bold=True, color=ANSWER_BLUE, size=11)
    add_section_label(doc, "Learn")
    add_body(doc, "Declarative sentence makes a statement. It is labeled with a _______.")
    add_body(doc, "An imperative sentence gives a command. It is labeled with an ______.")
    add_body(doc, "An interrogative sentence asks a question. It is labeled with an ______.")
    add_body(doc, "An exclamatory sentence expresses strong feeling. It is labeled with an ______.")
    if teacher:
        add_teacher_learn_answers(doc, ["D", "Imp", "Int", "E"])
    add_teacher_margin(doc, notes)


def page_l8b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 8, "Noun Check", space_after=6)
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "1. ", "A young reporter glanced curiously around.", "l8_1", teacher=teacher)
    add_classification_practice(doc, "2. ", "The stormy winter sky darkened suddenly!", "l8_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "An extremely frightened girl screamed very loudly!", "l8_3", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l8c(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 8, "Noun Check", space_after=6)
    add_memory_check(doc, ["What does a Noun Check confirm?", "Give one intensifier word."],
                     teacher=teacher, answers=["Subject noun is a noun", "very (also extremely, quite)"] if teacher else None)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l9a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 9, "Practice + Capitalization/Punctuation")
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "1. ", "Two beautiful butterflies flew slowly away.", "l9_1", teacher=teacher)
    add_classification_practice(doc, "2. ", "An old teapot whistled very loudly today.", "l9_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "Several angry bees circled around nearby!", "l9_3", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l9b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 9, "Capitalization/Punctuation")
    add_section_label(doc, "Using Capitalization and Punctuation Rules")
    add_body(doc, "Use your Chapter 1 Capitalization and Punctuation Reference.")
    add_body(doc, "Write the rule numbers for each correction in bold in the sentence below:", space_after=6)
    add_body(doc, "No, Alex did not go home with John during carpool on Friday.", bold=True, space_after=4)
    add_body(doc, "Corrections to mark: N, comma, A, J, F, period.", italic=True)
    add_blank_lines(doc, 4)
    if teacher:
        add_para(doc, "Rule numbers: Verify against protected reference.", bold=True, color=ANSWER_BLUE, size=11)
        add_para(doc, "Bold corrections: N, comma, A, J, F, period.", bold=True, color=ANSWER_BLUE, size=11)
    add_memory_check(doc, ["Where is the Chapter 1 reference for capitalization and punctuation rules?"],
                     teacher=teacher, answers=["Chapter 1 Capitalization and Punctuation Reference"] if teacher else None)
    add_teacher_check(doc)
    add_chapter_review_section(doc)
    add_teacher_margin(doc, notes)


def page_l2a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 2, "Adverbs")
    add_section_label(doc, "Learn")
    add_body(doc, "What are the adverb questions?")
    add_fill_line(doc, "1. ")
    add_fill_line(doc, "2. ")
    add_fill_line(doc, "3. ")
    if teacher:
        add_teacher_learn_answers(doc, ["How?, When?, Where?"])
    add_body(doc, "What does an adverb modify?", space_before=4)
    for i in range(1, 4):
        add_fill_line(doc, f"{i}. ")
    add_fill_line(doc, "It is labeled with the abbreviation ")
    if teacher:
        add_teacher_learn_answers(doc, ["verbs, adjectives, adverbs", "Adv"])
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "S. ", "Ships sailed slowly away today.", "l2_s", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l4a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 4, "Adjectives")
    add_section_label(doc, "Learn")
    add_body(doc, "An adjective describes a noun or a pronoun.")
    add_body(doc, "What kind? _____________________")
    add_body(doc, "Which _____________________?")
    add_body(doc, "How _______________________?")
    add_fill_line(doc, "It is labeled with the abbreviation ")
    if teacher:
        add_teacher_learn_answers(doc, ["What kind?, Which one?, How many?", "Adj"])
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "S. ", "Those five cargo ships sailed slowly away today.", "l4_s", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l5a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 5, "Article Adjectives")
    add_section_label(doc, "Learn")
    add_body(doc, "Article Adjectives are _______, __________, _________.")
    add_fill_line(doc, "They are labeled with the abbreviation ")
    add_body(doc, "Article adjectives are also known as ___________________.")
    if teacher:
        add_teacher_learn_answers(doc, ["a, an, the", "A", "noun markers"])
    add_knowledge_box(doc, "Use a before a consonant sound; use an before a vowel sound.")
    add_section_label(doc, "Practice — a or an")
    for item, _ in AAN_DRILL:
        add_body(doc, item, space_after=2)
    if teacher:
        add_para(doc, "a/an key: a, an, a, an, a, a, an, a, an", bold=True, color=ANSWER_BLUE, size=10)
    add_teacher_margin(doc, notes)


def page_l5b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 5, "Article Adjectives", space_after=6)
    add_section_label(doc, "Practice Together")
    add_classification_practice(doc, "S. ", "The five cargo ships sailed slowly away.", "l5_s", teacher=teacher)
    add_classification_practice(doc, "1. ", "The girls giggled loudly.", "l5_1", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l5c(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 5, "Article Adjectives", space_after=6)
    add_classification_practice(doc, "2. ", "The four happy girls giggled loudly today.", "l5_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "A huge whale swam very slowly away.", "l5_3", teacher=teacher)
    add_section_label(doc, "Apply")
    add_body(doc, "Write your own sentence using A Adj Adj SN V Adv Adv:", bold=True)
    add_blank_lines(doc, 4)
    add_memory_check(doc, ["Name the three article adjectives.", "Article adjectives are also known as what?"],
                     teacher=teacher, answers=["a, an, the", "noun markers"] if teacher else None)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l7b(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 7, "Sentence Types", space_after=6)
    add_knowledge_box(doc, "Skill Check: end mark → purpose → sentence type → label D, Imp, Int, or E.")
    add_classification_practice(doc, "S. ", "The two pirate ships appeared quite suddenly!", "l7_s", teacher=teacher)
    add_classification_practice(doc, "1. ", "The music played softly.", "l7_1", teacher=teacher)
    add_teacher_margin(doc, notes)


def page_l7c(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 7, "Sentence Types", space_after=6)
    add_classification_practice(doc, "2. ", "The very soothing music played softly tonight.", "l7_2", teacher=teacher)
    add_classification_practice(doc, "3. ", "Several urgent messages arrived very early today.", "l7_3", teacher=teacher)
    add_section_label(doc, "Parts of Speech")
    add_body(doc, "Write the abbreviations for the four parts of speech studied so far:")
    add_blank_lines(doc, 1)
    if teacher:
        add_teacher_learn_answers(doc, ["N, V, Adv, Adj"])
    add_memory_check(doc, ["Name the four sentence types and their labels.", "What is The Divide?"],
                     teacher=teacher, answers=["D, Imp, Int, E", "Slash before the verb"] if teacher else None)
    add_teacher_check(doc)
    add_teacher_margin(doc, notes)


def page_l8a(doc, teacher: bool = False, notes: TeacherPageNotes | None = None):
    add_lesson_banner(doc, 8, "Noun Check + Intensifiers")
    add_vocab_template(doc)
    if teacher:
        add_para(doc, "Teacher-assigned word", bold=True, color=ANSWER_BLUE, size=11)
    add_analogy_block(doc, "urgent : important :: answer : reply")
    if teacher:
        add_para(doc, "Relationship: synonym", bold=True, color=ANSWER_BLUE, size=11)
    add_knowledge_box(doc, "Noun Check: Subject Noun [word], yes, it is a noun.")
    add_knowledge_box(doc, "Intensifiers (very, extremely, quite, etc.) strengthen an adjective or adverb.")
    add_teacher_margin(doc, notes)


# ── Review documents ───────────────────────────────────────────────────────────

def add_review_content(doc, keyed: bool = False):
    add_body(doc, "Name: _________________     Date: _________________", space_after=10)
    add_section_label(doc, "Part A — SN/V Classification")
    for rid, prompt, kid in REVIEW_ITEMS[:2]:
        if keyed and kid:
            add_body(doc, prompt)
            render_classification(doc, CLASSIFICATION_KEYS[kid], answer=True)
        else:
            add_classification_practice(doc, prompt.split(".", 1)[0] + ". ", prompt.split(". ", 1)[1], kid)
    add_section_label(doc, "Part B — Full Pattern + Sentence Type")
    for rid, prompt, kid in REVIEW_ITEMS[2:4]:
        if keyed and kid:
            add_body(doc, prompt)
            render_classification(doc, CLASSIFICATION_KEYS[kid], answer=True)
        else:
            add_classification_practice(doc, prompt.split(".", 1)[0] + ". ", prompt.split(". ", 1)[1], kid)
    add_section_label(doc, "Part C — Questions")
    if keyed:
        add_para(doc, "Adverb: How? / When? / Where?", bold=True, color=ANSWER_BLUE)
        add_para(doc, "Adjective: What kind? / Which one? / How many?", bold=True, color=ANSWER_BLUE)
    else:
        add_blank_lines(doc, 1, "Adverb questions:")
        add_blank_lines(doc, 1, "Adjective questions:")
    add_section_label(doc, "Part D — a/an + Analogy")
    for rid, prompt, kid in REVIEW_ITEMS[6:9]:
        if keyed and kid in AAN_KEY:
            add_para(doc, f"{prompt}  →  {AAN_KEY[kid]}", bold=True, color=ANSWER_BLUE, space_after=4)
        elif keyed and kid == "analogy_rhyming":
            add_para(doc, f"{prompt}  →  rhyming", bold=True, color=ANSWER_BLUE, space_after=4)
        else:
            add_body(doc, prompt)
            if kid == "analogy_rhyming":
                add_body(doc, "Relationship: synonym    antonym    rhyming    part-to-whole")
            add_blank_lines(doc, 1)


def build_review():
    doc = Document()
    set_margins(doc.sections[0], 0.6, 0.6, 0.6, 0.6)
    add_para(doc, "Chapter 2 — In-Class Chapter Review", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_body(doc, "Complete this review in class. Work with a partner when your teacher directs.", italic=True, space_after=8)
    add_review_content(doc, keyed=False)
    add_teacher_check(doc)
    return doc


def build_review_key():
    doc = Document()
    set_margins(doc.sections[0], 0.6, 0.6, 0.6, 0.6)
    add_para(doc, "Chapter 2 — In-Class Chapter Review Key", bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_review_content(doc, keyed=True)
    return doc


# ── Teacher notes (1:1 with student pages) ────────────────────────────────────

TEACHER_NOTES = [
    TeacherPageNotes("Page 1 — Cover", procedures=["Student illustration — no fixed answer."]),
    TeacherPageNotes("Page 2 — Sentence Blueprint (Core Five)", procedures=["Review Q&A Flow before Lesson 1."]),
    TeacherPageNotes("Page 3 — Sentence Blueprint (continued)"),
    TeacherPageNotes("Page 4 — Lesson 1 Learn + S.", classifications=["l1_s"],
                     procedures=["Read sentence in unison before classifying."]),
    TeacherPageNotes("Page 5 — Lesson 1 Practice 1–3 + Memory Check", classifications=["l1_1", "l1_2", "l1_3"]),
    TeacherPageNotes("Page 6 — Lesson 1 Apply + Teacher Check",
                     procedures=["Use Who? for Boys (person)."]),
    TeacherPageNotes("Page 7 — Lesson 2 Learn + S.", classifications=["l2_s"]),
    TeacherPageNotes("Page 8 — Lesson 2 Practice 1–3 + Memory Check", classifications=["l2_1", "l2_2", "l2_3"],
                     procedures=["Spiders: where? around; how? quickly; How quickly? very"]),
    TeacherPageNotes("Page 9 — Lesson 2 Apply + Teacher Check"),
    TeacherPageNotes("Page 10 — Lesson 3 Learn + Practice 1–3", classifications=["l3_1", "l3_2", "l3_3"],
                     procedures=["Mover and Shaker — revision only."]),
    TeacherPageNotes("Page 11 — Lesson 3 Apply + checks"),
    TeacherPageNotes("Page 12 — Lesson 4 Learn + S.", classifications=["l4_s"]),
    TeacherPageNotes("Page 13 — Lesson 4 Practice 1–3 + Memory Check", classifications=["l4_1", "l4_2", "l4_3"]),
    TeacherPageNotes("Page 14 — Lesson 4 Apply + Teacher Check"),
    TeacherPageNotes("Page 15 — Lesson 5 Learn + a/an",
                     alternates=["Use noun markers only — no alternate grammar terminology outside TM Ch.2."]),
    TeacherPageNotes("Page 16 — Lesson 5 classify S. + 1–2", classifications=["l5_s", "l5_1"]),
    TeacherPageNotes("Page 17 — Lesson 5 classify 3 + Apply", classifications=["l5_2", "l5_3"]),
    TeacherPageNotes("Page 18 — Lesson 6 Practice 1–3", classifications=["l6_1", "l6_2", "l6_3"],
                     procedures=["Partial patterns — label only words present."]),
    TeacherPageNotes("Page 19 — Lesson 6 Memory + checks"),
    TeacherPageNotes("Page 20 — Lesson 7 Vocab", alternates=["Vocabulary: Teacher-assigned — do not pre-fill soothing."]),
    TeacherPageNotes("Page 21 — Lesson 7 Learn + analogy", answers=["D, Imp, Int, E", "rhyming"]),
    TeacherPageNotes("Page 22 — Lesson 7 Practice S. + 1", classifications=["l7_s", "l7_1"],
                     procedures=["Skill Check per TM Ref 26."]),
    TeacherPageNotes("Page 23 — Lesson 7 Practice 2–3 + checks", classifications=["l7_2", "l7_3"]),
    TeacherPageNotes("Page 24 — Lesson 8 Vocab + Learn",
                     alternates=["Vocabulary: Teacher-assigned — do not pre-fill urgent."]),
    TeacherPageNotes("Page 25 — Lesson 8 Practice 1–3", classifications=["l8_1", "l8_2", "l8_3"],
                     procedures=["Noun Check after Skill Check."]),
    TeacherPageNotes("Page 26 — Lesson 8 Memory + checks"),
    TeacherPageNotes("Page 27 — Lesson 9 Practice 1–3", classifications=["l9_1", "l9_2", "l9_3"]),
    TeacherPageNotes("Page 28 — Lesson 9 Cap/Punct + Review",
                     alternates=["Rule numbers: Verify against protected reference."]),
]

STUDENT_PAGES = [
    page_cover, page_blueprint, page_blueprint_2,
    page_l1a, page_l1b, page_l1c,
    page_l2a, page_l2b, page_l2c,
    page_l3, page_l3b,
    page_l4a, page_l4b, page_l4c,
    page_l5a, page_l5b, page_l5c,
    page_l6a, page_l6b,
    page_l7a, page_l7a2, page_l7b, page_l7c,
    page_l8a, page_l8b, page_l8c,
    page_l9a, page_l9b,
]


def build_student_packet():
    doc = Document()
    for i, builder in enumerate(STUDENT_PAGES, 1):
        section = doc.sections[0] if i == 1 else doc.add_section()
        set_margins(section)
        add_page_footer(section, i)
        builder(doc, teacher=False)
    return doc, len(STUDENT_PAGES)


def build_teacher_edition():
    doc = Document()
    for i, (builder, notes) in enumerate(zip(STUDENT_PAGES, TEACHER_NOTES), 1):
        section = doc.sections[0] if i == 1 else doc.add_section()
        set_margins(section)
        add_page_footer(section, i)
        builder(doc, teacher=True, notes=notes)
    return doc, len(STUDENT_PAGES)


def main():
    for path in (BLUEPRINT_IMG, CORE_FIVE_IMG, REF_SOURCE_PDF):
        if not path.exists():
            raise FileNotFoundError(f"Missing asset: {path}")
    assert len(TEACHER_NOTES) == len(STUDENT_PAGES), (
        f"Teacher notes ({len(TEACHER_NOTES)}) must match student pages ({len(STUDENT_PAGES)})"
    )
    outputs = [
        (STUDENT_OUT, *build_student_packet()),
        (TEACHER_OUT, *build_teacher_edition()),
        (REVIEW_OUT, build_review(), None),
        (REVIEW_KEY_OUT, build_review_key(), None),
    ]
    for path, document, page_count in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        document.save(str(path))
        label = f"{page_count} pages" if page_count else "document"
        print(f"Created: {path} ({label})")


if __name__ == "__main__":
    main()
