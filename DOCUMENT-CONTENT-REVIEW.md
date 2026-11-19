# Source-document content review

**Status: reviewed for content quality and publication risk; not cleared for publication.**

## Scope and method

- 49 source files are present: 43 PDFs, 3 DOCX files, 1 TXT file and 2 Pine Script files.
- One exact duplicate PDF pair was identified, leaving **48 unique source documents**: 42 unique PDFs, 3 DOCX, 1 TXT and 2 Pine files.
- The 574-page combined-film PDF is a duplicate of its (1) copy; both remain withheld, and the unique content needs to be reviewed only once.
- Text extraction completed for all 49 source files with no extraction errors. OCR was used on three low-text pages. The extracted text was reviewed for structure, count consistency, sample content, sensitive themes, attribution and obvious editorial problems.
- This is a substantive editorial triage, not a line-by-line fact-check of every book, film, author, rating or URL. Visual inspection is still required for PDFs whose column/table layouts produce garbled text extraction.
- The extraction detected no common contact or credential patterns. That is not a complete privacy review.

## Rights decision

**All 49 source files remain withheld. No document is approved for publication.**

The text scan did not establish a publication licence or ownership for any of these files. Mentions of Creative Commons, public domain, authors, publishers or ISBNs inside a document are not proof that the document itself is licensed for republication. Absence of a copyright notice is also not permission.

Several files contain substantial third-party material: poems, film descriptions, book descriptions, curated lists, ratings, quotations, and aggregated collections. Obtain evidence of authorship/licence/permission before publishing them. For compilations, confirm rights for both the compilation and any reproduced descriptions or excerpts.

**Repository exposure:** withholding a file from GitHub Pages does not make it private. The originals remain accessible in this public GitHub repository. If rights are uncertain, move the originals to a private repository or private storage before treating them as safe.

## Per-file editorial review

