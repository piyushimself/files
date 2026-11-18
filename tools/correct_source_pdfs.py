#!/usr/bin/env python3
"""Apply narrowly scoped, visually reviewed editorial corrections to source PDFs.

This script edits only the exact passages listed below. It does not clear any
source for publication or establish copyright/licensing permission.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
import fitz

ROOT = Path(os.environ.get("RR_SOURCE_PDF_ROOT", Path(__file__).resolve().parents[1]))


def block_rect(page: fitz.Page, needle: str) -> fitz.Rect:
    normalize = lambda value: re.sub(r'\s+', ' ', value).strip().casefold()
    target = normalize(needle)
    # search_for handles phrases that cross PDF text-line boundaries more
    # consistently across PyMuPDF versions than raw block-string matching.
    hits = page.search_for(target)
    if hits:
        hit_union = union([fitz.Rect(hit) for hit in hits])
        blocks = [fitz.Rect(b[:4]) for b in page.get_text('blocks')]
        containing = [rect for rect in blocks if rect.contains(hit_union)]
        if len(containing) == 1:
            return containing[0]
        overlapping = [rect for rect in blocks if rect.intersects(hit_union)]
        if len(overlapping) == 1:
            return overlapping[0]
    matches = [fitz.Rect(b[:4]) for b in page.get_text('blocks') if target in normalize(b[4])]
    if len(matches) != 1:
        raise RuntimeError(f'expected one text block for {needle!r}; search hits={len(hits)}, blocks={len(matches)}')
    return matches[0]


def union(rects: list[fitz.Rect]) -> fitz.Rect:
    out = fitz.Rect(rects[0])
    for r in rects[1:]:
        out |= r
    return out


def redact(page: fitz.Page, rects: list[fitz.Rect], fill: tuple[float, float, float]) -> None:
    for rect in rects:
        page.add_redact_annot(rect, fill=fill, cross_out=False)
    page.apply_redactions(images=0, graphics=0)


def put(page: fitz.Page, rect: fitz.Rect, text: str, *, font: str, size: float,
        color: tuple[float, float, float], align: int = 0, lineheight: float = 1.15,
        label: str) -> None:
    spare = page.insert_textbox(rect, text, fontname=font, fontsize=size,
                                color=color, align=align, lineheight=lineheight)
    if spare < 0:
        raise RuntimeError(f'{label}: text did not fit in {rect}; overflow={spare:.2f}')


def save_doc(doc: fitz.Document, path: Path) -> None:
    tmp = path.with_suffix(path.suffix + '.tmp')
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    tmp.replace(path)


def edit_masters() -> None:
    path = ROOT / 'masters_of_e_art_cinema.pdf'
    doc = fitz.open(path)
    page = doc[9]
    print(f'DEBUG masters path={path.resolve()} size={path.stat().st_size} pages={len(doc)}')
    print(f'DEBUG masters page10 text={page.get_text()[:900]!r}')
    print(f'DEBUG masters search={page.search_for("Jane Campion")!r}')
    old = block_rect(page, 'Jane Campion is the only woman to have won the Palme')
    corrected = (
        "Jane Campion was the first woman to win the Palme d'Or at Cannes, for The Piano (1993). "
        'She later won the Academy Award for Best Director for The Power of the Dog (2022). '
        'Her cinema is defined by an unflinching engagement with female desire, female power, and the violence that greets both. '
        "The Piano remains the great feminist erotic film: Holly Hunter's mute Ada communicating through a keyboard and Harvey Keitel's body, "
        'in colonial New Zealand, is a portrait of desire as the most radical form of self-expression. '
        'Sweetie (1989), An Angel at My Table (1990), Portrait of a Lady (1996), and In the Cut (2003), a noir about female sexual danger in New York, '
        "all share the conviction that female interiority is cinema's most unexplored territory."
    )
    redact(page, [old], (1, 1, 1))
    put(page, old, corrected, font='Times-Roman', size=9.1,
        color=(26/255, 16/255, 8/255), lineheight=1.12, label='Campion paragraph')
    save_doc(doc, path)


def edit_sensitive() -> None:
    path = ROOT / 'sensitive_cinema.pdf'
    doc = fitz.open(path)
    page = doc[23]
    old = block_rect(page, 'WHAT IT TEACHES\nLove that contains violence')
    redact(page, [old], (12/255, 12/255, 12/255))
    heading = fitz.Rect(old.x0, old.y0, old.x1, old.y0 + 10.2)
    body = fitz.Rect(old.x0, old.y0 + 10.8, old.x1, old.y1)
    put(page, heading, 'CONTENT NOTE', font='Helvetica-Bold', size=7.0,
        color=(201/255, 169/255, 110/255), lineheight=1.0, label='Sensitive Cinema content-note heading')
    put(page, body,
        'Family violence. The film depicts attachment alongside harm; violence is not proof of love.',
        font='Helvetica', size=7.35, color=(122/255, 117/255, 112/255),
        lineheight=1.12, label='Sensitive Cinema content note')
    save_doc(doc, path)


def edit_anime_quote(filename: str, page_index: int, tagline: str, size: float) -> None:
    path = ROOT / filename
    doc = fitz.open(path)
    page = doc[page_index]
    quote = block_rect(page, '“Anime was a mistake.”')
    attribution = block_rect(page, 'Hayao Miyazaki (misquoted')
    rect = union([quote, attribution])
    redact(page, [quote, attribution], (1, 1, 1))
    put(page, rect, tagline, font='Times-BoldItalic', size=size,
        color=(255/255, 209/255, 102/255), align=fitz.TEXT_ALIGN_CENTER,
        lineheight=1.0, label=f'{filename} original tagline')
    save_doc(doc, path)


def sample_rgb(page: fitz.Page, x: int, y: int) -> tuple[float, float, float]:
    pix = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
    i = (y * pix.width + x) * pix.n
    rgb = tuple(pix.samples[i:i+3])
    return tuple(v / 255 for v in rgb)


def edit_ratings() -> None:
    path = ROOT / 'complete_movie_ratings.pdf'
    doc = fitz.open(path)
    page = doc[0]
    old = block_rect(page, '218 unique films')
    redact(page, [old], (1, 1, 1))
    put(page, old,
        '218 unique films · 98 Essential Films · 33 Erotic Art Films · 87 Anime Movies',
        font='Helvetica', size=9.0, color=(170/255, 170/255, 170/255),
        align=fitz.TEXT_ALIGN_CENTER, lineheight=1.0, label='ratings cover counts')
    for page_index, old_text, new_text in [
        (2, '100 ESSENTIAL FILMS', '98 ESSENTIAL FILMS'),
        (5, '50 EROTIC ART FILMS', '33 EROTIC ART FILMS'),
        (6, '100 ANIME MOVIES', '87 ANIME MOVIES'),
    ]:
        page = doc[page_index]
        old = block_rect(page, old_text)
        fill = sample_rgb(page, 50, 110)
        redact(page, [old], fill)
        put(page, old, new_text, font='Times-BoldItalic', size=15.5,
            color=(1, 1, 1), align=fitz.TEXT_ALIGN_CENTER,
            lineheight=1.0, label=f'ratings page {page_index+1} heading')
    save_doc(doc, path)


def edit_encyclopedia() -> None:
    path = ROOT / 'complete_movie_encyclopedia.pdf'
    doc = fitz.open(path)
    page = doc[1]
    a = block_rect(page, 'Streaming availability reflects the Indian market as of 2025')
    b = block_rect(page, 'MUBI operates a rotating library')
    rect = union([a, b])
    redact(page, [a, b], (1, 1, 1))
    disclaimer = (
        'Streaming entries in this edition are historical editorial notes, not verified current availability. '
        'Platform catalogues and licensing change frequently, and a title may be removed without notice. '
        'Verify each title in the India region directly with the service or a current regional availability provider before subscribing or purchasing.'
    )
    put(page, rect, disclaimer, font='Times-Roman', size=9.6,
        color=(13/255, 13/255, 13/255), lineheight=1.18,
        label='encyclopedia page 2 availability disclaimer')

    page = doc[54]
    old = block_rect(page, 'Streaming availability verified against Indian platform libraries as of 2025')
    redact(page, [old], (1, 1, 1))
    old = fitz.Rect(old.x0, old.y0 - 0.5, old.x1, old.y1 + 10.0)
    put(page, old, 'Streaming availability is time-sensitive. These entries are not a current availability guarantee; verify the India catalogue before subscribing or purchasing.',
        font='Helvetica-Oblique', size=7.2, color=(102/255, 102/255, 102/255),
        align=fitz.TEXT_ALIGN_CENTER, lineheight=1.0,
        label='encyclopedia final-page availability disclaimer')
    save_doc(doc, path)


def edit_cybersecurity() -> None:
    path = ROOT / 'Cybersecurity_Stories_For_Your_Teams.pdf'
    doc = fitz.open(path)
    bg = (246/255, 242/255, 235/255)
    heading_color = (107/255, 114/255, 128/255)
    body_color = (28/255, 28/255, 28/255)

    page = doc[14]
    old = block_rect(page, 'Map this to your breach notification obligations')
    redact(page, [old], bg)
    heading = fitz.Rect(old.x0, old.y0, old.x1, old.y0 + 10.5)
    body = fitz.Rect(old.x0, old.y0 + 11.0, old.x1, old.y1)
    put(page, heading, 'TELL YOUR TEAM', font='Helvetica-Bold', size=7.5,
        color=heading_color, lineheight=1.0, label='cyber page 15 heading')
    text = (
        'Do not use one generic clock. GDPR Article 33 generally requires a controller to notify the supervisory authority within 72 hours of awareness of a personal-data breach, '
        "unless the breach is unlikely to result in a risk to individuals' rights and freedoms. NIS2-covered entities have a 24-hour early warning, a 72-hour incident notification, "
        'and a final report within one month. DORA financial entities follow a separate timetable: initial notification within four hours of classifying a major ICT incident and no later than 24 hours after awareness; '
        'an intermediate report within 72 hours of the initial notification; and a final report within one month after the intermediate report. Confirm scope and deadlines with counsel.'
    )
    put(page, body, text, font='Times-Roman', size=8.9,
        color=body_color, lineheight=1.12, label='cyber page 15 legal timeline correction')

    page = doc[16]
    old = block_rect(page, 'Ransomware with a payment countdown is Speed. You have 72 hours')
    redact(page, [old], bg)
    heading = fitz.Rect(old.x0, old.y0, old.x1, old.y0 + 10.5)
    body = fitz.Rect(old.x0, old.y0 + 11.0, old.x1, old.y1)
    put(page, heading, 'TELL YOUR TEAM', font='Helvetica-Bold', size=7.5,
        color=heading_color, lineheight=1.0, label='cyber page 17 heading')
    text = (
        'Ransomware with a payment countdown is Speed. There is no universal 72-hour response window. Your Operations team must contain spread, assess scope, brief leadership, activate backups, '
        "and follow the pre-agreed payment decision process. The payment decision cannot be improvised in hour two of a live incident. Your organisation's policy (whether to pay, under what conditions, and who decides) "
        'must be documented in advance. Regulatory notification deadlines depend on the applicable regime, incident classification and data involved; do not use a generic countdown.'
    )
    put(page, body, text, font='Times-Roman', size=8.9,
        color=body_color, lineheight=1.12, label='cyber page 17 ransomware timeline correction')
    save_doc(doc, path)


def edit_kids_guide(filename: str, neural_needle: str, neural_text: str,
                    direction_needle: str, direction_text: str,
                    *, color: tuple[float, float, float], size: float) -> None:
    path = ROOT / filename
    doc = fitz.open(path)
    page = doc[14]
    for needle, replacement, label in [
        (neural_needle, neural_text, "reading-frequency evidence wording"),
        (direction_needle, direction_text, "language-aware reading-direction guidance"),
    ]:
        old = block_rect(page, needle)
        fill = sample_rgb(page, int(old.x0 + 2), int(old.y0 + 2))
        redact(page, [old], fill)
        put(page, old, replacement, font='Helvetica-Oblique', size=size,
            color=color, lineheight=1.08, label=f'{filename} {label}')
    save_doc(doc, path)


def edit_kids_guides() -> None:
    edit_kids_guide(
        'Three_Year_Old_Reading_Guide (1).pdf',
        'Daily reading at age 3 builds more neural pathways',
        'Short, regular shared-reading sessions can make books part of everyday life. Choose a relaxed rhythm that works for your family.',
        'Run your finger slowly under words',
        'If it helps your child follow along, move a finger or bookmark under the words. Follow the script and direction of the language you are reading; pointing is optional.',
        color=(102/255, 102/255, 102/255), size=7.8,
    )
    edit_kids_guide(
        'World_Stories_3YearOld_Guide.pdf',
        'Even 10 minutes of daily reading builds more neural pathways',
        'Short, regular shared reading offers language exposure and a familiar book routine. Longer relaxed sessions are welcome too; choose a rhythm that works for your family.',
        'Run your finger under words as you read',
        'If it helps your child follow along, point under the words. Follow the script and direction of the language you are reading; pointing is optional.',
        color=(26/255, 82/255, 118/255), size=7.8,
    )


def main() -> None:
    edit_masters()
    edit_sensitive()
    edit_anime_quote('definitive_anime_encyclopedia.pdf', 55,
                     'Choose stories that reward your time.', 16.0)
    edit_anime_quote('ultimate_anime_guide.pdf', 21,
                     'Choose the stories that stay with you.', 14.5)
    edit_ratings()
    edit_encyclopedia()
    edit_cybersecurity()
    edit_kids_guides()
    print('Applied 7 source-PDF corrections. All files remain withheld pending rights clearance.')


if __name__ == "__main__":
    main()
