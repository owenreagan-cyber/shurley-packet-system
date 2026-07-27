#!/usr/bin/env python3
"""Generate Chapter 1 Lesson 3–6 and Review presentations (blueprint visual style)."""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "exports/teacher-resource-packs/Shurley_Chapter_1_Teacher_Resource_Pack/05_Presentations"

# Blueprint palette (Chapter 2 visual-language-guide)
SN_BLUE = RGBColor(0x25, 0x63, 0xEB)
V_RED = RGBColor(0xDC, 0x26, 0x26)
ADV_GREEN = RGBColor(0x16, 0xA3, 0x4A)
TITLE_BLUE = RGBColor(0x1E, 0x3A, 0x5F)
BODY_DARK = RGBColor(0x1F, 0x29, 0x37)
LIGHT_BG = RGBColor(0xF8, 0xFA, 0xFC)
ACCENT_GOLD = RGBColor(0xCA, 0x8A, 0x04)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ANSWER_GREEN = RGBColor(0x05, 0x96, 0x69)


def new_deck() -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs


def blank_slide(prs: Presentation):
    return prs.slides.add_slide(prs.slide_layouts[6])


def fill_bg(slide, color=LIGHT_BG):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_textbox(slide, left, top, width, height, text, size=28, bold=False, color=BODY_DARK, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = "Calibri"
    return box


def add_title_slide(prs, lesson_label: str, subtitle: str):
    slide = blank_slide(prs)
    fill_bg(slide)
    add_textbox(slide, Inches(0.6), Inches(1.2), Inches(12), Inches(1.2), "Chapter 1 — Shurley English", 24, False, TITLE_BLUE, PP_ALIGN.CENTER)
    add_textbox(slide, Inches(0.6), Inches(2.2), Inches(12), Inches(1.4), lesson_label, 44, True, TITLE_BLUE, PP_ALIGN.CENTER)
    add_textbox(slide, Inches(0.6), Inches(3.8), Inches(12), Inches(1), subtitle, 28, False, BODY_DARK, PP_ALIGN.CENTER)


def add_learn_slide(prs, heading: str, bullets: list[str]):
    slide = blank_slide(prs)
    fill_bg(slide)
    add_textbox(slide, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), heading, 36, True, TITLE_BLUE)
    y = Inches(1.4)
    for b in bullets:
        add_textbox(slide, Inches(0.8), y, Inches(11.5), Inches(0.7), f"•  {b}", 26, False, BODY_DARK)
        y += Inches(0.75)


def add_classification_slide(
    prs,
    heading: str,
    sentence: str,
    labels: list[tuple[str, str]],
    pattern_lines: list[str],
    sentence_type: str = "",
    is_answer: bool = False,
):
    """Blueprint two-zone slide: Pattern Zone (left) + Construction Zone (right)."""
    slide = blank_slide(prs)
    fill_bg(slide)
    tag = " — Answer" if is_answer else " — Preview"
    add_textbox(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7), heading + tag, 32, True, ANSWER_GREEN if is_answer else TITLE_BLUE)

    # Pattern zone box
    pat = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0.5), Inches(1.2), Inches(3.8), Inches(5.5))
    pat.fill.solid()
    pat.fill.fore_color.rgb = RGBColor(0xE0, 0xE7, 0xFF)
    pat.line.color.rgb = SN_BLUE
    add_textbox(slide, Inches(0.65), Inches(1.35), Inches(3.5), Inches(0.5), "Pattern Zone", 20, True, SN_BLUE)
    py = Inches(2.0)
    for line in pattern_lines:
        add_textbox(slide, Inches(0.75), py, Inches(3.3), Inches(0.6), line, 24, True, BODY_DARK, PP_ALIGN.CENTER)
        py += Inches(0.65)

    # Construction zone box
    con = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(4.6), Inches(1.2), Inches(8.2), Inches(5.5))
    con.fill.solid()
    con.fill.fore_color.rgb = WHITE
    con.line.color.rgb = TITLE_BLUE
    add_textbox(slide, Inches(4.75), Inches(1.35), Inches(7.8), Inches(0.5), "Construction Zone", 20, True, TITLE_BLUE)

    words = sentence.replace(".", "").replace("!", "").replace("?", "").split()
    if not words:
        words = [sentence]
    x_start = Inches(5.0)
    slot_w = Inches(7.6 / max(len(words), 1))
    for i, word in enumerate(words):
        wx = x_start + slot_w * i
        add_textbox(slide, wx, Inches(2.3), slot_w, Inches(0.55), word + (sentence[-1] if i == len(words) - 1 and sentence[-1] in ".!?" else ""), 28, True, BODY_DARK, PP_ALIGN.CENTER)
        if is_answer and i < len(labels):
            lbl, color = labels[i]
            lb = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, wx + Inches(0.05), Inches(3.0), slot_w - Inches(0.1), Inches(0.45))
            lb.fill.solid()
            lb.fill.fore_color.rgb = color
            lb.line.fill.background()
            add_textbox(slide, wx, Inches(3.05), slot_w, Inches(0.4), lbl, 18, True, WHITE, PP_ALIGN.CENTER)
        elif not is_answer:
            add_textbox(slide, wx, Inches(3.0), slot_w, Inches(0.4), "?", 22, True, RGBColor(0x99, 0x99, 0x99), PP_ALIGN.CENTER)

    if is_answer and sentence_type:
        add_textbox(slide, Inches(10.5), Inches(4.2), Inches(2), Inches(0.6), sentence_type, 32, True, V_RED, PP_ALIGN.CENTER)