| Source file | Content review and issues found | Decision |
|---|---|---|
| 1000_Creative_Educational_Cultural_Links.pdf | A large resource directory with descriptions and URLs. The document's “verified/safe” framing is not substantiated by a current link check. Links can be dead, redirected, changed or unsafe over time. | Withhold; validate all links and soften “verified” claims. |
| 1000_Google_Searches_Grand_Curiosity_Atlas.pdf | Curiosity/search prompts cover cultures and communities. Some wording frames groups as “pure,” “last,” secretive or frozen in time. Rephrase to avoid exoticising and essentialising living communities; add reliable sources for factual framing. | Withhold; cultural and factual edit required. |
| 1000_Greatest_Fictional_Books.pdf | The contents counts sum to 1,000 slots, but the cover says 26 traditions while the contents lists 36 sections. A title-line audit found only 857 unique titles (143 repeats), and the list includes memoir/non-fiction works despite “Fictional Books” in the title. Many repeated entries are explicitly marked “already listed.” | Withhold; correct scope, categories, duplicates and classification. |
| 1000_Inspirations.pdf | The contents claims 1,000, while the extracted numbered list contains 1,001 items and one section is labelled 201. Minor count inconsistency; some prompts touch on sensitive social issues. | Withhold; reconcile count and add suitable content notes. |
| 1000_Writing_Prompts.docx | The file contains 835 prompts, not 1,000+. The title/cover overstates the inventory. | Withhold; rename to the actual count or complete the missing prompts. |
| 100_essential_films.pdf | A 100-film list with adult/erotic material among the selections. Descriptions and selection claims need attribution and fact-checking. | Withhold; rights review and mature-content label required. |
| 2000_Inspirations (1).pdf | The title and “200 each” framing are inaccurate: the ten section counts add to 1,462, not 2,000. The sections have materially different counts. | Withhold; complete the missing content or retitle/recount accurately. |
| 200_Films_Like_Frida.pdf | A film recommendation list with short editorial descriptions. The numbered list contains 220 entries but only 218 unique title lines, despite the 200-film title. Selection rationale and factual details need source checks; no republication rights established. | Withhold; rights and fact-check required. |
| 200_prompts_emotion_wonder_v2.pdf | Reflective prompts include grief, trauma and emotionally intense themes. The material should distinguish journaling prompts from therapeutic advice and include content notes. | Withhold; add boundaries/content notes and review attribution. |
| 200_prompts_mind_detox_v2.pdf | Useful reflective structure, but “detox” can imply a mental-health intervention. Avoid suggesting that prompts treat or cure anxiety or other conditions; add a clear non-therapy note. | Withhold; revise health framing and establish rights. |
| 200_thinkers_quiet_mind_v2.pdf | Philosophical/psychological material is presented as a course for reducing anxiety and mental noise. Claims and thinker attributions need sources; do not imply clinical efficacy. | Withhold; source-check and reframe as reflective education, not treatment. |
| 300_Films_Filmography.pdf | A 300-film list. Only 298 numbered entry lines were extracted (numbering reaches 300), so two entries need reconciliation. Names/transliterations need proofreading; examples include damaged diacritics in filmmaker names. Some evaluative claims are unattributed. | Withhold; proofread names and source factual claims. |
| 500_Films_500_Music_Global_Guide.pdf | The 500-film/500-music structure is present. Quotes and descriptive claims need attribution; selection criteria and rights for descriptions are unclear. | Withhold; rights and attribution review. |
| 500_Manga_Movies.pdf | A manga-adaptation film list with mature titles/themes. Entry descriptions and title counts need a complete audit. | Withhold; rights review and mature-content label required. |
| 50_e_art_films.pdf | An explicitly erotic/art-cinema guide. Its distinction between erotic art cinema and pornography is an editorial claim, not a self-evident fact. | Withhold; 18+ label, fact-check and rights review. |
| ATH - Pine.txt | This file is now a deprecation notice for the former monthly indicator. The retired implementation had chart-timeframe-dependent monthly signals, an unreliable weekly exit stream, displayed but unenforced stop/target levels, and invalid account-level return/drawdown calculations. Its executable predecessor remains in Git history. | Keep deprecated and withheld; do not describe it as a tested strategy. Use the weekly replacement only after external TradingView validation. |
| ATH_Weekly_Confirmed_Strategy.pine | Replacement Strategy Tester strategy introduced in PR #15. It requires a weekly chart, reads only the previous confirmed monthly candle, evaluates exits on confirmed weekly bars, submits actual `strategy.entry`/`strategy.exit` orders, sizes from strategy equity, and caps open legs/deployed capital. Static source checks pass, but it has not been compiled or backtested in TradingView. | Withhold from performance/live-use claims until TradingView compilation, symbol-specific backtests, Bar Magnifier/order-sequencing review, quantity/point-value checks and broker-cost/fill calibration are completed. |
| A_Filmmakers_Reading_List.pdf | A curated reading list. Statements about which works are influential or widely cited need references; titles/authors and edition details need checking. | Withhold; source-check and rights review. |
| A_Life_Worth_Living_500_Suggestions.docx | A 500-item life/reading/art list. There are duplicate identity/name references (e.g. Meera Bai/Mirabai) and translation/attribution issues that need checking; some recommendations are subjective but written as definitive. | Withhold; deduplicate and verify translations/attributions. |
| Aag_Ki_Kavitayen.pdf | A 100-poem Hindi compilation containing poems attributed to modern and well-known poets. Full poems are likely protected literary works; no permission evidence was found. | **High rights risk — keep withheld unless explicit permission/licence is documented.** |
| All_Film_Collections_Combined_compressed (1).pdf | 574-page, approximately 211,000-word aggregate of multiple film collections and descriptions. It is an exact duplicate of the un-suffixed file. The compilation contains extensive third-party film/book descriptions and sensitive/adult material. | Withhold; review one copy only; rights clearance required for the entire compilation. |
| All_Film_Collections_Combined_compressed.pdf | Exact byte-for-byte duplicate of the (1) file. No separate content review is needed. | Withhold as duplicate; retain only one working copy if the owner later chooses. |
| Bold_Cinema_Collection.pdf | A 300+ film collection with erotic/explicit sections. Streaming/platform availability is time-sensitive and needs current verification. | Withhold; 18+ label, current availability checks and rights review. |
| Crypto_Trend_Rider_4H.pine | Static review found no request.security lookahead use, but trade/alert conditions are not gated by barstate.isconfirmed, so intrabar signals/alerts can appear and disappear. The Chandelier candidate can move down, loosening a long stop; the initial risk stop is not the enforced exit. Exit is close-based, not an intrabar stop fill. Partial exits are counted as separate trade events, so win rate/average R/holding statistics are not position-level; unrealised drawdown, fees, slippage and crypto funding are omitted. It is an indicator, not a Strategy Tester strategy, and was not compiled/backtested in TradingView. | Withhold from performance claims; fix confirmation, stop ratchet, position-level metrics and realistic costs before relying on it. |
| Cybersecurity_Stories_For_Your_Teams.pdf | Security analogies are useful as discussion starters, but the GDPR/NIS2/DORA incident-reporting timelines are oversimplified. GDPR Article 33 is a 72-hour controller notification where feasible and subject to the risk exception; NIS2 uses a 24-hour early warning, 72-hour incident notification and one-month final report; DORA RTS 2025/301 uses an initial notification within four hours of major classification and no later than 24 hours after awareness, followed by staged reports. Metaphors must not be mistaken for technical equivalence. See the official references below. | Withhold from training publication until regulatory claims are corrected and sourced. |
| Cybersecurity_Storytelling_Movies.pdf | Movie-to-security mappings are illustrative, not technical controls. Cost and impact claims (e.g. BEC/phishing losses) lack citations. Add sources and label analogies clearly. | Withhold; fact-check and source claims. |
| Films_That_Open_New_Human_Domains.pdf | A 200-film thematic list with strongly interpretive descriptions. Separate subjective interpretation from verifiable facts and establish rights for descriptions. | Withhold; editorial/source review. |
| Free_Art_Resource_Library.docx | Resource directory contains at least one missing URL and time-sensitive audience/subscriber claims. Every link and access/licence statement needs checking. | Withhold; repair missing links and verify resource licences. |
| Global_Kids_Books_Complete_Guide.pdf | Substantial overlap with the “FINAL” reading guide (roughly 55% token-set similarity). Text extraction shows table/column ordering problems on some pages; the 600+ count needs an auditable inventory. | Withhold; visually inspect layout, reconcile with the FINAL version and count titles. |
| Global_Kids_Reading_Guide_FINAL (1).pdf | Near-duplicate of the complete guide, with overlapping age bands and recommendations. Choose one canonical version and merge only genuinely unique entries; verify age suitability and book metadata. | Withhold; consolidate and source-check. |
| Personal_Reference_Film_Books_Art.pdf | A 49-entry personal reference with adult/erotic cinema. Rating glyphs appear as ####I in extracted text, suggesting a font/encoding or export issue requiring visual inspection. | Withhold; fix glyph rendering, label mature material and verify rights. |
| Reading_Course_Emotions_Wonder.pdf | A 40-book reflective course. Strong outcome promises are subjective and should be reframed as intentions, not guaranteed personal transformation. | Withhold; soften claims and verify bibliographic details. |
| Three_Year_Old_Reading_Guide (1).pdf | A 60-story/40-week guide. It makes an unsupported neuroscience claim that daily reading creates “more neural pathways” than weekend reading. Left-to-right reading guidance is not universal across scripts/languages. | Withhold; remove unsupported science claims and make literacy guidance language-aware. |
| World_Stories_3YearOld_Guide.pdf | Near-duplicate of the other three-year-old guide (roughly 57% token-set similarity). Some table/column text extracts in the wrong order. The shared neuroscience claim needs removal. | Withhold; consolidate with the other guide and visually verify layout. |
| asian_books_curriculum.pdf | A 300-book/6-arc curriculum contains visible editorial placeholders such as “Not Asian — replace with …” and non-Asian entries inside an Asian-literature list. | **Not publication-ready — remove placeholders, correct scope and re-audit all entries.** |
| asian_cinema_curriculum.pdf | A 200-film curriculum with interpretive commentary. Verify country/region classifications, titles, directors and cultural framing; add sources for factual claims. | Withhold; source and editorial review. |
| cinema_900 (1).pdf | Internal contradiction: the cover lists 100 films in each of three lists (300 total), while the contents and section introductions say 300 films per list (900 total). The contents' regional subtotals add to 300 for each list, supporting the 900 framing, but the cover is materially wrong. The extracted list sections also show numbering extending well beyond 100. The separate library-3 collection reports 835, likely a de-duplicated/overlap-adjusted count, but that relationship is not documented. | **Not publication-ready — correct cover and reconcile 900 raw entries against 835 library entries; state duplicate policy.** |
| complete_movie_encyclopedia.pdf | Claims 647 films and streaming availability verified in 2025. The availability statement is stale in 2026; library-3 refers to 649, a two-title discrepancy. | Withhold; reconcile count and remove/update dated availability claims. |
| complete_movie_ratings.pdf | Claims 218 unique films, but section labels imply 100 essential, 50 erotic-art and 100 anime entries while extracted section counts are 98, 33 and 87. The 218 total matches those actual counts, not the section labels. | Withhold; correct section titles/counts and verify ratings/source dates. |
| complete_movie_ratings_647.pdf | The three named sections contain 100 essential + 50 erotic-art + 88 anime = 238 entries; the combined ranking contains 647 numbered rows (1–647). A reproducible title/director/year normalization finds 18 repeated category records, leaving 629 distinct films under that rule; see FILM-RATINGS-DEDUPLICATION.md. Visual inspection of pages 13, 26 and 34 confirms the sampled table columns align: Peter Mullan belongs to The Magdalene Sisters (rank 257), not Antichrist, and the Antichrist rows are duplicate category entries. The earlier extraction-alignment concerns are false positives in those sampled pages, but every table page still needs visual review. Page 2/cover overstate uniqueness; page 36 statistics currently reflect 647 rows including repeats. IMDb/RT values still need source URLs and an as-of date per record or batch. | Withhold; correct 647-entry/629-film claims and statistics labels, complete remaining visual checks, and add rating provenance/date. |
| definitive_anime_encyclopedia.pdf | A 200-work anime guide includes a Hayao Miyazaki quote that the document itself identifies as misquoted. Remove it rather than repeating a known false attribution. | Withhold; remove false attribution and verify all quotes. |
| library-3.pdf | A 4,942-item personal film/art library. Its top-level category totals add to 4,942, but subcollection counts conflict with other files (900 vs 835; 647 vs 649). It aggregates overlapping collections and sensitive material. Its 900-slot world-cinema source is represented as 835 in the combined library, and the film encyclopedia appears as 649 there versus 647 in its standalone file. | Withhold; reconcile source-of-truth counts, duplicates and rights. |
| manga_recommendations.pdf | A short recommendation list includes mature romance/manhwa titles. Confirm age suitability and the rights to descriptions. | Withhold; mature-content label and rights review. |
| masters_of_art.pdf | A 25-artist guide with biographical and work descriptions. Verify dates, works, quotes and image/description rights. | Withhold; fact-check and rights review. |
| masters_of_e_art_cinema.pdf | A 15-filmmaker erotic-art-cinema guide. It incorrectly says Jane Campion is the only woman to have won the Palme d'Or; later women directors have also won. Explicit material requires an 18+ label. | **Not publication-ready — correct the false claim, add 18+ notice and verify rights.** |
| meditation_on_death.pdf | A 100-work death/mortality curriculum. It makes a strong promise that the course will change the reader's remaining years; this is subjective and emotionally intense. Add content notes and remove guaranteed-outcome language. | Withhold; editorial/content-warning and rights review. |
| memento-mori-course.pdf | A 50-work mortality course. It includes emotionally intense material and needs content notes, careful framing and bibliographic verification. | Withhold; content-warning and rights review. |
| sensitive_cinema.pdf | A 253-film guide across sensitive themes. Some “what it teaches” statements are overly absolute; one line frames love containing violence as still love, which risks normalising abuse. Reframe as interpretation and add specific content warnings. | **Not publication-ready — rewrite harmful framing and add content notes.** |
| ultimate_anime_guide.pdf | A 54-work anime guide repeats the known misattributed/misquoted Miyazaki line. Remove it and verify all quotes and recommendations. | Withhold; correct attribution and verify rights. |

