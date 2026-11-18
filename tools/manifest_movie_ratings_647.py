#!/usr/bin/env python3
"""Extract and audit the 647 ranked film rows from the ratings PDF."""
from __future__ import annotations
import argparse, csv, json, re, unicodedata
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import fitz
EXPECTED_ROWS = 647
FIRST_PAGE_INDEX = 20
LAST_PAGE_INDEX = 34
def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return " ".join(value.split())

def normalize_title(title: str, director: str, year: str) -> str:
    """Strip only recognized trailing category/year/director/alias labels."""
    title = unicodedata.normalize("NFKC", title).strip()
    match = re.search(r"\s+\(([^()]*)\)$", title)
    if match:
        label = normalize_name(match.group(1))
        director_tokens = normalize_name(director).split()
        director_suffixes = {" ".join(director_tokens[-n:]) for n in range(1, len(director_tokens) + 1)}
        categories = {"anime", "war", "animation", "drama", "essential", "erotic art", "erotic directors", "world cinema"}
        if label in categories or label == normalize_name(year) or label in director_suffixes or label == "laputa":
            title = title[:match.start()].strip()
    return normalize_name(title)

def parse_rows(pdf_path: Path):
    doc = fitz.open(pdf_path)
    rows = []
    try:
        for page_index in range(FIRST_PAGE_INDEX, LAST_PAGE_INDEX + 1):
            page = doc[page_index]
            words = page.get_text("words")
            markers = []
            for word in words:
                x0, y0, _x1, _y1, token = word[:5]
                if token.isdigit() and 1 <= int(token) <= EXPECTED_ROWS and 70 <= x0 <= 100 and 85 <= y0 <= 820:
                    markers.append((y0, int(token)))
            markers.sort()
            for index, (start_y, rank) in enumerate(markers):
                end_y = markers[index + 1][0] if index + 1 < len(markers) else 820.0
                entry_words = [w for w in words if start_y - 0.5 <= w[1] < end_y - 0.5 and 100 <= w[0] <= 540]
                def column(x_min, x_max):
                    selected = [w for w in entry_words if x_min <= w[0] < x_max]
                    selected.sort(key=lambda w: (round(w[1], 1), w[0]))
                    return " ".join(w[4] for w in selected).strip()
                rows.append({"rank": rank, "pdf_page": page_index + 1, "title": column(100, 250),
                    "director": column(250, 350), "year": column(350, 385),
                    "source_category": column(385, 450), "imdb_score": column(450, 490),
                    "rotten_tomatoes_pct": column(490, 540)})
    finally:
        doc.close()
    rows.sort(key=lambda row: int(row["rank"]))
    if len(rows) != EXPECTED_ROWS or [int(r["rank"]) for r in rows] != list(range(1, EXPECTED_ROWS + 1)):
        raise ValueError(f"Expected complete ranks 1–647; parsed {len(rows)} rows")
    for row in rows:
        for field in ("title", "director", "source_category"):
            if not row[field]:
                raise ValueError(f"Rank {row['rank']}: missing {field}")
        if not re.fullmatch(r"\d{4}", str(row["year"])):
            raise ValueError(f"Rank {row['rank']}: invalid year {row['year']!r}")
        if not re.fullmatch(r"\d\.\d", str(row["imdb_score"])):
            raise ValueError(f"Rank {row['rank']}: invalid IMDb score {row['imdb_score']!r}")
        if not re.fullmatch(r"\d{1,3}%", str(row["rotten_tomatoes_pct"])):
            raise ValueError(f"Rank {row['rank']}: invalid RT score {row['rotten_tomatoes_pct']!r}")
    return rows
def audit(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[(normalize_title(str(row["title"]), str(row["director"]), str(row["year"])), normalize_name(str(row["director"])), str(row["year"]))].append(row)
    duplicate_groups, group_ids, canonical = [], {}, {}
    for index, (key, group) in enumerate(sorted(groups.items(), key=lambda item: min(int(r["rank"]) for r in item[1])), 1):
        first = min(int(r["rank"]) for r in group)
        for row in group:
            rank = int(row["rank"])
            canonical[rank] = first
            if len(group) > 1:
                group_ids[rank] = f"D{index:02d}"
        if len(group) > 1:
            if len({str(r["imdb_score"]) for r in group}) != 1 or len({str(r["rotten_tomatoes_pct"]) for r in group}) != 1:
                raise ValueError(f"Duplicate group {key!r} has inconsistent ratings")
            duplicate_groups.append({"duplicate_group": f"D{index:02d}", "canonical_rank": first,
                "ranks": [int(r["rank"]) for r in sorted(group, key=lambda r: int(r["rank"]))],
                "title": str(group[0]["title"]), "director": str(group[0]["director"]),
                "year": str(group[0]["year"]),
                "categories": [str(r["source_category"]) for r in sorted(group, key=lambda r: int(r["rank"]))]})
    unique = [r for r in rows if canonical[int(r["rank"])] == int(r["rank"])]
    imdb = [Decimal(str(r["imdb_score"])) for r in unique]
    rt = [Decimal(str(r["rotten_tomatoes_pct"]).rstrip("%")) for r in unique]
    stats = {"ranked_entries": len(rows), "unique_films_under_title_director_year_rule": len(unique),
        "duplicate_groups": len(duplicate_groups), "repeat_category_records": len(rows) - len(unique),
        "average_imdb_unique_films": str((sum(imdb)/len(imdb)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
        "average_rt_unique_films": str((sum(rt)/len(rt)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)),
        "unique_films_imdb_8_5_plus": sum(v >= Decimal("8.5") for v in imdb),
        "unique_films_imdb_8_0_plus": sum(v >= Decimal("8.0") for v in imdb),
        "unique_films_rt_100": sum(v == Decimal("100") for v in rt),
        "rt_100_ranked_rows": sum(Decimal(str(r["rotten_tomatoes_pct"]).rstrip("%")) == Decimal("100") for r in rows),
        "duplicate_groups_detail": duplicate_groups}
    if (stats["ranked_entries"], stats["unique_films_under_title_director_year_rule"], stats["repeat_category_records"]) != (647, 629, 18):
        raise ValueError(f"Unexpected deduplication result: {stats}")
    output = []
    for row in rows:
        rank = int(row["rank"])
        output.append({**row, "canonical_rank": canonical[rank],
            "duplicate_group": group_ids.get(rank, ""),
            "is_repeat_record": "true" if rank != canonical[rank] else "false"})
    return output, stats
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--csv", type=Path, default=Path("FILM-RATINGS-647-MANIFEST.csv"))
    ap.add_argument("--json", type=Path, default=Path("FILM-RATINGS-647-AUDIT.json"))
    args = ap.parse_args()
    rows, stats = audit(parse_rows(args.pdf))
    with args.csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    args.json.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in stats.items() if k != "duplicate_groups_detail"}, indent=2))
    print(f"Wrote {args.csv} and {args.json}")
if __name__ == "__main__":
    main()
