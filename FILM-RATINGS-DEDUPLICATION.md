# Complete Movie Ratings 647 — deduplication audit

**Source:** `complete_movie_ratings_647.pdf`  
**Reviewed:** 18 November 2026  
**Purpose:** reconcile the 647-row combined ranking with the claim of 647 unique films.

## Result

The combined ranking on PDF pages 21–35 contains **647 numbered rows**, numbered 1–647 with no missing rank. Parsing the table columns (title, director, year, category, IMDb score and Rotten Tomatoes score) yields **18 repeated title/director/year groups**. Under the normalization rule below, that is **629 distinct films represented by 647 category-specific records**.

The repeats are retained in the source ranking because the same film appears in more than one source category. That can be useful for category traceability, but the cover and page 2 must not call all 647 rows “unique titles”. Page 36's existing average and threshold statistics also match the 647 rows, including repeats; they should either be labelled as entry-based or recalculated on the 629-film deduplicated set.

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

## Method

1. Read all numbered rows from pages 21–35 and verified the complete rank range 1–647.
2. Extracted title, director, year, category, IMDb and RT columns by their table positions.
3. Normalized Unicode and punctuation, removed parenthetical disambiguators from the title for comparison, and grouped by normalized title + director + year.
4. Found 18 groups with two category records each; the rating fields also match within each repeated group.

This is a reproducible, conservative duplicate rule, not a global film-database identity resolver. Alternate titles or inconsistent director/year metadata could conceal additional aliases. Therefore **629 is the distinct-film count under this documented rule**; do not claim a stronger globally verified count without a title-by-title alias review.

## Visual table verification

The original PDF was rendered and visually inspected at pages 13, 26 and 34:
- The columns align correctly in the sampled pages.
- The “Peter Mullan” director record belongs to rank 257, *The Magdalene Sisters*, on page 26. It is not part of the *Antichrist* row.
- The *Antichrist* rows at ranks 610–611 are two category records for the same film, not a column-shift defect.
- The anime score and RT columns are aligned in the sampled page 34 table.

The previously reported Peter Mullan and detached-score concerns were extraction-order false positives in these sampled pages. This does not substitute for a visual check of every table page.

## Required source-PDF correction

- Replace “647 Unique Titles” with “647 ranked entries · 629 unique films under the documented deduplication rule”.
- Correct page 2's explanation and duplicate policy.
- Correct page 36's unique-film count and either recalculate statistics on the deduplicated set or label them as 647-entry statistics.
- Keep IMDb/RT provenance and as-of dates unresolved until the original source URLs and collection dates are available.
