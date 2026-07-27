#!/usr/bin/env python3
"""Generate Chapter 1 Lesson 3–6 and Review presentations (DI pacing style)."""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "exports/teacher-resource-packs/Shurley_Chapter_1_Teacher_Resource_Pack/05_Presentations"

TITLE_BLUE = RGBColor(0x1E, 0x3A, 0x5F)
BODY_DARK = RGBColor(0x1F, 0x29, 0x37)
LIGHT_BG = RGBColor(0xF8, 0xFA, 0xFC)
TEACHER_GOLD = RGBColor(0xB4, 0x5F, 0x06)
ANSWER_GREEN = RGBColor(0x05, 0x96, 0x69)
MODEL_BLUE = RGBColor(0x1D, 0x4E, 0xD8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def new_deck() -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs


def blank_slide(prs: Presentation):
    return prs.slides.add_slide(prs.slide_layouts[6])


def fill_bg(slide, color=LIGHT_BG):
    fill = slide.background.fill
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


def title_slide(prs, lesson, subtitle):
    slide = blank_slide(prs)
    fill_bg(slide)
    add_textbox(slide, Inches(0.5), Inches(1.0), Inches(12.3), Inches(0.8), "Chapter 1 — Shurley English", 24, False, TITLE_BLUE, PP_ALIGN.CENTER)
    add_textbox(slide, Inches(0.5), Inches(2.0), Inches(12.3), Inches(1.2), lesson, 44, True, TITLE_BLUE, PP_ALIGN.CENTER)
    add_textbox(slide, Inches(0.5), Inches(3.5), Inches(12.3), Inches(0.8), subtitle, 28, False, BODY_DARK, PP_ALIGN.CENTER)


def teacher_model_slide(prs, heading, teacher_says, students_do):
    slide = blank_slide(prs)
    fill_bg(slide, RGBColor(0xFF, 0xFB, 0xEB))
    add_textbox(slide, Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.7), f"Teacher Model — {heading}", 32, True, TEACHER_GOLD)
    add_textbox(slide, Inches(0.7), Inches(1.2), Inches(11.8), Inches(2.5), f'Teacher says: "{teacher_says}"', 26, False, BODY_DARK)
    add_textbox(slide, Inches(0.7), Inches(3.8), Inches(11.8), Inches(2.5), f"Students do: {students_do}", 26, True, MODEL_BLUE)


def learn_slide(prs, heading, bullets):
    slide = blank_slide(prs)
    fill_bg(slide)
    add_textbox(slide, Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.7), heading, 36, True, TITLE_BLUE)
    y = Inches(1.2)
    for b in bullets:
        add_textbox(slide, Inches(0.7), y, Inches(11.8), Inches(0.65), f"•  {b}", 28, False, BODY_DARK)
        y += Inches(0.72)


def guided_practice_slide(prs, heading, items, is_answer=False):
    slide = blank_slide(prs)
    fill_bg(slide)
    color = ANSWER_GREEN if is_answer else TITLE_BLUE
    suffix = " — Answer Reveal" if is_answer else ""
    add_textbox(slide, Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.7), heading + suffix, 34, True, color)
    y = Inches(1.2)
    for i, text in enumerate(items, 1):
        add_textbox(slide, Inches(0.7), y, Inches(11.8), Inches(0.65), f"{i}.  {text}", 28, is_answer, ANSWER_GREEN if is_answer else BODY_DARK)
        y += Inches(0.78)


def check_slide(prs, question, expected):
    slide = blank_slide(prs)
    fill_bg(slide)
    add_textbox(slide, Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.7), "Check for Understanding", 34, True, TITLE_BLUE)
    add_textbox(slide, Inches(0.7), Inches(1.5), Inches(11.8), Inches(1.5), question, 30, False, BODY_DARK, PP_ALIGN.CENTER)
    add_textbox(slide, Inches(0.7), Inches(3.5), Inches(11.8), Inches(1.2), f"Expected: {expected}", 26, True, ANSWER_GREEN, PP_ALIGN.CENTER)


