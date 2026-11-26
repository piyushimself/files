#!/usr/bin/env python3
"""Replace missing ZapfDingbats markers in the personal reference PDF.

The original source is never overwritten. Rating values and surrounding page
content are retained; star and bullet symbols are redrawn as PDF vectors.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path
import fitz


def rgb(value: int) -> tuple[float, float, float]:
    return ((value >> 16 & 255) / 255, (value >> 8 & 255) / 255, (value & 255) / 255)


def sample_background(pix: fitz.Pixmap, rect: fitz.Rect, scale: float = 3.0) -> tuple[float, float, float]:
    # Sample just above the glyph on the same flat row background, away from antialiasing.
    x = max(0, min(pix.width - 1, round((rect.x0 + rect.x1) * scale / 2)))
    y = max(0, min(pix.height - 1, round((rect.y0 - 1.2) * scale)))
    index = (y * pix.width + x) * pix.n
    return tuple(pix.samples[index + channel] / 255 for channel in range(3))


def star_points(cx: float, cy: float, outer: float, inner: float) -> list[fitz.Point]:
    points = []
    for index in range(10):
        radius = outer if index % 2 == 0 else inner
        angle = -math.pi / 2 + index * math.pi / 5
        points.append(fitz.Point(cx + math.cos(angle) * radius, cy + math.sin(angle) * radius))
    return points


def draw_star(page: fitz.Page, cx: float, cy: float, radius: float, color, background, filled: bool) -> None:
    page.draw_polyline(
        star_points(cx, cy, radius, radius * 0.43),
        color=color,
        fill=color if filled else background,
        width=0.55,
        closePath=True,
        lineJoin=1,
    )


def glyph_kind(value: str):
    if value and set(value) <= {"#", "I"} and "#" in value:
        return ("stars", value.count("#"), value.count("I"))
    if value == "#":
        return ("star",)
    return ("bullet",)


def fix(source: Path, output: Path) -> int:
    document = fitz.open(source)
    replaced = 0
    for page in document:
        spans = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if span.get("font") == "ZapfDingbats":
                        spans.append(span)
        if not spans:
            continue

        pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False)
        redactions = []
        drawings = []
        for span in spans:
            rect = fitz.Rect(span["bbox"])
            background = sample_background(pixmap, rect)
            color = rgb(span["color"])
            redactions.append((rect, background))
            drawings.append((rect, background, color, glyph_kind(span["text"])))

        for rect, background in redactions:
            page.add_redact_annot(rect, fill=background, cross_out=False)
        page.apply_redactions(images=0, graphics=0)

        for rect, background, color, kind in drawings:
            center_x = (rect.x0 + rect.x1) / 2
            center_y = (rect.y0 + rect.y1) / 2
            if kind[0] == "stars":
                filled, empty = kind[1], kind[2]
                count = filled + empty
                cell_width = rect.width / max(count, 1)
                radius = min(rect.height * 0.43, cell_width * 0.44)
                for index in range(count):
                    draw_star(
                        page,
                        rect.x0 + cell_width * (index + 0.5),
                        center_y,
                        radius,
                        color,
                        background,
                        filled=index < filled,
                    )
            elif kind[0] == "star":
                radius = min(rect.height * 0.42, rect.width * 0.44)
                draw_star(page, center_x, center_y, radius, color, background, filled=True)
            else:
                radius = min(rect.height * 0.14, 1.05)
                page.draw_circle((center_x, center_y), radius, color=color, fill=color, width=0.2)
        replaced += len(spans)

    output.parent.mkdir(parents=True, exist_ok=True)
    document.save(output, garbage=4, deflate=True)
    document.close()
    return replaced


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    arguments = parser.parse_args()
    print(f"Replaced {fix(arguments.source, arguments.output)} ZapfDingbats spans with vector glyphs")