def add_guided_practice_slide(prs, heading: str, items: list[str], answers: list[str] | None = None):
    slide = blank_slide(prs)
    fill_bg(slide)
    is_answer = answers is not None
    add_textbox(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7), heading + (" — Answers" if is_answer else ""), 32, True, ANSWER_GREEN if is_answer else TITLE_BLUE)
    y = Inches(1.3)
    src = answers if is_answer else items
    for i, text in enumerate(src, 1):
        add_textbox(slide, Inches(0.8), y, Inches(11.5), Inches(0.65), f"{i}.  {text}", 26, is_answer, ANSWER_GREEN if is_answer else BODY_DARK)
        y += Inches(0.85)


def add_analogy_slide(prs, heading: str, analogy: str, relationship: str = "", is_answer: bool = False):
    slide = blank_slide(prs)
    fill_bg(slide)
    add_textbox(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7), heading, 32, True, ANSWER_GREEN if is_answer else TITLE_BLUE)
    add_textbox(slide, Inches(0.8), Inches(2.0), Inches(11.5), Inches(1.2), analogy, 36, True, BODY_DARK, PP_ALIGN.CENTER)
    if is_answer and relationship:
        add_textbox(slide, Inches(0.8), Inches(3.8), Inches(11.5), Inches(0.8), f"Relationship: {relationship}", 28, True, ANSWER_GREEN, PP_ALIGN.CENTER)


def add_cp_preview_slide(prs, cp_label: str, sentences: list[str]):
    slide = blank_slide(prs)
    fill_bg(slide, RGBColor(0xFF, 0xF7, 0xED))
    add_textbox(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7), f"Classroom Practice Preview — {cp_label}", 30, True, ACCENT_GOLD)
    add_textbox(slide, Inches(0.8), Inches(1.1), Inches(11.5), Inches(0.6), "Oral only — not in student packet", 22, True, ACCENT_GOLD, PP_ALIGN.CENTER)
    y = Inches(2.0)
    for s in sentences:
        add_textbox(slide, Inches(0.8), y, Inches(11.5), Inches(0.7), s, 28, False, BODY_DARK)
        y += Inches(0.85)


def add_editing_slide(prs, heading: str, sentence: str, is_answer: bool = False, note: str = ""):
    slide = blank_slide(prs)
    fill_bg(slide)
    add_textbox(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7), heading + (" — Answer" if is_answer else ""), 32, True, ANSWER_GREEN if is_answer else TITLE_BLUE)
    add_textbox(slide, Inches(0.8), Inches(1.8), Inches(11.5), Inches(1.5), sentence, 30, is_answer, ANSWER_GREEN if is_answer else BODY_DARK, PP_ALIGN.CENTER)
    if note:
        add_textbox(slide, Inches(0.8), Inches(4.0), Inches(11.5), Inches(0.6), note, 22, False, ACCENT_GOLD, PP_ALIGN.CENTER)


