# Reading Room remediation — current status

**Status: IN PROGRESS — not a completion certificate.**  
**Last verified:** 19 November 2026, approximately 07:38 IST  
**Repository:** [piyushimself/files](https://github.com/piyushimself/files)  
**Published site:** https://piyushimself.github.io/files/

## Current repository state

- Current `main` after the source-correction merge: `0699b3a10090ddb9c018ba37116078597d8b0ccd`.
- PR [#19](https://github.com/piyushimself/files/pull/19) was squash-merged as this commit. It applies ten narrowly scoped source-PDF corrections, adds the reproducible 647-row film manifest/audit and validator, reconciles the source inventory, fixes three generated homepage catalogue/search metadata mismatches, and refreshes the review documentation.
- PR [#20](https://github.com/piyushimself/files/pull/20) was merged earlier as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`. It adds per-side spread-cost estimates to entry, partial-exit and final-exit legs and caps partial allocation below 100%. PR #16 was closed as superseded.
- PR [#17] age-gate QA fix is included in main at `1903c3787156523193380affa23b13ed4c6d2e11`.
- No open pull requests were present immediately after PR #19 merged.

## Latest CI and browser evidence

### PR #19 exact-head validation

[Workflow #299](https://github.com/piyushimself/files/actions/runs/44436114541), head `0f3bc8f57e0a0381397a5b8ce6f1d477e2102e0e`, completed successfully. Build, generated-app syntax checks, Pine static checks, corrected-PDF validator, redacted extraction, Chromium QA and artifact uploads passed. Deploy was skipped because this was a pull-request event.

The browser report recorded:

- 34 desktop collection pages and 68 mobile page checks;
- 96 iframe loads;
- 20 search, 14 select, 15 filter, 3 tab and 4 shell controls;
- 7 direct mature-app gates and 21 mature iframe-sync checks;
- 34 reader menus, 204 mobile reader controls and 63 filter disclosures;
- 33 theme, 32 font and 32 text-scale synchronisation checks; and
- **zero automated issues**.

The latest browser artifact was downloaded. Contact sheets covering all 34 wrapper pages at desktop, tablet and mobile sizes, plus the 33 available app-mobile captures, were visually swept. This is a page-level visual sweep, not a pixel-level review of every control or every state. The corrected-source-PDF artifact was also inspected; selected changed pages in the ten corrected PDFs were rendered and visually checked. It does not mean every page of every source PDF has been reviewed.

### Main-branch deployment before PR #19

[Main workflow #283](https://github.com/piyushimself/files/actions/runs/44435251703), for commit `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`, completed successfully, including its GitHub Pages deployment. Its Chromium report recorded the same 34 desktop / 68 mobile / 96 iframe coverage and zero automated issues.

**Important:** PR #19 merged after workflow #283. A fresh main-branch build, regression run and Pages deployment for `0699b3a10090ddb9c018ba37116078597d8b0ccd` had not yet appeared in the run list at this checkpoint. Do not claim the PR #19 merge is deployed until that new main run completes successfully.

### Artifact publication check

The PR #19 Pages artifact was inspected. It contained 34 published HTML collections and 123 artifact entries. It contained no PDF, DOCX, Pine or source-document files; `robots.txt` was the only `.txt` match. The publishing review lists 50 withheld items: the 49 source artifacts plus the duplicate HTML alias. This confirms exclusion from the Pages artifact only; it does **not** make root-level repository files private.

Independent live HTTP verification of the Pages hostname failed with a DNS-resolution error in this runtime. That is an environment limitation and does not establish that the site is down.

## Corrections merged

PR #19's corrected PDFs and reproducible audit cover:

- Jane Campion's Palme d'Or record;
- harmful violence-as-love wording in Sensitive Cinema;
- the known misattributed Miyazaki quotation in two anime guides;
- the 218-film section counts;
- the distinction between 647 ranked category entries and 629 distinct films under an explicit title/director/year matching rule (18 repeat groups);
- stale 2025 streaming-verification wording;
- GDPR, NIS2 and DORA reporting timelines and the generic ransomware countdown;
- unsupported toddler-reading neuroscience and universal left-to-right reading claims; and
- the two toddler-guide page-15 badge defects and missing footer glyphs.

The ratings parser validates ranks 1–647 and the manifest records the matching rule. The rule is reproducible but is not a global film-database identity resolver. IMDb/Rotten Tomatoes source URLs and rating as-of dates remain missing.

Generated homepage catalogue/search metadata now agrees with the verified app data for 296 animated films, 1,629 Complete Film Collection records and Big Library's 98-of-4,942 initial state. Validator assertions guard these values; original uploaded HTML sources were not modified.

PR #20's spread-cost correction is covered by static assertions for entry, partial exit and final exit. This is not TradingView compilation or backtesting.

## Findings still open

### Source content, counts and editorial decisions

- `asian_books_curriculum.pdf`: at least 25 literal placeholder markers and 40 “Not Asian” statements were found. These are marker counts, not unique invalid-title counts. A content-owner decision is needed on whether the intended work is comparative Asian/world literature or a strict Asian-literature curriculum.
- `cinema_900 (1).pdf`: the cover's 100 × 3 = 300 conflicts with the body’s 300 × 3 = 900; `library-3.pdf` reports 835 for the corresponding collection. The deduplication/reconciliation rule is not settled.
- `1000_Greatest_Fictional_Books.pdf`: 36 contents sections versus 26 on the cover; 857 unique title lines from 1,000 slots (143 repeats); memoir/non-fiction mixed into a “fictional books” list.
- `1000_Inspirations.pdf`: 1,001 numbered items and a section labelled 201 despite the 1,000 claim.
- `1000_Writing_Prompts.docx`: 835 prompts, not 1,000.
- `2000_Inspirations (1).pdf`: section counts total 1,462, not 2,000.
- `200_Films_Like_Frida.pdf`: 220 numbered entries and 218 unique title lines despite the 200-film title.
- `300_Films_Filmography.pdf`: 298 extracted entry lines although numbering reaches 300; names and diacritics need proofreading.
- `complete_movie_encyclopedia.pdf` versus `library-3.pdf`: 647 versus 649 claims still need a record-level reconciliation.
- Resource URLs, availability claims, licence statements, bibliographies, quotations, author/edition metadata and selection rationales remain incompletely verified.
- Ratings provenance remains unresolved: source URLs and collection/as-of dates are not documented. Do not present the figures as current or independently sourced until this is fixed.
- Remaining PDF/DOCX pages, OCR output, table/column alignment, glyphs and source-to-output completeness have not all received page-by-page human inspection.


### Additional per-file editorial findings still open

The full per-file inventory in `DOCUMENT-CONTENT-REVIEW.md` remains the authoritative detailed register. In addition to the count and scope issues above, these are still actionable and must not be treated as cleared:

- `1000_Creative_Educational_Cultural_Links.pdf`: verify every resource URL and access/licence claim; remove or qualify the unsupported “verified/safe” framing.
- `1000_Google_Searches_Grand_Curiosity_Atlas.pdf`: revise language that exoticises or essentialises living communities and source factual framing.
- `100_essential_films.pdf`, `500_Films_500_Music_Global_Guide.pdf`, `500_Manga_Movies.pdf`, `50_e_art_films.pdf` and `Bold_Cinema_Collection.pdf`: verify selection criteria, descriptions, attribution, mature-content handling and any time-sensitive availability claims.
- `200_prompts_emotion_wonder_v2.pdf`: add appropriate content notes and distinguish reflection prompts from therapeutic advice.
- `200_prompts_mind_detox_v2.pdf` and `200_thinkers_quiet_mind_v2.pdf`: remove implied treatment/cure language, add non-therapy boundaries, and source-check psychological claims and thinker attributions.
- `A_Filmmakers_Reading_List.pdf` and `A_Life_Worth_Living_500_Suggestions.docx`: verify titles, editions, translations, identity/name variants and attributions; distinguish subjective recommendations from facts.
- `Aag_Ki_Kavitayen.pdf` and `All_Film_Collections_Combined_compressed.pdf` (plus its exact duplicate): high rights risk due to poems and extensive third-party descriptions; explicit permission/licence evidence is missing.
- `Cybersecurity_Storytelling_Movies.pdf`: source cost/impact claims and label film-to-security mappings as analogies, not technical controls.
- `Films_That_Open_New_Human_Domains.pdf`: separate subjective interpretations from factual statements and establish rights for descriptions.
- `Free_Art_Resource_Library.docx`: repair the missing URL and verify every resource link, licence and time-sensitive audience claim.
- `Global_Kids_Books_Complete_Guide.pdf` and `Global_Kids_Reading_Guide_FINAL (1).pdf`: reconcile the substantial overlap, inspect column/table layout, establish a canonical version, count titles and verify age suitability and metadata.
- `Personal_Reference_Film_Books_Art.pdf`: visually resolve the rating-glyph extraction issue, then verify mature labels and rights.
- `Reading_Course_Emotions_Wonder.pdf`: reframe guaranteed transformation promises as intentions and verify bibliographic details.
- `Three_Year_Old_Reading_Guide (1).pdf` and `World_Stories_3YearOld_Guide.pdf`: the shared unsupported neuroscience and universal reading-direction claims and the page-15 layout defects were corrected; other developmental claims, age suitability, bibliographies, remaining layouts and consolidation still need review.
- `asian_cinema_curriculum.pdf`: verify country/region classifications, titles, directors and cultural framing; source factual claims.

These items are open work, not all permission-blocked. Rights-dependent publication remains blocked until ownership/licence evidence is supplied. Editorially ambiguous items require a documented scope decision. Do not relabel an unresolved content-quality issue as a rights blocker merely because the source is withheld.

### Page, interaction and accessibility acceptance

`PAGE-AUDIT.md` still has 11 unchecked manual acceptance items. The Chromium suite is broad automated smoke, responsive, console and selected-control coverage, but it does not certify:
- every control on every app and every filter combination;
- keyboard-only completion and focus order;
- screen-reader announcements/semantics;
- formal WCAG contrast and accessibility conformance;
- reduced-motion behavior;
- every page's typography, sticky-header behavior and long-content layout; or
- complete source-to-output semantic fidelity.

The wrapper screenshot contact sheets have been reviewed across desktop/tablet/mobile, and app-mobile captures were swept, but that is not equivalent to exhaustive per-control and accessibility review.

### Rights, privacy and repository exposure

- The inventory contains 49 source artifacts: 43 PDFs, 3 DOCX, 1 legacy TXT and 2 Pine scripts. The exact duplicate PDF pair leaves 48 unique source documents.
- All source documents remain withheld from GitHub Pages. No ownership or republication licence evidence has been established.
- The GitHub repository is public. Root-level files and their Git history remain accessible even when omitted from Pages. Do not claim they are private. Moving them to private storage or changing repository visibility/history requires an informed owner decision; no such change has been made.
- The 100-poem Hindi anthology and extensive third-party film/book descriptions remain high rights-risk material without explicit permission.

### Pine Script and external verification

- The ATH weekly strategy replacement and Crypto Trend Rider remain statically checked only.
- TradingView compilation, Strategy Tester/backtesting, Bar Magnifier/order sequencing, symbol-specific data, and broker/exchange fees, spread, slippage and funding calibration have not been completed.
- Do not claim tested performance, profitability or live readiness. These require an available TradingView/exchange validation path and explicit evidence.

### Independent live-site check

A direct request from this runtime could not resolve `piyushimself.github.io`. Verify the merged site from an independent network after the new main deployment. The DNS failure here is not proof of an outage.

## Next acceptance work

1. Confirm the fresh main workflow for `0699b3a10090ddb9c018ba37116078597d8b0ccd` passes build, Chromium QA and Pages deployment; inspect its artifacts and verify the live site independently.
2. Continue objective count reconciliation and correct source documents where the evidence is sufficient; preserve explicit uncertainty where it is not.
3. Obtain the Asian-books scope decision and Cinema 900 deduplication rule before rewriting those works.
4. Complete the remaining page-by-page interaction, visual and accessibility checks; disposition every one of the 11 manual acceptance items with evidence or a specific blocker.
5. Verify resource URLs, licences, bibliographies, quotations, rating provenance and as-of dates; record source and date for every time-sensitive claim.
6. Obtain rights/ownership evidence or keep sources withheld and make an informed decision about public-repository exposure.
7. Complete external TradingView and venue-specific validation or document each exact dependency and the limits on any performance claims.

**Completion rule:** do not mark this project complete until every actionable finding is corrected and validated or individually documented as blocked by concrete evidence, permissions, an owner decision or an external dependency; the final main-branch regression and deployment are confirmed; the manual acceptance list is fully dispositioned; and this status report is synchronized with the final evidence.