def build_lesson_3():
    prs = new_deck()
    title_slide(prs, "Lesson 3", "Complete Sentences")
    teacher_model_slide(prs, "Sentence Jingle",
                        "Let's chant the Sentence Jingle together. What five things does every sentence need?",
                        "Chant together. Then name the five parts on packet page 2.")
    learn_slide(prs, "Learn — Five Parts of a Complete Sentence", [
        "Capital letter at the beginning",
        "End mark (. ? !) at the end",
        "Complete sense — it makes sense",
        "Subject — who or what",
        "Verb — what the subject does or is",
    ])
    guided_practice_slide(prs, "Guided Practice — Check Your Sentence", [
        "Does it start with a capital letter?",
        "Does it end with an end mark?",
        "Does it make complete sense?",
        "Can you find the subject?",
        "Can you find the verb?",
    ])
    check_slide(prs, "Name all five parts of a complete sentence.", "Capital letter, End mark, Complete sense, Subject, Verb")
    title_slide(prs, "Lesson 3 (continued)", "Synonyms and Antonyms")
    teacher_model_slide(prs, "Synonyms",
                        "Synonyms are words with almost the same meaning. Noisy and loud are synonyms.",
                        "Turn and tell a partner one synonym pair.")
    teacher_model_slide(prs, "Antonyms",
                        "Antonyms are words with opposite meanings. Night and day are antonyms.",
                        "Turn and tell a partner one antonym pair.")
    guided_practice_slide(prs, "Guided Practice — Circle Synonym or Antonym", [
        "remember, forget  →  ?",
        "give, share  →  ?",
        "clumsy, graceful  →  ?",
        "shy, bashful  →  ?",
    ])
    guided_practice_slide(prs, "Guided Practice — Answer Reveal", [
        "remember, forget  →  Antonym",
        "give, share  →  Synonym",
        "clumsy, graceful  →  Antonym",
        "shy, bashful  →  Synonym",
    ], is_answer=True)
    check_slide(prs, "What is a synonym?", "Words with almost the same meaning")
    return prs


def build_lesson_4():
    prs = new_deck()
    title_slide(prs, "Lesson 4", "Understanding Analogies")
    teacher_model_slide(prs, "Analogy Intro",
                        "An analogy is a word puzzle. front is to back as top is to bottom.",
                        "Repeat using 'is to' and 'as.' Write bottom on packet page 5.")
    learn_slide(prs, "Learn — Analogy Symbols", [
        "Colon (:) separates words in a pair",
        "Double colon (::) means 'is to ___ as'",
        "Spoken: boat is to goat as fan is to ___",
        "Written: front : back :: top : ___",
    ])
    learn_slide(prs, "Learn — Four Relationship Types", [
        "Synonym — almost the same (big : large)",
        "Antonym — opposites (big : small)",
        "Rhyming — words rhyme (near : deer)",
        "Part-to-Whole — part of something (leaf : tree)",
    ])
    guided_practice_slide(prs, "Guided Practice — Preview", [
        "giggle : chuckle :: unhappy : ___________",
        "fire : ice :: asleep : ___________",
        "tree : forest :: page : ___________",
    ])
    guided_practice_slide(prs, "Guided Practice — Answer Reveal", [
        "giggle : chuckle :: unhappy : sad  (Synonym)",
        "fire : ice :: asleep : awake  (Antonym)",
        "tree : forest :: page : book  (Part-to-Whole)",
    ], is_answer=True)
    check_slide(prs, "What does :: mean in an analogy?", "Is to ___ as")
    return prs


