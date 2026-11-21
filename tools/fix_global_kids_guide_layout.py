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
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(fix_layout(args.source, args.output))


if __name__ == "__main__":
    main()