def build_lesson_3() -> Presentation:
    prs = new_deck()
    add_title_slide(prs, "Lesson 3", "Complete Sentences, Synonyms, and Antonyms")
    add_learn_slide(prs, "Learn — Five Parts of a Complete Sentence", [
        "Capital letter at the beginning",
        "End mark (. ? !) at the end",
        "Complete sense — the sentence makes sense",
        "Subject — who or what the sentence is about",
        "Verb — what the subject does or is",
    ])
    add_classification_slide(prs, "Guided Practice 1", "Cats ran.", [], ["SN V", "P1"], is_answer=False)
    add_classification_slide(
        prs, "Guided Practice 1", "Cats ran.",
        [("Cats", SN_BLUE), ("ran", V_RED)], ["SN V", "P1"], "D", is_answer=True,
    )
    add_classification_slide(prs, "Guided Practice 2", "Birds flew away.", [], ["SN V", "P1"], is_answer=False)
    add_classification_slide(
        prs, "Guided Practice 2", "Birds flew away.",
        [("Birds", SN_BLUE), ("flew", V_RED)], ["SN V", "P1"], "D", is_answer=True,
    )
    add_learn_slide(prs, "Learn — Synonyms and Antonyms", [
        "Synonyms = words with almost the same meaning (noisy / loud)",
        "Antonyms = words with opposite meanings (night / day)",
        "Circle Synonym or Antonym for each pair on your packet page 11.",
    ])
    add_guided_practice_slide(prs, "Synonym / Antonym Practice", [
        "remember, forget  →  ?",
        "give, share  →  ?",
        "clumsy, graceful  →  ?",
    ])
    add_guided_practice_slide(prs, "Synonym / Antonym Practice", [], [
        "remember, forget  →  Antonym",
        "give, share  →  Synonym",
        "clumsy, graceful  →  Antonym",
    ])
    add_cp_preview_slide(prs, "Oral Warm-Up", [
        "Say a synonym pair: run and dash",
        "Say an antonym pair: hot and cold",
        "Chant the Sentence Jingle together",
    ])
    return prs


def build_lesson_4() -> Presentation:
    prs = new_deck()
    add_title_slide(prs, "Lesson 4", "Understanding Analogies")
    add_learn_slide(prs, "Learn — What Is an Analogy?", [
        "An analogy shows how two word pairs are related.",
        "Spoken: boat is to goat as fan is to ___",
        "Written: front : back :: top : ___",
        "Colon (:) separates words in a pair.",
        "Double colon (::) means “is to ___ as”.",
    ])
    add_analogy_slide(prs, "Worked Example — Preview", "front : back :: top : _________")
    add_analogy_slide(prs, "Worked Example — Answer", "front : back :: top : bottom", "Antonym", is_answer=True)
    add_learn_slide(prs, "Learn — Four Analogy Relationships", [
        "Synonym — words mean almost the same (big : large)",
        "Antonym — words are opposites (big : small)",
        "Rhyming — words rhyme (near : deer)",
        "Part-to-Whole — first word is part of second (leaf : tree)",
    ])
    add_guided_practice_slide(prs, "Guided Practice — Preview", [
        "giggle : chuckle :: unhappy : ___________",
        "fire : ice :: asleep : ___________",
        "tree : forest :: page : ___________",
    ])
    add_guided_practice_slide(prs, "Guided Practice — Answers", [], [
        "giggle : chuckle :: unhappy : sad  (Synonym)",
        "fire : ice :: asleep : awake  (Antonym)",
        "tree : forest :: page : book  (Part-to-Whole)",
    ])
    add_analogy_slide(prs, "Source Example", "encourage : cheer :: easy : simple", "Synonym", is_answer=True)
    add_cp_preview_slide(prs, "Oral Warm-Up", [
        "Nice is to Kind as Mad is to Angry — what relationship?",
        "Finger is to Hand as Tree is to Forest — what relationship?",
    ])
    return prs


