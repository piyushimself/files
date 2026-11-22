#!/usr/bin/env python3
"""Expand the Global Kids Books PDF canvas to reveal clipped table columns.

The source tables extend beyond the A4 MediaBox on multiple pages. This
preserves the original vector/text content and size, widens every page to one
consistent custom page width, and writes a separate output file.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import fitz


def visible_bounds(page: fitz.Page) -> tuple[float, float] | None:
    boxes = [box for kind, box in page.get_bboxlog()
             if kind in {"fill-path", "fill-text", "stroke-path", "stroke-text"}]
    if not boxes:
        return None
    return min(box[0] for box in boxes), max(box[2] for box in boxes)


def repair_wrapped_row_numbers(page: fitz.Page) -> int:
    """Replace vertically wrapped two-digit row numbers in the first table column."""
    spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                x0, y0, x1, y1 = span["bbox"]
                value = span["text"].strip()
                if x0 < 16 and y0 > 230 and len(value) == 1 and value.isdigit():
                    spans.append((value, x0, y0, x1, y1, span["color"]))
    spans.sort(key=lambda item: item[2])

    repairs = []
    for first, second in zip(spans, spans[1:]):
        if (first[0] != "1" or abs(first[1] - second[1]) >= 0.6
                or not second[0].isdigit() or not 10 < second[2] - first[2] < 14):
            continue
        midpoint = (first[2] + second[4]) / 2
        background = (1.0, 1.0, 1.0)
        for drawing in page.get_drawings():
            rect = drawing["rect"]
            if (drawing.get("fill") and rect.x0 <= first[1] <= rect.x1
                    and rect.y0 <= midpoint <= rect.y1):
                background = drawing["fill"]
                break

        # Stay inside the narrow number cell and preserve its borders/row fill.
        patch = fitz.Rect(first[1] - 1.7, first[2] - 1.0,
                          first[1] + 9.5, second[4] + 1.0)
        page.add_redact_annot(patch, fill=background, cross_out=False)
        repairs.append((first[0] + second[0], first[1], first[2]))

    if repairs:
        # Remove the original stacked glyphs from the text layer, not just visually cover them.
        page.apply_redactions(images=0, graphics=0)
        for number, x0, y0 in repairs:
            page.insert_text((x0, y0 + 9.6), number, fontname="helv",
                             fontsize=8.5, color=(68 / 255, 68 / 255, 68 / 255),
                             overlay=True)
    return len(repairs)


def count_wrapped_row_number_pairs(page: fitz.Page) -> int:
    """Count residual stacked digit pairs after repair."""
    spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                x0, y0, _, _ = span["bbox"]
                value = span["text"].strip()
                if x0 < 16 and y0 > 230 and len(value) == 1 and value.isdigit():
                    spans.append((value, x0, y0))
    spans.sort(key=lambda item: item[2])
    return sum(1 for first, second in zip(spans, spans[1:])
               if first[0] == "1" and abs(first[1] - second[1]) < 0.6
               and second[0].isdigit() and 10 < second[2] - first[2] < 14)


def fix_layout(source: Path, output: Path) -> dict[str, int | float]:
    if source.resolve() == output.resolve():
        raise ValueError("Output must be separate; source is never overwritten")
    doc = fitz.open(source)
    if not doc:
        raise ValueError("Source PDF has no pages")

    bounds = [visible_bounds(page) for page in doc]
    bounds = [item for item in bounds if item is not None]
    if not bounds:
        raise ValueError("No visible page content found")

    # Existing table content spans x=-73.46 to x=668.74 on A4 pages.
    # Keep a 0.5 pt margin on each side; do not scale or rasterize content.
    left = min(0.0, min(item[0] for item in bounds)) - 0.5
    right = max(max(page.rect.width for page in doc),
                max(item[1] for item in bounds)) + 0.5
    height = max(page.rect.height for page in doc)
    before_chars = sum(len(page.get_text()) for page in doc)

    for page in doc:
        old = page.mediabox
        page.set_mediabox(fitz.Rect(left, old.y0, right, old.y1))

    repaired_number_cells = sum(repair_wrapped_row_numbers(page) for page in doc)
    remaining_number_pairs = sum(count_wrapped_row_number_pairs(page) for page in doc)
    if remaining_number_pairs:
        doc.close()
        raise RuntimeError(f"Two-digit row numbers still wrap vertically: {remaining_number_pairs}")

    # Remove only truly empty pages (no text, vector drawings, images or annotations).
    blank_page_indexes = []
    for index, page in enumerate(doc):
        if (not page.get_text().strip() and not page.get_drawings()
                and not page.get_images(full=True) and page.first_annot is None
                and not page.get_bboxlog()):
            blank_page_indexes.append(index)
    for index in reversed(blank_page_indexes):
        doc.delete_page(index)

    violations = []
    for index, page in enumerate(doc, start=1):
        box = visible_bounds(page)
        if box and (box[0] < -1.0 or box[1] > page.rect.width + 1.0):
            violations.append((index, box, page.rect.width))
    if violations:
        doc.close()
        raise RuntimeError(f"Content remains clipped: {violations[:5]}")

    output.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output, garbage=4, deflate=True, clean=True)
    after_chars = sum(len(page.get_text()) for page in doc)
    pages = len(doc)
    doc.close()

    # Newly visible off-page text increases extraction; content must not vanish.
    if after_chars < before_chars:
        raise RuntimeError(f"Text extraction lost content: {before_chars} -> {after_chars}")
    return {
        "pages": pages,
        "page_width_pt": round(right - left, 2),
        "page_height_pt": round(height, 2),
        "text_characters_before": before_chars,
        "text_characters_after": after_chars,
        "overflow_pages_after_fix": 0,
        "repaired_two_digit_number_cells": repaired_number_cells,
        "remaining_wrapped_number_pairs": remaining_number_pairs,
        "blank_pages_removed": len(blank_page_indexes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(fix_layout(args.source, args.output))


if __name__ == "__main__":
    main()
