# Source-document content review

## Current audit and workflow-artifact note — 26 November 2026, 20:47 IST (Asia/Kolkata)

- Latest main: `d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`; PR #26 and #27 are merged; main workflow #356 / run 45794785456 passed build and Pages deployment.
- The corrected Personal Reference PDF preview is artifact [15104820560](https://github.com/piyushimself/files/actions/runs/45794785456): 20 pages, 117 vector-glyph replacements, zero remaining ZapfDingbats spans; pages 3 and 14 were rendered and inspected. Original source is unchanged.
- Main workflow #356 also uploaded artifact [15103848500](https://github.com/piyushimself/files/actions/runs/45794785456), with 49 extracted source-text files, manifest, summary and README. The extracted text totals approximately 5.46 million characters / 915,935 words. All 49 manifest records show an empty `redactions` map (zero redaction events); therefore the artifact must not be described as a verified sanitized copy. Its expiry is 2026-11-27 09:46:13 UTC.
- A follow-up branch `remediation/stop-public-source-review-artifacts-2026-11-26` removes the extracted-text artifact upload and the PR-only upload of source PDFs. The current main workflow still contains those upload steps until that PR is merged and a subsequent main run verifies the change.
- All 49 source artifacts remain withheld from Pages because publication permission evidence is absent. The repository itself is public, so the originals remain accessible in GitHub; Pages exclusion is not private storage.
- This extraction/triage does not establish line-by-line factual accuracy, publication rights, full visual review or source-to-output completeness.

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
| 1000_Creative_Educational_Cultural_Links.pdf | A large resource directory with descriptions and URLs. The 1,000 numbered entries are present with unique sequential numbers, and the contents section counts sum to 1,000; however, the cover says 30 categories while the contents enumerates 36 category headings. The document's “verified/safe” framing is not substantiated by a current link check. Links can be dead, redirected, changed or unsafe over time. | Withhold; reconcile the category count, validate all links and soften “verified” claims. |
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
| Crypto_Trend_Rider_4H.pine | PR #14 added confirmed-bar gating, a ratcheting long stop, enforced stop logic, parent-leg partial accounting and configurable fee/slippage/funding estimates. PR #20 added spread estimates on entry, partial exit and final exit, capped partial allocation at 99%, corrected cost labels and added static assertions for all three cost paths. Exact-head workflow #272 passed. It remains an indicator simulation, not a Strategy Tester strategy; it has not been compiled/backtested in TradingView or calibrated to a specific venue. | Withhold from performance/live-use claims until TradingView compilation, symbol-specific backtests and venue-specific fill/cost calibration are complete. |
| Cybersecurity_Stories_For_Your_Teams.pdf | Corrected GDPR, NIS2 and DORA reporting timelines and removed the generic “72-hour” ransomware countdown. Pages 15 and 17 were visually inspected against the official references listed below. Incident classification and legal interpretation remain organisation-specific. | Withhold pending legal/security review and rights confirmation. |
| Cybersecurity_Storytelling_Movies.pdf | Movie-to-security mappings are illustrative, not technical controls. Cost and impact claims (e.g. BEC/phishing losses) lack citations. Add sources and label analogies clearly. | Withhold; fact-check and source claims. |
| Films_That_Open_New_Human_Domains.pdf | A 200-film thematic list with strongly interpretive descriptions. Separate subjective interpretation from verifiable facts and establish rights for descriptions. | Withhold; editorial/source review. |
| Free_Art_Resource_Library.docx | Resource directory contains at least one missing URL and time-sensitive audience/subscriber claims. Every link and access/licence statement needs checking. | Withhold; repair missing links and verify resource licences. |
| Global_Kids_Books_Complete_Guide.pdf | Substantial overlap with the “FINAL” reading guide (roughly 55% token-set similarity). Original 30-page A4 source had table overflow on pages 4–12 and 14–28. PR #23 is merged; exact-head workflow #347 and main workflow #348 validated a separate 29-page, 743.2 pt-wide output with 11 repaired number cells, zero horizontal overflow and zero remaining stacked-number pairs; original page 13 was verified blank and removed from the generated copy. The corrected PDF is created in a temporary directory and is not retained as a durable artifact. The eight age-band counts still total 317, not the cover’s “600+” claim; substantial overlap with the FINAL guide and uncited/overgeneralised developmental claims remain unresolved. | Layout defect corrected and CI-validated in a separate generated output; source remains withheld and unchanged. Still reconcile the 600+ count and FINAL version, verify age suitability/metadata, and source or soften developmental claims. |
| Global_Kids_Reading_Guide_FINAL (1).pdf | Near-duplicate of the complete guide, with overlapping age bands and recommendations. Choose one canonical version and merge only genuinely unique entries; verify age suitability and book metadata. | Withhold; consolidate and source-check. |
| Personal_Reference_Film_Books_Art.pdf | A 49-entry personal reference with adult/erotic cinema. The visible ZapfDingbats placeholder defect is corrected in a separate vector-preserving 20-page preview: 117 glyph spans replaced, zero ZapfDingbats spans remain, numeric rating/page values preserved, and rendered pages 3 and 14 visually inspected from workflow artifact [15104820560](https://github.com/piyushimself/files/actions/runs/45794785456). The original upload is unchanged. Rating source URLs, collection/as-of dates and mature-content labelling remain missing. | Generated glyph correction validated; original source remains withheld. Rating provenance, mature-content labelling and publication permissions remain open. |
| Reading_Course_Emotions_Wonder.pdf | A 40-book reflective course. Strong outcome promises are subjective and should be reframed as intentions, not guaranteed personal transformation. | Withhold; soften claims and verify bibliographic details. |
| Three_Year_Old_Reading_Guide (1).pdf | Removed the unsupported neural-pathway claim and replaced universal left-to-right reading advice with script/language-aware guidance. Page 15 badge/footer layout was corrected and visually inspected. Other developmental claims, age suitability, bibliography and consolidation with the near-duplicate guide remain open. | Withhold pending developmental/source review, consolidation and rights clearance. |
| World_Stories_3YearOld_Guide.pdf | Removed the shared unsupported neural-pathway claim and replaced universal left-to-right reading advice with script/language-aware guidance. Page 15 badge layout was corrected and visually inspected. Other developmental claims, table layout, age suitability and consolidation with the near-duplicate guide remain open. | Withhold pending developmental/source review, consolidation and rights clearance. |
| asian_books_curriculum.pdf | The 31-page, 6-arc × 50 curriculum contains at least 25 literal “Placeholder” markers across pages 3–16, 24 and 27, plus 40 “Not Asian” statements across pages 3–16 and 23–24. Several non-Asian entries are followed by same-rank replacement entries; other global works are explicitly retained as “irreplaceable”. The stated 300 therefore cannot be assumed to mean 300 distinct titles without reconciling repeated/reread entries and numbering. The scope is mixed: Asian literature plus deliberate global comparators. | **Not publication-ready — editorial decision required: either retitle/reframe as comparative Asian and world literature or enforce an Asian-only scope. Remove placeholder copy, reconcile numbering/repeats, verify bibliographic and cultural classifications, and obtain rights evidence. Do not automatically delete global comparators.** |
| asian_cinema_curriculum.pdf | A 200-film curriculum with interpretive commentary. Verify country/region classifications, titles, directors and cultural framing; add sources for factual claims. | Withhold; source and editorial review. |
| cinema_900 (1).pdf | Internal contradiction: the cover lists 100 films in each of three lists (300 total), while the contents and section introductions say 300 films per list (900 total). The contents' regional subtotals add to 300 for each list, supporting the 900 framing, but the cover is materially wrong. The extracted list sections also show numbering extending well beyond 100. The separate library-3 collection reports 835, likely a de-duplicated/overlap-adjusted count, but that relationship is not documented. | **Not publication-ready — correct cover and reconcile 900 raw entries against 835 library entries; state duplicate policy.** |
| complete_movie_encyclopedia.pdf | Replaced the stale 2025 “verified” streaming-availability claim with a historical-notes / not-current-availability disclaimer. Pages 2 and 55 were visually inspected. The 647-versus-649 count discrepancy with library-3 remains unresolved. | Withhold pending count reconciliation, source checks and rights review. |
| complete_movie_ratings.pdf | The cover and section labels now report 218 films: 98 Essential, 33 Erotic Art and 87 Anime. The cover and changed section pages were visually inspected. Rating-source URLs and as-of dates remain missing. | Withhold pending rating provenance, date and rights review. |
| complete_movie_ratings_647.pdf | Corrected the 647 ranked category entries / 629 distinct films distinction under the documented title-director-year rule, methodology, page 21 heading, page 36 unique-film statistics and footers. Parser validates ranks 1–647 and 18 repeat groups; pages 1, 2, 21, 36 and 39 were visually inspected and ranking pages 21–35 reviewed as a contact sheet. Rating-source URLs/as-of dates and full row-level fact-check remain missing. | Withhold pending rating provenance, date, full row review and rights clearance. |
| definitive_anime_encyclopedia.pdf | The known misattributed/misquoted Miyazaki line was removed and replaced with an original editorial tagline. The corrected quote page was visually inspected; other quotations and factual claims remain unverified. | Withhold pending quote, factual and rights review. |
| library-3.pdf | A 4,942-item personal film/art library. Its top-level category totals add to 4,942, but subcollection counts conflict with other files (900 vs 835; 647 vs 649). It aggregates overlapping collections and sensitive material. Its 900-slot world-cinema source is represented as 835 in the combined library, and the film encyclopedia appears as 649 there versus 647 in its standalone file. | Withhold; reconcile source-of-truth counts, duplicates and rights. |
| manga_recommendations.pdf | A short recommendation list includes mature romance/manhwa titles. Confirm age suitability and the rights to descriptions. | Withhold; mature-content label and rights review. |
| masters_of_art.pdf | A 25-artist guide with biographical and work descriptions. Verify dates, works, quotes and image/description rights. | Withhold; fact-check and rights review. |
| masters_of_e_art_cinema.pdf | The false claim that Jane Campion was the only woman to win the Palme d'Or was corrected to say she was the first woman to win, for *The Piano* (1993). Corrected page 10 was visually inspected. The 18+ notice, other biographical claims, attribution and rights still need review. | Withhold pending an 18+ notice, remaining fact/rights review. |
| meditation_on_death.pdf | A 100-work death/mortality curriculum. It makes a strong promise that the course will change the reader's remaining years; this is subjective and emotionally intense. Add content notes and remove guaranteed-outcome language. | Withhold; editorial/content-warning and rights review. |
| memento-mori-course.pdf | A 50-work mortality course. It includes emotionally intense material and needs content notes, careful framing and bibliographic verification. | Withhold; content-warning and rights review. |
| sensitive_cinema.pdf | The harmful “love that contains violence is still love” framing was replaced with a family-violence content note stating that violence is not proof of love. Corrected page 24 was visually inspected. The rest of the catalogue still needs content-warning and interpretive review. | Withhold pending full content-warning, factual and rights review. |
| ultimate_anime_guide.pdf | The known misattributed/misquoted Miyazaki line was removed and replaced with an original editorial tagline. The corrected quote page was visually inspected; other quotations and factual claims remain unverified. | Withhold pending quote, factual and rights review. |

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

A CI static-invariant check covers these source properties. PR #20 was rebuilt on current main and merged as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`; exact-head workflow #272 passed. It adds per-side spread to entry, partial-exit and final-exit costs, caps partial allocation at 99%, and distinguishes per-side trading costs from 8-hour funding. This remains an indicator-based simulation, not a Strategy Tester strategy. TradingView compilation/backtesting, order sequencing and exchange-specific fee, spread, slippage and funding calibration remain external acceptance steps; do not present displayed results as validated strategy performance.

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

The corrections and audit are on branch `source-pdf-corrections-final` in PR #19 and remain subject to the limitations documented below. The source PDFs remain excluded from the public Pages site until rights/ownership evidence is established.


## Additional visual QA findings and correction — 19 November 2026

The first direct high-resolution review of the corrected-PDF artifact found layout defects on page 15 of both toddler guides. These have now been corrected in the source PDFs and re-rendered:

- `Three_Year_Old_Reading_Guide (1).pdf`: tip 10 is now centered on one line in its badge; the two unsupported footer glyphs after “Happy reading.” have been removed without leaving a cover-up rectangle.
- `World_Stories_3YearOld_Guide.pdf`: tip 10 is now centered on one line in its badge.

**Validation evidence:** correction workflow [run 44381955172](https://github.com/piyushimself/files/actions/runs/44381955172) completed successfully. Its `toddler-guide-pdf-layout-fixes` artifact (ID `14464436487`) contains fresh 1.5× page-15 renders of both PDFs. Both renders were inspected at full size; the two-digit badges are legible on one line and the first guide's closing panel has no missing-glyph squares or residual patch. The workflow reran the correction script against already-corrected PDFs without error.

The correction script's two page-2 whitespace-normalization expressions were also corrected from a literal backslash-s match to actual whitespace matching. This improves its repeat-run checks.

This closes only the newly discovered page-15 layout findings. Other developmental claims, bibliography/metadata, cultural scope, all remaining page layouts, rating provenance and rights clearance remain open as listed elsewhere in this review. All source PDFs remain withheld from GitHub Pages.


## Inventory reconciliation — 19 November 2026

The repository root contains 49 source artifacts for this review: 43 PDFs, 3 DOCX files, 1 legacy `.txt` file and 2 `.pine` scripts. The two combined-film PDFs are byte-identical, so the inventory represents 48 unique source documents after that one duplicate pair. `top500_manga.html` is a separate byte-identical HTML alias of `top500_adult_manga.html`; it is handled by the generated-site publishing review, not counted as a PDF/DOCX/TXT/Pine source document. The publishing report's 50 withheld items includes this duplicate HTML alias as well as the 49 source artifacts. No source is approved for publication.


### Asian-books curriculum follow-up — 19 November 2026

A fresh extraction of `asian_books_curriculum.pdf` confirmed the placeholder issue is broader than the single example previously recorded: 25 literal “Placeholder” markers and 40 “Not Asian” statements appear in the extracted text. These counts are text-marker counts, not counts of unique invalid books; several are paired replacement instructions and some describe intentionally retained comparative works. Pages with explicit placeholder markers are 3–16, 24 and 27. The content owner/editor must decide whether the intended scope is a comparative Asian/world curriculum or a strict Asian-literature curriculum before a safe rewrite can be made. Until that editorial intent is established, the PDF remains withheld and the issue is actionable but not safely auto-resolvable.


## Crypto Trend Rider cost-accounting follow-up — 19 November 2026

PR [#20](https://github.com/piyushimself/files/pull/20) was merged as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0` after exact-head workflow [#272](https://github.com/piyushimself/files/actions/runs/44434546875) passed. The source now applies the configurable per-side spread estimate to entry, partial-exit and final-exit notional, caps the partial target at 99% so a nonzero leg remains, and labels per-side trading costs separately from 8-hour funding. Static assertions cover each of the three spread-cost paths. Chromium QA recorded 34 desktop pages, 68 mobile page checks and zero automated issues.

This does not compile the Pine source in TradingView, convert the indicator into a Strategy Tester strategy, validate order sequencing, or calibrate fees/spread/slippage/funding to an exchange. The displayed trade simulation remains unvalidated performance data; external TradingView and venue-specific tests are still required.


## Latest correction and CI checkpoint — 19 November 2026

PR #19 was merged as `0699b3a10090ddb9c018ba37116078597d8b0ccd` after exact-head workflow [#299](https://github.com/piyushimself/files/actions/runs/44436114541) passed. Its corrected-source-PDF validator, build, generated-app checks, Pine static checks and Chromium suite passed. The browser report records 34 desktop pages, 68 mobile checks, 96 iframe loads and zero automated issues. The deploy job was skipped on the PR event.

The corrected-PDF artifact includes the 43-PDF review set. Selected changed pages from the ten corrected PDFs were rendered and visually inspected; this does not constitute page-by-page review of all 43 PDFs or all 3 DOCX files. All 49 source artifacts (48 unique documents after one exact duplicate PDF pair) remain withheld from Pages and are not rights-cleared.

Main workflow [#283](https://github.com/piyushimself/files/actions/runs/44435251703) completed successfully, including Pages deployment, for the preceding main commit `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`. It predates PR #19's merge; a fresh main run for `0699b3a10090ddb9c018ba37116078597d8b0ccd` is required to confirm deployment of these corrections.

The following remain unresolved: Asian-books scope decision; Cinema 900 and other collection-count reconciliation; resource URL/licence checks; bibliography, quotation and metadata attribution; rating-source URLs/as-of dates; remaining document page/layout/OCR and factual review; ownership/republication evidence; and TradingView/venue-specific Pine validation. See `REMEDIATION-STATUS.md` for the consolidated acceptance ledger.


## Main-branch deployment checkpoint — 19 November 2026

Main workflow [#305](https://github.com/piyushimself/files/actions/runs/44442583472) passed build, generated-app validation, Pine static checks, corrected-source-PDF validation, redacted extraction, Chromium QA and GitHub Pages deployment for main commit `0bbe318ae4341aa16393ff95d9dd24452bed46d7`. The browser report records 34 desktop pages, 68 mobile page checks, 96 iframe loads and zero automated issues. The latest browser and Pages artifacts were downloaded and inspected. The Pages artifact contains no PDF, DOCX or Pine source files; `robots.txt` is the only `.txt` file. This confirms source exclusion from the published artifact, not rights clearance or repository privacy.

The 49 source artifacts (48 unique source documents after the exact duplicate PDF pair) remain withheld. The per-file findings above remain open where stated. In particular, no permission evidence has been supplied; the Asian-books scope decision, Cinema 900 deduplication rule, collection-count reconciliations, resource/licence/attribution checks, rating provenance and remaining factual/layout review are not cleared by this deployment. The TradingView and venue-specific Pine tests remain external. The latest status ledger is `REMEDIATION-STATUS.md`.


## Global Kids Books table-layout correction — 22–23 November 2026

The original source PDF has 30 pages. A page-by-page drawing-bounds audit found table overflow on pages 4–12 and 14–28: x=-73.46 to x=668.74 points on A4 pages only 595.28 points wide. Original page 13 was verified genuinely blank.

PR [#23](https://github.com/piyushimself/files/pull/23) was merged. Its exact-head workflow [#347](https://github.com/piyushimself/files/actions/runs/45028369149) passed, and main workflow [#348](https://github.com/piyushimself/files/actions/runs/45028369149) passed the corrected-PDF validator for main SHA `386618942e54979ecf8cd389153f34e5ef4d3841`.

The separate generated output widens all pages to 743.2 points without scaling or rasterizing, repairs 11 vertically wrapped two-digit row numbers, and removes the genuinely blank original page 13. Validation reports 29 pages, 44,394 extracted characters (from 34,670), zero horizontal-overflow pages and zero remaining stacked-number pairs. The full 29-page contact sheet and full-size renders of all six affected pages were inspected.

The validator generates the corrected PDF in a temporary directory and deletes it after validation; no durable corrected-PDF artifact is retained. The original uploaded source remains unchanged and withheld from GitHub Pages.

**Editorial findings remain open:** the eight age-band counts total 317 rather than the cover's “600+” claim; the guide has roughly 55% token-set overlap with the FINAL guide; and the introduction contains uncited, overgeneralised developmental claims. Age suitability, bibliographic metadata and the canonical version also require review. Layout validation does not close these content findings or establish publication rights.