## Pine Script review notes

The two `.pine` scripts and legacy `ATH - Pine.txt` were inspected statically; none was compiled or backtested in TradingView.

### ATH - Pine.txt

1. The monthly signal calculations depend on the chart timeframe, so the script must be on a monthly chart; this is not enforced.
2. A weekly exit requested from monthly logic cannot reliably process every weekly close inside the month. The current code can miss an intra-month weekly exit and uses the monthly close for reported P&L.
3. Stored stop-loss and target levels are used for sizing/display, but the code does not actually exit at those levels; the primary exit is the weekly-SMA condition.
4. totalReturnPct, CAGR and drawdown are not valid account-level metrics because per-leg percentage returns are compounded without position-size/capital weighting.
5. The script is an indicator with custom simulated trades, not a TradingView strategy backtest. Do not treat its metrics as a Strategy Tester result.

### Crypto_Trend_Rider_4H.pine

1. Entry, exit, partial and alert conditions are not consistently restricted to confirmed 4-hour bars; intrabar signals can repaint or alert before the bar closes.
2. The Chandelier candidate can move down as the rolling high/ATR changes; a long trailing stop should normally ratchet and never loosen.
3. The initial stop used for sizing is not the same as an enforced stop exit; exits are close-based and may not represent stop-order fills.
4. Partial exits count as separate trade events, so win rate, average R and holding-period statistics are not position-level metrics.
5. Fees, slippage, spread and crypto funding are not modelled. The indicator is not a strategy backtest.

