#!/usr/bin/env python3
"""Validate high-confidence source-PDF corrections and their audit artifacts."""
from __future__ import annotations
import csv
import json
import os
import sys
from pathlib import Path
import fitz

ROOT = Path(os.environ.get("RR_SOURCE_PDF_ROOT", Path(__file__).resolve().parents[1]))

def text(path: str, page_number: int) -> str:
    doc = fitz.open(ROOT / path)
    try:
        if page_number < 1 or page_number > len(doc):
            raise AssertionError(f"{path}: page {page_number} missing (pages={len(doc)})")
        return " ".join(doc[page_number - 1].get_text().split()).casefold()
    finally:
        doc.close()

def require(path: str, page: int, contains: tuple[str, ...], excludes: tuple[str, ...] = ()) -> None:
    value = text(path, page)
    for phrase in contains:
        if phrase.casefold() not in value:
            raise AssertionError(f"{path} p.{page}: expected {phrase!r}")
    for phrase in excludes:
        if phrase.casefold() in value:
            raise AssertionError(f"{path} p.{page}: obsolete text remains: {phrase!r}")

def badge_is_single_line(path: str, badge: tuple[float, float, float, float]) -> None:
    doc = fitz.open(ROOT / path)
    try:
        page = doc[14]
        rect = fitz.Rect(badge)
        values = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    span_rect = fitz.Rect(span["bbox"])
                    if rect.contains(span_rect) and span["text"].strip() in {"1", "0", "10"}:
                        values.append(span["text"].strip())
        if values != ["10"]:
            raise AssertionError(f"{path} p.15: expected one '10' span in badge, found {values}")
    finally:
        doc.close()

def main() -> None:
    require("masters_of_e_art_cinema.pdf", 10,
            ("first woman to win the Palme d'Or", "The Piano (1993)"),
            ("only woman to have won the Palme",))
    require("sensitive_cinema.pdf", 24,
            ("CONTENT NOTE", "violence is not proof of love"),
            ("love that contains violence is still love",))
    require("definitive_anime_encyclopedia.pdf", 56,
            ("Choose stories that reward your time",),
            ("anime was a mistake", "Hayao Miyazaki (misquoted"))
    require("ultimate_anime_guide.pdf", 22,
            ("Choose the stories that stay with you",),
            ("anime was a mistake", "Hayao Miyazaki (misquoted"))

    require("complete_movie_ratings.pdf", 1,
            ("218 unique films", "98 Essential Films", "33 Erotic Art Films", "87 Anime Movies"))
    require("complete_movie_ratings.pdf", 3, ("98 ESSENTIAL FILMS",))
    require("complete_movie_ratings.pdf", 6, ("33 EROTIC ART FILMS",))
    require("complete_movie_ratings.pdf", 7, ("87 ANIME MOVIES",))

    require("complete_movie_ratings_647.pdf", 1,
            ("647 ranked entries", "629 unique films"), ("647 unique titles",))
    require("complete_movie_ratings_647.pdf", 2,
            ("629 distinct films", "Eighteen repeat records"), ("647 unique titles",))
    require("complete_movie_ratings_647.pdf", 21,
            ("All 647 Ranked Entries by IMDb Score",), ("All 647 Films Ranked by IMDB Score",))
    require("complete_movie_ratings_647.pdf", 36,
            ("629 / 647 entries", "7.58 / 10", "26", "184", "53"))
    require("complete_movie_ratings_647.pdf", 39,
            ("647 ranked entries", "629 unique films"))

    require("complete_movie_encyclopedia.pdf", 2,
            ("Streaming entries in this edition are historical editorial notes", "not verified current availability"),
            ("Streaming availability reflects the Indian market as of 2025",))
    require("complete_movie_encyclopedia.pdf", 55,
            ("Streaming availability is time-sensitive", "not a current availability guarantee"),
            ("verified against Indian platform libraries as of 2025",))

    require("Cybersecurity_Stories_For_Your_Teams.pdf", 15,
            ("Do not use one generic clock", "GDPR Article 33", "NIS2-covered entities", "DORA financial entities"),
            ("Map this to your breach notification obligations",))
    require("Cybersecurity_Stories_For_Your_Teams.pdf", 17,
            ("There is no universal 72-hour response window", "documented in advance"),
            ("You have 72 hours",))

    require("Three_Year_Old_Reading_Guide (1).pdf", 15,
            ("Short, regular shared-reading sessions", "Follow the script and direction of the language", "Read Every Day: Choose a Rhythm That Works", "Point as You Read: Follow the Language Direction"),
            ("Daily reading at age 3 builds more neural pathways", "10 Minutes Beats 1 Hour", "left-to-right habit"))
    require("World_Stories_3YearOld_Guide.pdf", 15,
            ("Short, regular shared reading offers language exposure", "Follow the script and direction of the language"),
            ("Even 10 minutes of daily reading builds more neural pathways", "Run your finger under words as you read"))
    badge_is_single_line("Three_Year_Old_Reading_Guide (1).pdf", (51.4803, 631.9756, 72.7402, 659.9756))
    badge_is_single_line("World_Stories_3YearOld_Guide.pdf", (63.5276, 659.6315, 83.3701, 693.6315))

    # The footer area after "Happy reading." must be the original teal panel color,
    # not a missing glyph or a white cover-up rectangle.
    doc = fitz.open(ROOT / "Three_Year_Old_Reading_Guide (1).pdf")
    try:
        pix = doc[14].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
        teal = bytes((29, 137, 137))
        for y in range(749, 768):
            for x in range(487, 530):
                i = (y * pix.width + x) * pix.n
                if pix.samples[i:i+3] != teal:
                    raise AssertionError("Three_Year_Old_Reading_Guide p.15: footer glyph/patch remains")
    finally:
        doc.close()

    # Recompute the 647-row audit and compare it with the committed manifest and JSON.
    sys.path.insert(0, str(ROOT / "tools"))
    from manifest_movie_ratings_647 import parse_rows, audit
    parsed_rows, stats = audit(parse_rows(ROOT / "complete_movie_ratings_647.pdf"))
    with (ROOT / "FILM-RATINGS-647-MANIFEST.csv").open(newline="", encoding="utf-8") as handle:
        committed_rows = list(csv.DictReader(handle))
    if len(committed_rows) != 647:
        raise AssertionError(f"manifest row count is {len(committed_rows)}, expected 647")
    for index, (expected, actual) in enumerate(zip(parsed_rows, committed_rows), 1):
        for key, value in expected.items():
            if str(value) != actual.get(key):
                raise AssertionError(f"manifest row {index} field {key}: {actual.get(key)!r} != {value!r}")
    committed_stats = json.loads((ROOT / "FILM-RATINGS-647-AUDIT.json").read_text(encoding="utf-8"))
    if stats != committed_stats:
        raise AssertionError("committed JSON audit does not match a fresh parse of the PDF")
    if (stats["ranked_entries"], stats["unique_films_under_title_director_year_rule"], stats["duplicate_groups"]) != (647, 629, 18):
        raise AssertionError(f"unexpected audit summary: {stats}")

    print("Source-PDF correction checks passed: corrected claims, page text, toddler-guide layout, 647-row manifest and JSON audit match.")

if __name__ == "__main__":
    main()