def build_lesson_5() -> Presentation:
    prs = new_deck()
    add_title_slide(prs, "Lesson 5", "Vocabulary, Capitalization, and Editing")
    add_analogy_slide(prs, "Vocabulary Analogy Example", "fraction : whole :: wing : bird", "Part-to-Whole", is_answer=True)
    add_learn_slide(prs, "Learn — Capitalization Rules", [
        "Capitalize the first word in a sentence.",
        "Capitalize proper nouns: names, places, days, months.",
        "Use your packet reference pages 18–20 during editing.",
    ])
    add_editing_slide(prs, "Capitalization Passage — Preview",
                      "my friend amy and i went to ford's theater on friday.")
    add_editing_slide(prs, "Capitalization Passage — Answer",
                      "My friend Amy and I went to Ford's Theater on Friday.", is_answer=True)
    add_editing_slide(prs, "Editing — Capitals Only — Preview",
                      "we drove to lake michigan on saturday with mrs. daniels.")
    add_editing_slide(prs, "Editing — Capitals Only — Answer",
                      "We drove to Lake Michigan on Saturday with Mrs. Daniels.", is_answer=True)
    add_cp_preview_slide(prs, "Oral Warm-Up", [
        "Which words need capitals: reagan, main street, july?",
        "Point to Rule 1 on your reference page.",
    ])
    return prs


def build_lesson_6() -> Presentation:
    prs = new_deck()
    add_title_slide(prs, "Lesson 6", "Capitalization, Punctuation, and Mixed Editing")
    add_analogy_slide(prs, "Vocabulary Analogy Example", "individual : community :: bird : flock", "Part-to-Whole", is_answer=True)
    add_learn_slide(prs, "Learn — Model Sentences", [
        "A complete sentence needs a capital, end mark, and complete sense.",
        "Commas separate items in a list.",
        "Apostrophes show possession (Charlotte's Web).",
    ])
    add_editing_slide(prs, "Mixed Editing 1 — Preview",
                      "yes mr green will move to denver colorado on june 18 2024",
                      note="Find: 6 capitals, 4 commas, 1 period, 1 end mark")
    add_editing_slide(prs, "Mixed Editing 1 — Answer",
                      "Yes, Mr. Green will move to Denver, Colorado, on June 18, 2024.",
                      is_answer=True)
    add_editing_slide(prs, "Mixed Editing 2 — Preview",
                      "did your teacher ms coleman read charlottes web to your class today",
                      note="Find: 5 capitals, 2 commas, 1 period, 1 end mark, 1 apostrophe")
    add_editing_slide(prs, "Mixed Editing 2 — Answer",
                      "Did your teacher, Ms. Coleman, read Charlotte's Web to your class today?",
                      is_answer=True)
    add_cp_preview_slide(prs, "Oral Warm-Up", [
        "What end mark goes with a question?",
        "Name two punctuation marks besides the period.",
    ])
    return prs


def build_review() -> Presentation:
    prs = new_deck()
    add_title_slide(prs, "Chapter 1 Review", "In-Class Chapter Review")
    add_learn_slide(prs, "Review — Complete Sentences", [
        "Name all five parts: Capital letter, End mark, Complete sense, Subject, Verb",
    ])
    add_learn_slide(prs, "Review — Synonyms and Antonyms", [
        "Synonyms have almost the same meaning.",
        "Antonyms have opposite meanings.",
        "hot / warm = Synonym     run / walk = Antonym",
    ])
    add_learn_slide(prs, "Review — Analogies", [
        "Four types: Synonym, Antonym, Rhyming, Part-to-Whole",
        "big : small :: hot : cold  (Antonym)",
        "leaf : tree :: paw : dog  (Part-to-Whole)",
    ])
    add_learn_slide(prs, "Review — Vocabulary", [
        "encourage — to cheer on",
        "magnify — to make something appear larger",
        "community — a town or group of people",
        "fraction — a part of a whole number",
    ])
    add_editing_slide(prs, "Review — Editing",
                      "kevin asked bobby bill and tonya to his birthday party",
                      note="Correct: 4 capitals, 2 commas, 1 end mark")
    add_editing_slide(prs, "Review — Editing Answer",
                      "Kevin asked Bobby, Bill, and Tonya to his birthday party.",
                      is_answer=True)
    return prs


DECKS = [
    ("Ch.1_Lesson_3_Complete_Sentences.pptx", build_lesson_3),
    ("Ch.1_Lesson_4_Analogies.pptx", build_lesson_4),
    ("Ch.1_Lesson_5_Capitalization_Editing.pptx", build_lesson_5),
    ("Ch.1_Lesson_6_Mixed_Editing.pptx", build_lesson_6),
    ("Ch.1_Chapter_Review.pptx", build_review),
]


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, builder in DECKS:
        path = OUT_DIR / filename
        prs = builder()
        prs.save(str(path))
        print(f"Created: {path} ({len(prs.slides)} slides)")


if __name__ == "__main__":
    main()