def build_lesson_5():
    prs = new_deck()
    title_slide(prs, "Lesson 5", "Capitalization")
    teacher_model_slide(prs, "Proper Nouns",
                        "Proper nouns name specific people, places, or things. They always begin with a capital letter.",
                        "Point to Rule 1 on your reference page. Find one proper noun in Passage 1.")
    learn_slide(prs, "Learn — Capitalization", [
        "Capitalize the first word in a sentence",
        "Capitalize proper nouns: names, places, days, months",
        "Do NOT capitalize common nouns like 'friends' or 'night'",
        "Use reference pages 8–10 during editing",
    ])
    guided_practice_slide(prs, "Guided Practice — Passage 1 Preview", [
        "my friends and i will meet amy at the ford's theater on friday night to see nim's island.",
    ])
    guided_practice_slide(prs, "Answer Reveal — Passage 1", [
        "My, I, Amy, Ford's, Theater, Friday, Nim's, Island",
    ], is_answer=True)
    guided_practice_slide(prs, "Independent Practice — Preview", [
        "we drove to lake michigan on saturday with mrs. daniels.",
    ])
    guided_practice_slide(prs, "Answer Reveal — Sentence 1", [
        "We drove to Lake Michigan on Saturday with Mrs. Daniels.",
    ], is_answer=True)
    check_slide(prs, "What is a proper noun?", "A specific person, place, or thing — capitalized")
    return prs


def build_lesson_6():
    prs = new_deck()
    title_slide(prs, "Lesson 6", "Punctuation and Editing")
    teacher_model_slide(prs, "Model Sentences",
                        "Read sentence 1 aloud. What end mark does a question need?",
                        "Identify capitals, commas, and end marks on packet page 13.")
    learn_slide(prs, "Learn — Punctuation", [
        "Period (.) ends a statement",
        "Question mark (?) ends a question",
        "Exclamation point (!) shows strong feeling",
        "Commas separate items in a list",
        "Apostrophes show possession (Charlotte's Web)",
    ])
    guided_practice_slide(prs, "Editing Preview — Sentence 1", [
        "yes mr green will move to denver colorado on june 18 2024",
        "Find: 6 capitals, 4 commas, 1 period, 1 end mark",
    ])
    guided_practice_slide(prs, "Answer Reveal — Sentence 1", [
        "Yes, Mr. Green will move to Denver, Colorado, on June 18, 2024.",
    ], is_answer=True)
    guided_practice_slide(prs, "Editing Preview — Sentence 2", [
        "did your teacher ms coleman read charlottes web to your class today",
        "Find: 5 capitals, 2 commas, 1 period, 1 end mark, 1 apostrophe",
    ])
    guided_practice_slide(prs, "Answer Reveal — Sentence 2", [
        "Did your teacher, Ms. Coleman, read Charlotte's Web to your class today?",
    ], is_answer=True)
    check_slide(prs, "Name three punctuation marks.", "Period, question mark, exclamation point (also comma, apostrophe)")
    return prs


def build_review():
    prs = new_deck()
    title_slide(prs, "Chapter 1 Review", "In-Class Review")
    learn_slide(prs, "Review — Complete Sentences", [
        "Five parts: Capital letter, End mark, Complete sense, Subject, Verb",
    ])
    learn_slide(prs, "Review — Vocabulary", [
        "encourage — to cheer on",
        "magnify — to make something appear larger",
        "community — a town or group of people",
        "fraction — a part of a whole number",
    ])
    learn_slide(prs, "Review — Synonyms, Antonyms, Analogies", [
        "Synonyms = almost same meaning",
        "Antonyms = opposite meanings",
        "Four types: Synonym, Antonym, Rhyming, Part-to-Whole",
    ])
    guided_practice_slide(prs, "Review — Editing Preview", [
        "kevin asked bobby bill and tonya to his birthday party",
    ])
    guided_practice_slide(prs, "Answer Reveal — Editing", [
        "Kevin asked Bobby, Bill, and Tonya to his birthday party.",
    ], is_answer=True)
    return prs


DECKS = [
    ("Ch.1_Lesson_3_Complete_Sentences.pptx", build_lesson_3),
    ("Ch.1_Lesson_4_Analogies.pptx", build_lesson_4),
    ("Ch.1_Lesson_5_Capitalization.pptx", build_lesson_5),
    ("Ch.1_Lesson_6_Editing.pptx", build_lesson_6),
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