## Required before any source document is published

1. Confirm authorship, licence or written permission for every source file and every substantial third-party description, poem, quote or excerpt.
2. Reconcile counts and duplicates across the film, manga and reading collections.
3. Correct the high-priority factual/editorial problems listed above.
4. Visually inspect the PDFs with table/column extraction problems and the rating glyph issue.
5. Verify all external URLs and time-sensitive streaming claims.
6. Keep all originals withheld until the above checks are complete.


### Official references for the cybersecurity reporting-timeline correction

- GDPR, Article 33: https://eur-lex.europa.eu/eli/reg/2016/679/oj#art_33
- NIS2, Article 23: https://eur-lex.europa.eu/eli/dir/2022/2555/oj#art_23
- DORA, Commission Delegated Regulation (EU) 2025/301, Article 5: https://eur-lex.europa.eu/eli/reg_del/2025/301/oj/eng#art_5


### Official TradingView references for the Pine findings

- Lower-timeframe request.security() returns one intrabar per chart bar; request.security_lower_tf() returns an array of available intrabars: https://www.tradingview.com/pine-script-docs/faq/other-data-and-timeframes/
- barstate.isconfirmed is true on the closing update of a realtime bar, but does not work inside a request.security() call: https://www.tradingview.com/pine-script-docs/concepts/bar-states/


