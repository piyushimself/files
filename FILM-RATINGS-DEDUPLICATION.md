# Complete Movie Ratings 647 — deduplication audit

**Source:** \`complete_movie_ratings_647.pdf\`  
**Reviewed:** 19 November 2026  
**Purpose:** reconcile the 647-row combined ranking with the claim of 647 unique films.

## Result

The combined ranking on PDF pages 21–35 contains **647 numbered rows**, numbered 1–647 with no missing rank. Parsing the table columns (title, director, year, source category, IMDb score and Rotten Tomatoes score) yields **18 repeated title/director/year groups**. Under the documented normalization rule, those are **629 distinct films represented by 647 category-specific records**.

The repeats are retained because the same film appears in more than one source category. This preserves category traceability, but the cover and page 2 must not call all 647 rows “unique titles”.

## Recomputed unique-film statistics

The statistics below use one canonical row per normalized title/director/year group, retaining the first ranked row for each group. Duplicate groups were checked to have matching IMDb and RT values.

| Metric | 629 distinct films |
|---|---:|
| Average IMDb score | 7.58 / 10 |
| Average Rotten Tomatoes Tomatometer | 88% |
| IMDb 8.5+ | 26 |
| IMDb 8.0+ | 184 |
| 100% RT | 53 |

The 100% RT appendix still contains **55 ranked rows**, representing **53 distinct films**.

## Duplicate groups

| Ranks | Canonical film | Repeated category records |
|---:|---|---|
| 16, 17 | Grave of the Fireflies | Essential; Anime |
| 32, 33 | Apocalypse Now | Essential; War |
| 37, 40 | Come and See | Essential; War |
| 99, 101 | The Tale of Princess Kaguya | Anime; Animation |
| 128, 132 | The Seventh Seal | Essential; Drama |
| 138, 139 | Millennium Actress | Anime; Animation |
| 141, 142 | Nausicaä of the Valley of the Wind | Anime; Animation |
| 146, 147 | Perfect Blue | Anime; Animation |
| 168, 169 | Castle in the Sky (Laputa) | Anime; Animation |
| 182, 184 | Tokyo Godfathers | Anime; Animation |
| 282, 284 | Naked | Erotic Art; Drama |
| 297, 298 | Only Yesterday | Anime; Animation |
| 320, 321 | Paprika | Anime; Animation |
| 391, 392 | The Piano | Essential; Erotic Directors |
| 438, 439 | Pom Poko | Anime; Animation |
| 580, 581 | Sweetie | World Cinema; Erotic Directors |
| 610, 611 | Antichrist | Erotic Art; Erotic Directors |
| 629, 630 | Romance | Erotic Art; Erotic Directors |

## Reproducibility

- Parser: \`tools/manifest_movie_ratings_647.py\`
- Per-row manifest: \`FILM-RATINGS-647-MANIFEST.csv\`
- Machine-readable audit: \`FILM-RATINGS-647-AUDIT.json\`
- Run: \`python tools/manifest_movie_ratings_647.py complete_movie_ratings_647.pdf --csv FILM-RATINGS-647-MANIFEST.csv --json FILM-RATINGS-647-AUDIT.json\`

The parser uses the PDF's fixed column geometry, validates all ranks 1–647 and required fields, normalizes Unicode/punctuation, strips a trailing parenthetical only when it is a year, recognized source category, director-name suffix, or the known alternate-title label “Laputa”, and groups by normalized title + normalized director + year. Unrecognized parenthetical title text is preserved. It verifies that all repeated rows have matching IMDb and RT values.

This is a reproducible, rule-based deduplication method, not a global film-database identity resolver. It can still miss aliases that are not encoded in the PDF and should be reviewed before treating 629 as a universal catalogue count. Alternate titles or inconsistent director/year metadata could conceal additional aliases. Therefore **629 is the distinct-film count under this documented rule**, not a claim of globally verified unique works.

## Visual table verification

All 15 ranking pages (21–35) were reviewed in a contact sheet for consistent table geometry and column placement; pages 21, 26 and 34 were additionally inspected at high resolution:
- The columns align correctly in the sampled pages.
- The “Peter Mullan” director record belongs to rank 257, *The Magdalene Sisters*, on page 26. It is not part of the *Antichrist* row.
- The *Antichrist* rows at ranks 610–611 are two category records for the same film, not a column-shift defect.
- The anime score and RT columns are aligned in the sampled page 34 table.

The earlier Peter Mullan and detached-score concerns were extraction-order false positives in those sampled pages. The page 21 heading was also corrected from “All 647 Films Ranked” to “All 647 Ranked Entries by IMDb Score”. The contact-sheet review checks layout consistency, not every title/score individually. IMDb/RT source URLs and collection dates remain unresolved.

## Source-PDF correction

The review branch corrects the cover, methodology, page 36 statistics, page footers and final-page tagline to distinguish ranked entries from distinct films. All original source documents remain withheld pending rights evidence and broader fact-checking.