## Pine remediation follow-up — 18 November 2026

### Crypto_Trend_Rider_4H.pine — proposed correction in PR #14

The source revision in [PR #14](https://github.com/piyushimself/files/pull/14) now:

- gates entries, add-ons, partial exits, full exits and alerts on confirmed 4-hour bars;
- ratchets the long Chandelier stop upward and evaluates the prior bar's stop against the current bar, avoiding same-bar look-ahead from a newly raised stop;
- enforces a shared stop using the ratcheted Chandelier and the initial stops of all open legs, with gap-down fills assumed at the bar open;
- uses a high-touch target fill assumption, with stop/EMA exits taking priority when both conditions occur in one bar;
- rolls partial realized P&L into the parent leg so reported trade counts, win rate, R multiple and holding duration are based on completed legs;
- adds configurable fee, slippage and funding-cost estimates; and
- labels drawdown as closed-leg drawdown rather than implying mark-to-market account drawdown.

A CI static-invariant check was added for these source properties. **This is not a Pine compiler or Strategy Tester result.** The revision remains an indicator-based simulation. PR #16 proposes a per-side spread-cost estimate and caps the partial target at 99%; its current branch is diverged/dirty, and the last passing workflow tested an older SHA, not the current head. A refreshed branch and fresh CI run are required before accepting that follow-up. TradingView compilation/backtesting and exchange-specific fee, spread, slippage and funding calibration remain external acceptance steps; do not present displayed results as validated strategy performance.

### ATH weekly replacement — code correction merged; external validation pending

PR #15 replaced the former indicator with `ATH_Weekly_Confirmed_Strategy.pine` and changed `ATH - Pine.txt` into a deprecation notice. The replacement requires a weekly chart, consumes the prior confirmed monthly candle, advances monthly state on the first weekly bar of a new month, and submits Strategy Tester entry/stop/limit orders. It delegates account-level P&L and drawdown to TradingView Strategy Tester rather than compounding per-leg percentages.

Repository CI checks static source invariants only. No TradingView compiler result, Strategy Tester report, symbol-specific historical backtest, Bar Magnifier sequencing review, or broker/exchange cost calibration is available. These are explicit external dependencies. The strategy must not be described as compiled, backtested, profitable, or live-ready until those tests are performed on the intended symbols and venue settings.

## Source-PDF correction pass — corrected files, not publication-cleared

A high-confidence correction pass has been applied to the following source PDFs. The modified pages listed below were visually inspected in rendered output. This is not a complete visual review of every page, a full fact-check of every record, or a rights clearance. **All source files remain withheld from GitHub Pages.**

| Source | Correction applied | Validation and remaining limitation |
|---|---|---|
| `masters_of_e_art_cinema.pdf` | Corrected the false claim that Jane Campion is the only woman to win the Palme d'Or; the text now says she was the first woman to win, for *The Piano* in 1993. | Corrected page 10 visually inspected. Other biographical/interpretive claims still need source checks. |
| `sensitive_cinema.pdf` | Replaced the harmful “love that contains violence is still love” framing with a family-violence content note stating that violence is not proof of love. | Corrected page 24 visually inspected. Full catalogue still needs content-warning and interpretation review. |
| `definitive_anime_encyclopedia.pdf`, `ultimate_anime_guide.pdf` | Removed the known misattributed/misquoted Miyazaki line and substituted original editorial taglines. | Corrected quote pages visually inspected. Other quotations remain unverified. |
| `complete_movie_ratings.pdf` | Corrected cover and section counts to 218 unique films: 98 Essential, 33 Erotic Art and 87 Anime. | Cover and changed section pages visually inspected. Rating provenance and as-of dates remain missing. |
| `complete_movie_ratings_647.pdf` | Corrected 647 “unique titles” to 647 ranked category entries / 629 distinct films under the documented title-director-year rule; corrected methodology, page 36 unique-film metrics, page footers and final tagline. | Pages 1, 2, 36 and 39 visually inspected. Parser validates all ranks 1–647 and identifies 18 repeat groups. Ratings source URLs/as-of dates remain unresolved. |
| `complete_movie_encyclopedia.pdf` | Replaced the stale 2025 “verified” streaming claim with a historical-notes / not-current-availability disclaimer. | Pages 2 and 55 visually inspected. Individual platform availability was not rechecked live; keep entries labelled historical. |
| `Cybersecurity_Stories_For_Your_Teams.pdf` | Corrected GDPR, NIS2 and DORA reporting timelines and removed the generic “72-hour” ransomware countdown. | Pages 15 and 17 visually inspected against the official references above. Incident classification and legal interpretation remain organisation-specific. |
| `Three_Year_Old_Reading_Guide (1).pdf`, `World_Stories_3YearOld_Guide.pdf` | Removed unsupported neural-pathway claims and replaced left-to-right reading advice with script/language-aware guidance. The first guide's headings no longer claim “10 minutes beats 1 hour” or a universal left-to-right habit. | Modified page 15 visually inspected after final typography pass; em-dash glyph issue was corrected to colons. Other developmental claims in both guides still need careful review. |

## Reproducible 647-row ratings audit

- `tools/manifest_movie_ratings_647.py` parses the 647 ranked table rows and validates the full rank sequence and required fields.
- `FILM-RATINGS-647-MANIFEST.csv` contains one row per ranked entry, canonical rank, duplicate group and repeat marker.
- `FILM-RATINGS-647-AUDIT.json` records 647 ranked entries, 629 unique films under the explicit title/director/year rule, 18 duplicate groups and recalculated unique-film statistics (IMDb mean 7.58, RT mean 88%, 26 IMDb 8.5+, 184 IMDb 8.0+, 53 unique 100% RT films; the appendix has 55 ranked rows).
- Parenthetical title suffixes are stripped only when they are a year, a recognized source category, a director-name suffix, or the known alternate-title label “Laputa”. Other parenthetical title text is preserved.
- This rule is reproducible but is not a global film-database identity resolver. Rating sources and as-of dates remain missing.

The corrections and audit are on branch `source-pdf-corrections-clean` and are being submitted for review. The source PDFs remain excluded from the public Pages site until rights/ownership evidence is established.


## Additional visual QA findings and correction — 19 November 2026

The first direct high-resolution review of the corrected-PDF artifact found layout defects on page 15 of both toddler guides. These have now been corrected in the source PDFs and re-rendered:

- `Three_Year_Old_Reading_Guide (1).pdf`: tip 10 is now centered on one line in its badge; the two unsupported footer glyphs after “Happy reading.” have been removed without leaving a cover-up rectangle.
- `World_Stories_3YearOld_Guide.pdf`: tip 10 is now centered on one line in its badge.

**Validation evidence:** correction workflow [run 44381955172](https://github.com/piyushimself/files/actions/runs/44381955172) completed successfully. Its `toddler-guide-pdf-layout-fixes` artifact (ID `14464436487`) contains fresh 1.5× page-15 renders of both PDFs. Both renders were inspected at full size; the two-digit badges are legible on one line and the first guide's closing panel has no missing-glyph squares or residual patch. The workflow reran the correction script against already-corrected PDFs without error.

The correction script's two page-2 whitespace-normalization expressions were also corrected from a literal backslash-s match to actual whitespace matching. This improves its repeat-run checks.

This closes only the newly discovered page-15 layout findings. Other developmental claims, bibliography/metadata, cultural scope, all remaining page layouts, rating provenance and rights clearance remain open as listed elsewhere in this review. All source PDFs remain withheld from GitHub Pages.


## Inventory reconciliation — 19 November 2026

The repository root contains 49 source artifacts for this review: 43 PDFs, 3 DOCX files, 1 legacy `.txt` file and 2 `.pine` scripts. The two combined-film PDFs are byte-identical, so the inventory represents 48 unique source documents after that one duplicate pair. `top500_manga.html` is a separate byte-identical HTML alias of `top500_adult_manga.html`; it is handled by the generated-site publishing review, not counted as a PDF/DOCX/TXT/Pine source document. The publishing report's 50 withheld items includes this duplicate HTML alias as well as the 49 source artifacts. No source is approved for publication.
