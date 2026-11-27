# Reading Room remediation handoff

## Latest verified checkpoint — 27 November 2026, 12:06 IST (Asia/Kolkata)

- Default branch `main` remains at [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e). Main workflow [#356](https://github.com/piyushimself/files/actions/runs/45794785456) remains the latest successful production build and Pages deployment for that exact SHA. No post-merge deployment of PR #28 exists.
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open on `remediation/stop-public-source-review-artifacts-2026-11-26`, exact head [`7102b9dfe858175b0cc3a924e2e1be050d6d988a`](https://github.com/piyushimself/files/commit/7102b9dfe858175b0cc3a924e2e1be050d6d988a), 26 commits ahead of main and zero behind. It has no submitted reviews, inline review threads or conversation comments. No merge was performed.
- Exact-head PR workflow [#368](https://github.com/piyushimself/files/actions/runs/45941318571) completed successfully for `7102b9dfe858175b0cc3a924e2e1be050d6d988a`. The build job passed; the deploy job was correctly skipped for a pull-request event. Build, generated-app validation, Pine static checks, corrected-source-PDF validation and Chromium desktop/mobile QA passed.
- The complete #368 build log was inspected. It contains no `tools/document_review_extract.py` step, source-review inventory, per-file source-review output, redaction/OCR inventory or `PUBLISHING-REVIEW.md` upload. The remaining OCR-engine installation is part of the build environment and did not produce the old document-review extraction output.
- Browser QA artifact [15173471615](https://github.com/piyushimself/files/actions/runs/45941318571) was downloaded and inspected. It contains 528 files. Its report records 34 desktop pages, 68 mobile pages, 96 iframe loads, 20 search controls, 14 select controls, 15 filter controls, 3 tabs, 4 shell controls, 7 direct mature-app gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 scale-sync, 63 filter disclosures, 34 reader menus and 204 mobile reader-shell controls. It reports zero automated issues and zero preliminary accessibility warnings. These automated results are not WCAG conformance or assistive-technology certification.
- The #368 Pages preview [15173446808](https://github.com/piyushimself/files/actions/runs/45941318571) was downloaded and inspected: 122 tar entries, 83 regular files and 68 HTML files. No PDF, DOCX, Pine source or internal publishing report/source inventory is present. The only text file is `robots.txt`; `manifest.webmanifest` is expected site metadata.
- Visual inspection of #368 screenshots confirmed readable homepage desktop/mobile captures and the 300 Animated Films mobile middle rows, with ranks 7–16 remaining on one line. The 32 dark-desktop captures include the five previously targeted pages: Asian Cinema Curriculum, The Cinematic Canon, The Fiction of Living and Top 500 Adult Manga appear materially improved; Manga & Comics Archive still looks visually subdued in parts of its filter/sidebar area. The artifact contains dark-desktop captures but no dark-mobile screenshot set. Measured contrast and dark-mode mobile acceptance remain open.
- Existing public artifacts remain unresolved. At this checkpoint, source-review artifact [15103848500](https://github.com/piyushimself/files/actions/runs/45794785456) was still downloadable and expires 27 November 2026 at 09:46:13 UTC (15:16:13 IST). It was downloaded again: its manifest has 49 records, every `redactions` map is empty, and the ZIP contains 49 extracted source-text files plus its README, summary and manifest. It is not a verified sanitized copy. Old browser-QA artifact [15105410621] was also downloaded and still contains `PUBLISHING-REVIEW.md` listing 50 withheld filenames/reasons; it expires 10 December 2026 at 09:56:13 UTC. Source-derived corrected-PDF preview [15104820560] remains downloadable until 10 December 2026 at 09:46:04 UTC. Older Pages artifact [15104822142] remains downloadable until 27 November 2026 at 09:56:16 UTC (15:26:16 IST). The connected GitHub integration exposes no artifact-deletion action; owner deletion or verified automatic expiry is required.
- All 11 manual acceptance items in `PAGE-AUDIT.md` remain unchecked at this checkpoint (unchecked entries: 11; checked entries: 0). They cover full page-by-page desktop/mobile review, interactions, themes/fonts/scaling, sticky controls, measured contrast, keyboard/screen-reader/reduced-motion acceptance, complete PDF/DOCX/OCR inspection, source-to-output completeness, links/images/console/sitemap, catalogue reconciliation and title/H1 fallback behavior.
- Editorial findings remain open: Asian Books scope/placeholders (25 placeholder markers and 40 “Not Asian” statements); Cinema 900 cover/body 300-versus-900 and 835-item comparison; Global Kids Books 317-versus-600+, roughly 55% overlap and uncited developmental claims; other catalogue-count conflicts; URL validation; bibliographies, quotations, attribution, author/edition metadata, age suitability and rating provenance.
- All 49 original source artifacts remain withheld from Pages because publication-permission evidence is absent, but the repository is public and the originals remain accessible through GitHub. Do not change repository visibility, remove originals or rewrite history without the owner's informed decision. Pine static checks pass; TradingView compilation/backtesting and venue-specific calibration remain external dependencies and are not treated as Reading Room website deployment gates.
- **Status: IN PROGRESS — not a completion certificate.** The PR-preview regression is validated, but existing public artifact exposure, incomplete manual acceptance, unresolved editorial findings, missing PR review and missing post-merge production verification remain open.

### Immediate next actions

1. At/after 15:16 IST on 27 November, re-fetch artifact metadata and attempt downloads for #15103848500; record expiry only if GitHub reports `expired: true` and download is unavailable. At/after 15:26 IST, repeat for #15104822142.
2. Keep #15105410621 and #15104820560 on the exposure watch until their December expiries or owner deletion; verify actual unavailability, not just the timestamp.
3. Continue the 11 manual acceptance tasks and editorial dispositions; the current #368 screenshots and zero automated warnings do not close them.
4. Review the remaining Manga & Comics Archive dark-mode filter/sidebar appearance and obtain measured contrast plus dark-mobile visual evidence.
5. Obtain PR review; do not merge solely because #368 passed.
6. After all pre-merge gates are accepted, merge PR #28, run a fresh main workflow, inspect its artifacts, and verify production desktop/mobile behavior and the deployed SHA.



## Superseded checkpoint — 27 November 2026, 10:07 IST (Asia/Kolkata)

- Default branch `main` remains at [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e). Main workflow [#356](https://github.com/piyushimself/files/actions/runs/45794785456) is still the latest production deployment; its build and Pages deploy succeeded for that exact main SHA.
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open on `remediation/stop-public-source-review-artifacts-2026-11-26`, head [`14c750e25f047c066560741687149f60b19fb927`](https://github.com/piyushimself/files/commit/14c750e25f047c066560741687149f60b19fb927), 25 commits ahead of main and zero behind. It changes six files and has no submitted reviews or inline review threads.
- Exact-head PR workflow [#367](https://github.com/piyushimself/files/actions/runs/45939270985) completed successfully for `14c750e25f047c066560741687149f60b19fb927`. The build job passed; the deploy job was skipped correctly for a pull-request event. Build, generated-app validation, Pine static checks, corrected-source-PDF validation and Chromium browser QA all passed.
- The complete #367 build log was inspected. It contains no `document_review_extract.py` step, source-review inventory, per-file source-review output, redaction inventory, OCR inventory or `PUBLISHING-REVIEW.md` upload. The Pages artifact upload lists only the generated site.
- Browser QA artifact [15171859856](https://github.com/piyushimself/files/actions/runs/45939270985) was downloaded and inspected. It contains 528 files. Its report records 34 desktop pages, 68 mobile checks, 96 iframe loads, 20 search controls, 14 select controls, 15 filter controls, 3 tabs, 4 shell controls, 7 direct mature-app gates, 21 mature iframe-sync checks, 33 theme-sync checks, 32 font-sync checks, 32 text-scale checks, 63 filter disclosures, 34 reader menus and 204 mobile reader-shell controls. It reports zero automated issues and zero preliminary accessibility warnings. These are automated checks, not WCAG or assistive-technology certification.
- Targeted #367 dark-desktop screenshots were visually inspected for Asian Cinema Curriculum, The Cinematic Canon, The Fiction of Living, Manga & Comics Archive and Top 500 Adult Manga. Four appear materially improved in the captured view. Manga & Comics Archive still has subdued filter/sidebar labels on its dark brown panel; measured contrast is not yet established. Dark-mode mobile visual acceptance and measured contrast remain open.
- Pages preview artifact [15171864842](https://github.com/piyushimself/files/actions/runs/45939270985) was downloaded and inspected. Its tar contains 122 entries / 83 files, including 68 HTML files. It contains no PDF, DOCX or Pine source files; `robots.txt` is the only TXT file. No internal review report or source-document inventory is present. The preview expires 28 November 2026 at 04:28:52 UTC (09:58:52 IST); browser QA expires 11 December 2026 at 04:28:49 UTC (09:58:49 IST).
- Existing public artifact exposure remains open. Main source-review artifact [15103848500](https://github.com/piyushimself/files/actions/runs/45794785456) is still listed as unexpired at this checkpoint and expires 27 November 2026 at 09:46:13 UTC (15:16:13 IST). It contains 49 extracted source-text files with empty redaction maps; it is not a verified sanitized copy. Main browser QA artifact [15105410621] still contains generated `PUBLISHING-REVIEW.md` and expires 10 December 2026 at 09:56:13 UTC. Main corrected-source-PDF preview [15104820560] expires 10 December 2026 at 09:46:04 UTC. Main Pages artifact [15104822142] expires 27 November 2026 at 09:56:16 UTC (15:26:16 IST). The connected GitHub integration has no artifact-deletion action; owner deletion through GitHub Actions or verified automatic expiry is required.
- All 11 manual acceptance items in `PAGE-AUDIT.md` remain unchecked: page-by-page desktop/mobile review; all interaction states; light/dark themes, fonts and scaling; sticky controls; measured contrast; keyboard focus, reduced motion, accessible labels and iframe titles; complete PDF/DOCX/image-only-page/OCR inspection; source-to-output completeness; links/images/console/sitemap; catalogue reconciliation; and missing-title/H1 fallback review.
- Editorial findings remain open: Asian Books scope/placeholders and 25 placeholder markers / 40 “Not Asian” statements; Cinema 900 cover/body 300-versus-900 and 835-item library comparison; Global Kids Books 317-versus-600+, roughly 55% overlap and uncited developmental claims; other catalogue-count conflicts; URL validation; bibliographies, quotations, attribution, author/edition metadata, age suitability and rating provenance.
- All 49 original source artifacts remain withheld from Pages because publication-permission evidence is absent, but the repository itself is public and the originals remain accessible through GitHub. Do not change repository visibility, remove originals or rewrite history without the owner's informed decision. Pine static checks pass; TradingView compilation/backtesting and venue-specific calibration remain external validation dependencies and are not treated as a Reading Room website deployment gate.
- **Status: IN PROGRESS — not a completion certificate.** A passing PR workflow does not close the artifact, manual, editorial, rights or production acceptance gates. After those gates are dispositioned and PR #28 is reviewed/accepted, a fresh main workflow, production desktop/mobile regression and Pages deployment must be verified.


## Dark-mode visual regression findings — 27 November 2026, 09:46 IST

The #364 browser-QA ZIP was downloaded and inspected locally. Its report records 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls and zero automated issues. A contact-sheet sweep covered all 34 wrapper desktop screenshots and all 34 wrapper mobile screenshots, plus 32 app-content top screenshots and 31 middle / 31 bottom screenshots in both desktop and mobile layouts. No general mobile overflow or clipping pattern was visible in this screenshot sweep. This does not replace interaction testing, measured contrast, keyboard-only testing or screen-reader acceptance.

The dark-desktop screenshot sweep exposed five actionable contrast defects that the automated smoke report did not flag:

1. **Asian Cinema Curriculum:** the dark theme made the hero surface pale while the eyebrow and subtitle remained translucent white.
2. **The Cinematic Canon:** the dark theme made the hero surface pale while the title, subtitle and statistic labels remained white.
3. **The Fiction of Living:** the introduction band became pale while its paragraph remained pale.
4. **Manga & Comics Archive:** dark-mode card descriptions and metadata used fixed dark-brown text on dark surfaces; its paper/ink token mapping also left the sort strip and some text colors inconsistent.
5. **Top 500 Adult Manga:** the dark-mode hero became pale while its small metadata pills retained low-contrast light text.

A page-scoped dark-mode repair was added to `site/assets/unified-app.css`. It changes only the generated shared CSS; original uploaded HTML/PDF/DOCX/source documents were not modified. Exact-head workflow #367 passed after these CSS changes. Targeted dark-desktop screenshots reviewed on 27 November 2026 show material visual improvement on Asian Cinema Curriculum, The Cinematic Canon, The Fiction of Living and Top 500 Adult Manga. Manga & Comics Archive still has subdued filter/sidebar labels on its dark brown panel. Measured contrast and dark-mode mobile review remain open, so the five-page dark-mode acceptance is not closed.

The 11 manual acceptance items remain open. The screenshot sweep is supporting visual evidence only, not a substitute for measured contrast or assistive-technology testing.


## Superseded checkpoint — 27 November 2026, 09:40 IST (Asia/Kolkata)

- Default branch `main` remains at [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e). Main workflow [#356](https://github.com/piyushimself/files/actions/runs/45794785456) completed successfully for that exact SHA; the deploy job created the Pages deployment for `d146196...` and reported success. No newer main commit or production deployment is present.
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open on `remediation/stop-public-source-review-artifacts-2026-11-26`, head [`3b5a65dd651163819b49e7961ce649bdb3e2fa7a`](https://github.com/piyushimself/files/commit/3b5a65dd651163819b49e7961ce649bdb3e2fa7a), based on current main. GitHub compare confirms 20 commits ahead and zero behind. No submitted reviews or inline review threads are recorded.
- Exact-head workflow [#364](https://github.com/piyushimself/files/actions/runs/45919155862) completed successfully for the exact PR head `3b5a65dd651163819b49e7961ce649bdb3e2fa7a` (event: `pull_request`). Build, generated-app validation, Pine static checks, corrected-source-PDF validation and Chromium desktop/mobile QA passed. The deploy job was skipped as expected for a PR event.
- The complete #364 build log contains no document-review extraction step, source-review inventory, source filenames, OCR counts, rights-marker categories or redaction-count output. The unsafe extraction step and associated uploads are absent from the current workflow.
- Browser QA artifact [15163856937](https://github.com/piyushimself/files/actions/runs/45919155862) was generated for #364. The report records 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, zero automated issues and zero preliminary accessibility warnings. This is automated regression evidence, not exhaustive human review, WCAG conformance, keyboard-only or screen-reader certification.
- Pages preview artifact [15163807038](https://github.com/piyushimself/files/actions/runs/45919155862) was generated for #364. The inspected preview contains 122 archive entries / 68 HTML files and excludes source documents and internal review reports. The preview is not a production deployment.
- The four remediation documents and PR description were stale at the prior 06:17 checkpoint; this 09:40 checkpoint supersedes that repository/workflow snapshot. Historical sections below are retained for traceability.
- **Status: IN PROGRESS — not a completion certificate.** Passing exact-head CI and PR-preview regression does not close the manual, editorial, artifact-exposure or production acceptance gates below.


Last updated: 2026-11-27 09:40 IST (Asia/Kolkata)

This file is the durable continuation point for the ongoing Reading Room remediation. Read it before continuing, then inspect live GitHub state because PRs and workflow runs may have changed since this checkpoint.

## Current verified continuation state — 27 November 2026, 06:17 IST (Asia/Kolkata)

- Repository: `piyushimself/files`; default branch `main`; latest main SHA [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e).
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open at head `1e6fab3cd995bf61b6c5cbca1d3a235cb81257ce`; it has 13 commits, no submitted reviews or inline review threads, and no open repository issues.
- Exact-head workflow #359 / run [45882706873](https://github.com/piyushimself/files/actions/runs/45882706873) passed build and Chromium desktop/mobile QA. Deploy was skipped because this is a PR event. The full build log contains no document-review extraction step or source-review inventory output.
- Browser artifact [15148637645](https://github.com/piyushimself/files/actions/runs/45882706873) has 528 files and reports 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, zero automated issues and zero preliminary accessibility warnings. Pages preview [15147284705] has 122 archive entries / 68 HTML files and no source documents or internal reports.
- I downloaded both #359 artifacts, inspected the report and Pages archive, and visually inspected homepage desktop/mobile plus 300 Animated Films middle desktop/mobile screenshots. The homepage is readable and ranks 10–16 stay on one line on mobile. This is sampled visual QA, not full manual acceptance.
- Main workflow #356 / run [45794785456](https://github.com/piyushimself/files/actions/runs/45794785456) remains the latest successful production deployment for SHA `d146196...`. Its deploy log created the Pages deployment for that exact SHA and reported success. #359 did not deploy. Independent live-site HTTP reachability is not confirmed through the external browser.
- Existing main source-review artifact [15103848500] is still downloadable (`expired: false`), contains 49 extracted text files and empty redaction maps, and expires **27 November 2026, 09:46:13 UTC (15:16:13 IST)**. Old browser QA [15105410621] contains the generated `PUBLISHING-REVIEW.md`; main and PR corrected-PDF previews remain downloadable until December. The connected GitHub integration exposes no artifact-deletion operation; owner deletion through GitHub Actions or automatic expiry is required.
- New #359 browser QA artifact expires 10 December 19:27:55 UTC; its Pages preview expires 27 November 19:27:58 UTC (28 November 00:57:58 IST). Earlier PR browser QA [15134060952] expires 10 December 15:32:58 UTC and its Pages preview [15134215945] expires 27 November 15:33:02 UTC.
- Remaining editorial findings: Asian Books scope/placeholders; Cinema 900 300/900/835 discrepancy; Global Kids Books 317-versus-600+ count, ~55% overlap, developmental claims, age/metadata decisions; other count discrepancies; URLs, bibliographies, quotations, attribution, metadata, age suitability and rating provenance.
- All 11 manual acceptance items in `PAGE-AUDIT.md` remain unchecked/incomplete. Automated QA does not prove full keyboard/screen-reader acceptance, measured contrast, reduced-motion behavior, or complete source-to-output review.
- All 49 original source files remain withheld from Pages for lack of publication-permission evidence, but remain accessible in the public repository. Do not change visibility or rewrite history without the user's specific informed confirmation.
- The four remediation documents were refreshed on this branch to record workflow #359 and the actual current artifact/deployment state. The PR description was also refreshed at 06:17 IST; the latest documentation-only head still requires exact-head workflow validation. **Status: IN PROGRESS — not a completion certificate.** Never push directly to `main`; continue on the existing PR branch and inspect exact-head evidence before merging.



The user explicitly authorized autonomous repository work: make necessary changes, test, create PRs, and merge safe fixes. Continue until every actionable finding is corrected and validated or clearly recorded as blocked by evidence, permissions, or an external dependency. Do not ask the user to restate context. Do not claim completion from a successful build alone.

Quality bar:
- Treat each page and source document as its own deliverable.
- Review mobile and desktop, typography, contrast, layout, controls, accessibility, content accuracy and readability.
- Correct root causes; run real browser QA and inspect screenshots/reports.
- Distinguish automated checks from visual/editorial review, factual verification, rights clearance, and external testing.
- Never invent facts, licences, permissions, TradingView results, or source data.

## Repository

- Repo: https://github.com/piyushimself/files
- Pages site: https://piyushimself.github.io/files/
- Default branch: main
- Public repository. Withholding originals from Pages does NOT make them private; originals remain accessible in GitHub and its history. Do not change repository visibility or rewrite history without a specific, informed confirmation.

## Latest completed UI fix

PR #12, “Fix mobile collection navigation overflow”, was merged:
- PR: https://github.com/piyushimself/files/pull/12
- Head: 8706ae97ddeef1873881c5aa63b0b5f88a39a813
- Merge commit: 347fc95e5d5610723eef7e4bc56f5f508074d74d
- Change: hide duplicate Previous/Next reader shortcuts on phone widths; collection browsing remains available through Browse collections.
- PR workflow #225 / run 44355644772 completed successfully (build/browser QA job passed); deploy was skipped as expected for a PR event.
- Main deployment workflow after merge: run 44357926956, URL https://github.com/piyushimself/files/actions/runs/44357926956. At checkpoint it was in progress. Poll it and verify deployment/live site.
- A subsequent main run 44358098251 was queued for commit ded46cb8ac707b9403252ae19504f6fdfcc80a80 (“Record post-merge mobile browser QA evidence”). Poll that too.
- Earlier main run 44356951764 for commit 3719ade5ba3dab09cc4e66d612dc0eff5d884d8e completed successfully.

## Source-document inventory and review

- 49 source artifacts: 43 PDFs, 3 DOCX, 1 TXT and 2 Pine scripts. One byte-identical PDF pair leaves 48 unique source documents.
- Exact duplicate PDF pair: All_Film_Collections_Combined_compressed.pdf and All_Film_Collections_Combined_compressed (1).pdf. The corrected 647-row audit is now tracked separately in `FILM-RATINGS-647-MANIFEST.csv` and `FILM-RATINGS-647-AUDIT.json`.
- The latest extraction workflow processed 49 source artifacts. OCR is still required for Aag_Ki_Kavitayen.pdf pages 27 and 90 and 1000_Creative_Educational_Cultural_Links.pdf page 82; verify those image pages before accepting the extracted text.
- Pattern scan found no common sensitive-data matches, but this is not proof of absence.
- All 49 source artifacts remain withheld from the Pages build; none is cleared for publication. Rights/licensing/ownership remain unproven. Never publish poems, descriptions, quotes, or other substantial third-party material without documented permission/licence.
- Current editorial review: DOCUMENT-CONTENT-REVIEW.md
  https://github.com/piyushimself/files/blob/main/DOCUMENT-CONTENT-REVIEW.md
- Latest known blob SHA before handoff commit: 6c845462fb05042faef8a28097ac28437d84acee. Fetch fresh before updating.

## High-priority source findings to fix

1. Count/scope mismatches:
   - 1000_Greatest_Fictional_Books.pdf: 36 sections vs cover 26; 857 unique titles / 143 repeats; includes non-fiction/memoir.
   - 1000_Inspirations.pdf: 1,001 numbered items and one section 201 vs 1,000 claim.
   - 1000_Writing_Prompts.docx: 835 prompts, not 1,000.
   - 2000_Inspirations (1).pdf: ten section counts total 1,462, not 2,000.
   - 200_Films_Like_Frida.pdf: 220 numbered entries, 218 unique title lines.
   - 300_Films_Filmography.pdf: 298 extracted entry lines though numbering reaches 300; repair names/diacritics.
   - Cinema 900: cover says 100 x 3 = 300 while body says 300 x 3 = 900; regional subtotals support 900. library-3 reports 835 for corresponding collection; reconcile dedupe policy.
   - complete_movie_ratings.pdf: actual section counts 98 + 33 + 87 = 218, but labels imply 100 + 50 + 100.
   - complete_movie_ratings_647.pdf: 647 ranked category rows resolve to 629 distinct films under the explicit title/director/year rule, with 18 cross-category repeat groups. The manifest/parser/audit are included in PR #19; rating-source URLs and as-of dates remain missing. Reconcile its relationship to library-3's 649 records.
   - complete_movie_encyclopedia.pdf: 647 vs library-3's 649; streaming verification statement dated 2025 is stale in 2026.
2. Factual/editorial:
   - asian_books_curriculum.pdf contains “Not Asian — replace with …” placeholder and non-Asian entries in Asian list.
   - masters_of_e_art_cinema.pdf falsely claims Jane Campion is the only woman Palme d'Or winner.
   - definitive_anime_encyclopedia.pdf and ultimate_anime_guide.pdf contain known misquoted/misattributed Miyazaki line.
   - sensitive_cinema.pdf has harmful framing implying love containing violence is still love; rewrite and add specific content warnings.
   - Three_Year_Old_Reading_Guide and World_Stories_3YearOld_Guide include unsupported neuroscience claim about daily reading creating more neural pathways; remove. Reading direction guidance must be language-aware.
   - Cybersecurity_Stories_For_Your_Teams.pdf oversimplifies GDPR/NIS2/DORA incident reporting timelines; correct against official sources already cited in DOCUMENT-CONTENT-REVIEW.md.
   - Other resource directories have unverified links, outdated availability, cultural framing and attribution issues as recorded in the review.
3. Layout/visual:
   - visually inspect ratings PDFs where extraction may scramble row/column alignment; do not assume extraction defects are source defects.
   - Personal_Reference_Film_Books_Art.pdf rating glyphs extracted as ####I; inspect actual rendered pages.
   - Global kids guides and some other table PDFs have extraction ordering issues; inspect rendered pages before edits.
   - Aag_Ki_Kavitayen.pdf must preserve Hindi poetry line/stanza structure; high rights risk.
4. Pine scripts:
   - ATH - Pine.txt: timeframe mismatch (monthly logic/weekly exit), stop/target displayed but not enforced, invalid account-level compounding/CAGR/drawdown metrics; indicator, not Strategy Tester strategy.
   - Crypto_Trend_Rider_4H.pine: signals/alerts not consistently barstate.isconfirmed, Chandelier stop may loosen, initial sizing stop not enforced, partial exits distort position-level stats, no fees/slippage/spread/funding; indicator, not Strategy Tester strategy.
   - Both were only statically reviewed; not compiled/backtested in TradingView. Never claim they were.

## Immediate next actions

1. Poll workflow run 44357926956 (main deployment after PR #12 merge) and queued run 44358098251. Verify successful Pages deployment and inspect live mobile reader at phone widths.
2. Fetch fresh repository tree and current DOCUMENT-CONTENT-REVIEW.md. Continue source-level remediation, not just report annotations.
3. Reconcile film counts with reproducible title manifests. Normalize titles carefully; document alias/duplicate rules and show exact mismatches before changing claims.
4. Obtain original PDF page renderings for table/glyph problems; correct only verified defects.
5. Correct high-confidence factual/editorial issues in source documents, preserve formatting, and update review table with evidence.
6. Fix Pine code only after establishing intended semantics; add tests where possible. Compile/backtest only if a real TradingView path is available.
7. Keep source docs withheld until rights and factual/layout requirements are resolved.
8. Keep DOCUMENT-CONTENT-REVIEW.md and this handoff current. For each finding record: source, exact issue, correction commit, validation evidence, status (fixed/verified/blocked).
9. Run site-wide regression and inspect screenshots/artifacts before declaring completion.

## Automation / notification

An hourly condition-watch automation titled “Reading Room Completion Watch” is active. It checks repo commits, PRs, workflow runs, browser QA artifacts and deployment, and should notify only when all correctable work is genuinely complete or clearly blocked and documented. The automation is a status watch; it does not itself perform the repairs.



## Latest continuation checkpoint — 18 November 2026, 23:25 IST

### Deployment and CI status

- Main run [#228](https://github.com/piyushimself/files/actions/runs/44357926956) completed successfully, including deployment of the PR #12 mobile navigation fix.
- Main run [#229](https://github.com/piyushimself/files/actions/runs/44358098251) completed successfully, including deployment of the post-merge browser evidence update.
- Main run [#231](https://github.com/piyushimself/files/actions/runs/44358176598) completed successfully, including deployment of this handoff file.
- Main run [#230](https://github.com/piyushimself/files/actions/runs/44358148370) built and passed Chromium QA but its deploy job failed only because GitHub Pages was already deploying commit 3ddb7d1d30bfc3dcc574ba798e96289934073012; later runs #229 and #231 deployed successfully. This was a deployment concurrency conflict, not a site-build/browser failure.
- Latest downloaded browser artifact from run #231 reports 34 collections, 32 apps, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 63 filter disclosures and zero automated issues. Contact sheets of all 34 collection mobile screenshots, 34 desktop screenshots, and the mobile app screenshots were reviewed. Selected individual screenshots were inspected at full size.

### Additional mobile reader finding and fix in progress

Visual inspection found that the collection reader toolbar's horizontally scrollable rail clipped the System font selector and text-size controls in the initial 390px mobile viewport. Although technically swipeable, those controls were not discoverable. PR [#13](https://github.com/piyushimself/files/pull/13) changes the phone layout to wrap controls into visible rows and extends Chromium QA to assert all required controls are visible, the toolbar has no horizontal overflow, Previous/Next remain hidden, and Browse collections exposes all 34 catalogue links.

- PR #13 head: cfc2d03d0a7fa94cb9e640de4c5552a6189a3043
- Workflow run #232: [44364534543](https://github.com/piyushimself/files/actions/runs/44364534543) — was in progress at checkpoint; poll before merge.
- Do not merge until the new assertions pass and its screenshots are visually inspected.

### Pine remediation in progress

PR [#14](https://github.com/piyushimself/files/pull/14) contains a proposed correction to Crypto_Trend_Rider_4H.pine:
- confirmed-bar gating for entries, add-ons, exits and alerts;
- ratcheted Chandelier stop and prior-bar stop evaluation;
- enforced initial/shared stop and gap-fill assumption;
- target high-touch fills with stop priority;
- partial P&L rolled into completed-leg metrics;
- configurable fee/slippage/funding estimates; and
- closed-leg drawdown labeling.

A static CI invariant check was added. It is not a Pine compiler or Strategy Tester run. TradingView compile/backtest and actual exchange-cost calibration remain external acceptance steps. PR #14 workflow is queued/running; poll the check run before deciding whether to merge.

The former ATH indicator has been replaced by `ATH_Weekly_Confirmed_Strategy.pine` in merged PR #15; `ATH - Pine.txt` is now a deprecation notice. The replacement uses weekly execution and real Strategy Tester orders, but TradingView compilation/backtesting, symbol-specific fill review and cost calibration remain external. Keep both Pine scripts and the deprecated text source withheld until validation.

## Next actions from this checkpoint

1. Poll PR #13 run #232; inspect report and mobile screenshots. If the wrap layout passes and looks correct, merge, then verify the main deployment.
2. Poll PR #14's workflow/check run. Inspect the static validator output. Review the Pine diff carefully; do not describe it as compiled or backtested. If CI passes and the code review is sound, merge the source correction while keeping it withheld; record TradingView validation as externally blocked.
3. Continue source-document corrections and count reconciliation. Rights evidence remains unproven for all source documents, so none is cleared for Pages publication.
4. Continue visual PDF page inspection for table/column extraction and rating glyph defects. Do not alter source entries based only on garbled text extraction.
5. Continue resolving the ATH Pine execution model, count discrepancies and factual/editorial issues listed above.



## Continuation checkpoint — 19 November 2026, 00:32 IST

### Current verified state
- PR #13 “Keep all reader controls visible on mobile” is merged. Its workflow #232 (run 44364534543) FAILED the new navigation test on seven mature-content pages: the age-gate modal intercepted the Browse collections click. The report was downloaded and inspected. The failures are genuine test failures; the rest of the run exercised 34 catalog items, 34 wrappers, 32 apps, 68 mobile page loads, 89 iframe loads and 204 reader controls.
- Root cause under investigation: QA's age-confirmation handling is not reliably dismissing the wrapper's modal before it clicks the navigation menu. The actual wrapper gate uses #age-gate and #age-confirm; the app iframe has a separate #rr-app-age-gate/#rr-app-age-confirm. The parent wrapper gate must be dismissed and verified before testing parent navigation.
- PR #17 “Fix mature age-gate handling in mobile browser QA” is open:
  https://github.com/piyushimself/files/pull/17
  Branch `fix-mature-gate-mobile-qa`, head `78b9977f7abbb66daae94491f79112964efcdc4e`.
  It uses the actual visible confirmation control, force-clicks only after checking visibility, and verifies the modal is hidden with display:none. Run #234 / 44376472525 was queued at checkpoint. Poll and inspect the resulting report/screenshots. Do not merge until the seven cases pass and no new issues are introduced.
- PR #14 “Correct Crypto Trend Rider risk and trade metrics” is merged. It remains an indicator simulation, not a Strategy Tester strategy. PR #16 “Model spread costs and guard partial exits” is open:
  https://github.com/piyushimself/files/pull/16
  Branch head `d17224f32f30cc57c4c238ac2a02bd51d1c147a6`.
  Adds configurable per-side spread cost and caps partial target percentage at 99%. Workflow run #233 / 44375453170 was still in progress at checkpoint. Poll; inspect full static validation and browser QA. Do not merge until all checks pass.
- PR #15 “Replace unreliable ATH indicator with weekly strategy” is merged as `dd07e4eeb75a06460136ca7aa18fd711fd370b56`; main workflow #231 / 44375319576 completed successfully including deployment. New source `ATH_Weekly_Confirmed_Strategy.pine` uses weekly chart guard, previous confirmed monthly data, confirmed weekly exit, real strategy.exit stop/limit orders and TradingView Strategy Tester metrics. `ATH - Pine.txt` is now marked deprecated and points to replacement. TradingView compilation/backtest, Bar Magnifier review and broker cost calibration remain unperformed; do not claim performance validation or live readiness.
- Latest source PDF correction runner run #235 / 44376439524 completed successfully on branch `source-pdf-corrections`, head `d282243ca22d119fc2e9ca6e6bd4ddcb42a67b8a`. Artifact `reading-room-corrected-source-pdfs` (ID 14461588246) was downloaded and inspected. It contains corrected versions of many PDFs plus `FILM-RATINGS-647-AUDIT.json` and `FILM-RATINGS-647-MANIFEST.csv`. The 647 ranked rows resolve to 629 unique films under title+director+year matching, across 18 duplicate groups. Calculated unique-film stats: IMDb mean 7.58, RT mean 88%, 26 IMDb 8.5+, 184 IMDb 8.0+, 53 films at 100% RT (55 ranked rows). The manifest is an artifact only so far, not yet committed to main. The source-correction branch was previously 20 commits ahead / 4 behind main; inspect its latest state and create a clean PR/rebase. Do not merge wholesale without inspecting every changed PDF page and the two exact duplicate PDFs.
- PR #16 and #17 are both open and mergeable at checkpoint.
- Latest Actions run list included #234 (PR17, queued), #233 (PR16, in progress), #235 (source PDF correction runner, completed success).

### Immediate next actions
1. Poll run #234 (44376472525) for PR #17. Inspect QA report; confirm mature wrapper gate dismissed before menu interaction on all seven mature collections. If test still fails, diagnose selectors/overlay precisely and correct before merge.
2. Poll run #233 (44375453170) for PR #16. Review spread/funding math, especially partial exit allocation and remaining position quantity, as well as static validator and full browser QA. Merge only if clean.
3. Create a new correction PR from the source-pdf-corrections branch after bringing it up to date with main. Include the reproducible 647-row manifest, parser/audit source, and corrected PDFs. Inspect every changed page, not only cover pages; ensure original files are preserved or replaced only where correction is justified. Do not publish any of these PDFs on Pages pending documented rights clearance.
4. Review corrected PDF pages for count/title labels and typography. Audit 647 manifest rows against source page images and rating sources/as-of date. The 647/629 counts are now supported by a row-level manifest but rating provenance still needs date/source evidence.
5. Continue fixing high-confidence factual/editorial findings (Asian book placeholders/scope, Palme d'Or claim, Miyazaki quote attribution, sensitive-cinema abuse framing, reading neuroscience claim, GDPR/NIS2/DORA reporting timelines, resource URL validation, stale streaming availability).
6. Continue checking source documents for visual table defects and Hindi poetry layout. Preserve rights-sensitive material withheld.
7. Update DOCUMENT-CONTENT-REVIEW.md with per-finding correction commits and validation evidence; update this handoff at every meaningful checkpoint.
8. Keep TradingView external validation clearly separated from repository static checks.


## Continuation checkpoint — 19 November 2026, 00:36 IST

### Source-PDF correction PR preparation
- A clean branch `source-pdf-corrections-clean` was created from current main commit `6cab6377a5e0234ff0f8a0a7a7c61994b1ad55bf` to avoid merging the stale/diverged 31-commit correction branch wholesale.
- It contains 10 corrected source PDFs, `tools/correct_source_pdfs.py`, the strict 647-row parser, CSV manifest, JSON audit and deduplication report. The temporary correction workflow is deliberately not included.
- The final correction workflow run [44377163391](https://github.com/piyushimself/files/actions/runs/44377163391) succeeded and produced artifact `reading-room-corrected-source-pdfs`. The parser verifies 647 rows, 629 unique films, 18 duplicate groups, 18 repeated category records, IMDb mean 7.58, RT mean 88%, 26 IMDb 8.5+, 184 IMDb 8.0+, and 53 unique 100% RT films (55 ranked rows).
- The parser's normalization was tightened after a failed run: it strips only known trailing year/category/director/“Laputa” labels; other parenthetical text is preserved. The final successful run validates the strict parser.
- The first toddler-guide heading pass produced replacement question marks because Helvetica did not support the em dash in that insertion. A second pass replaced those with colons; the final page 15 was visually inspected and now renders correctly.

### Open PRs and CI
- PR #16 `Model spread costs and guard partial exits` is open. It adds per-side spread cost to the fee/slippage/funding model and prevents 100% “partial” exits from leaving zero-quantity legs open. Its full browser QA was still running at checkpoint; poll before merge. The dashboard cost label should also be checked so per-side costs are not described as “per 8h”.
- PR #17 `Fix mature age-gate handling in mobile browser QA` is open. It addresses seven test failures caused by the mature wrapper modal intercepting Browse collections clicks. Its full Chromium QA was still running; inspect all seven cases and screenshots before merge.
- Main run [44375319576](https://github.com/piyushimself/files/actions/runs/44375319576) after PR #15 completed successfully including deployment.
- Main run [44376623677](https://github.com/piyushimself/files/actions/runs/44376623677) is running the updated QA and handoff commit; inspect its final report.
- The corrected PDFs are not publication-cleared. No licence or ownership evidence has been provided. Keep them withheld.

### Next actions
1. Poll PR #16 and #17 workflows; inspect browser reports/screenshots. Correct the PR #16 cost-label wording before merge if still inaccurate.
2. Open a PR from `source-pdf-corrections-clean`; confirm all 10 binary PDFs and audit files are in the diff, no temporary workflow is included, and no rights-sensitive files are added to the Pages artifact.
3. Inspect all changed PDF pages, not only the sampled pages; keep all originals withheld.
4. Continue the remaining count, cultural scope, placeholder, quote, URL, table layout, rating provenance, and rights findings.


## 19 November 2026 — source PDF correction refinement

- The 647-rating PDF page 21 heading was found to still say “All 647 Films Ranked” after the cover/footer correction. It has now been corrected to “All 647 Ranked Entries by IMDb Score”.
- The correction script was made idempotent per section after a partial-run failure exposed that a global completion check could re-edit already corrected cover/page-2/stat blocks. The latest correction run [44378251873](https://github.com/piyushimself/files/actions/runs/44378251873) passed and produced a fresh artifact. The page 21 rendering was visually inspected.
- All ranking table pages 21–35 were reviewed together in a contact sheet for consistent column geometry; pages 21, 26 and 34 received additional high-resolution review. The extraction concerns about Peter Mullan and the anime score columns were false positives in the high-resolution samples.
- The clean source-PDF PR branch has been updated to commit `70a0bdcf08378922cc9414b6981be872db57be93`; it includes the latest corrected 647 PDF, manifest, audit JSON and repeatable correction script.
- Rights/ownership evidence remains unavailable; all source PDFs remain withheld.


## Automation checkpoint — 19 November 2026, 00:56 IST

### Latest site QA and deployment
- PR [#17](https://github.com/piyushimself/files/pull/17) was squash-merged as `1903c3787156523193380affa23b13ed4c6d2e11`. It fixes the mature-wrapper age-gate handling in Chromium QA.
- PR #17 workflow [#246](https://github.com/piyushimself/files/actions/runs/44376472525) passed: 34 collections, 32 apps, 34 wrappers, 34 desktop pages, 68 mobile pages, 96 iframe loads, 204 mobile reader controls, 34 reader navigation menus, 7 direct mature-app gate tests, and zero automated issues.
- The #246 mobile contact sheet and all seven mature collection mobile screenshots were reviewed. Reader controls are visible in the initial 390px viewport. The direct age-gate screenshot clearly labels the prompt as self-declaration, not identity/age verification.
- Main run [#251](https://github.com/piyushimself/files/actions/runs/44380872713) for merge commit #17 was still running at this checkpoint. Its build/deployment result and live Pages state must be checked before marking the fix deployed.
- The latest previously completed main deployment was run [#247](https://github.com/piyushimself/files/actions/runs/44376623677) for commit `6cab6377a5e0234ff0f8a0a7a7c61994b1ad55bf`; it passed and deployed, but predates PR #17.

### Pine follow-up
- PR [#16](https://github.com/piyushimself/files/pull/16) remains open. Workflow [#245](https://github.com/piyushimself/files/actions/runs/44375453170) passed the Chromium suite with zero issues (same 34/32/96/204 coverage) and the static Pine invariant checks passed in the build.
- The diff adds per-side spread assumptions to entry, partial-exit and final-exit costs, caps partial target allocation at 99%, and fixes the dashboard label so spread/fee/slippage are per-side while funding is per 8-hour interval.
- Pine cost inputs remain user-calibrated assumptions, not historical exchange data. TradingView compilation/backtesting remains an external dependency. PR #16's branch is two commits behind current main and GitHub reports mergeability as unknown; refresh/recheck before merge.

### Source-PDF follow-up
- PR [#18](https://github.com/piyushimself/files/pull/18) remains open. Its latest PR workflow [#250](https://github.com/piyushimself/files/actions/runs/44378477884) passed the full Chromium suite with zero issues; its source-PDF visual-review artifact was downloaded and 19 modified pages were rendered for inspection.
- The corrections are high-confidence but do not constitute full-page editorial or rights clearance. The PDF artifact inspection found additional layout defects not yet recorded by the previous sampled review:
  1. On page 15 of `Three_Year_Old_Reading_Guide (1).pdf`, the “10” badge is rendered as vertically separated “1” and “0”; the closing teal panel also shows two missing-glyph squares after “Happy reading.”
  2. On page 15 of `World_Stories_3YearOld_Guide.pdf`, the “10” badge likewise wraps into two lines.
- These visual defects must be corrected and re-rendered before accepting the source-PDF PR. The correction script also contains two whitespace-normalization expressions written as `r'\\s+'` instead of `r'\s+'`; review/fix this idempotence-check defect before relying on repeat runs.
- All source PDFs remain withheld from GitHub Pages and no ownership/licence/permission evidence has been established. The public repository remains public; Pages withholding does not make root-level source files private.
- The source-document inventory still contains unresolved count/scope, factual, attribution, URL, table-layout, rating-provenance and rights findings. The 647-row/629-distinct-film audit is a documented rule-based result, not a global film-identity resolver.

### Completion state
Not complete. PR #17's QA is green but post-merge deployment still needs verification; PR #16 is pending branch refresh and merge; PR #18 has visual follow-up defects; multiple source-document findings and external TradingView validation remain outstanding. Do not notify completion from a passing build or merged PR alone.


## Continuation checkpoint — 19 November 2026, 01:03 IST

### Post-merge site verification
- Main run [#251](https://github.com/piyushimself/files/actions/runs/44380872713) for PR #17 merge commit `1903c3787156523193380affa23b13ed4c6d2e11` completed successfully, with both build and Pages deploy jobs green.
- Its browser artifact `reading-room-browser-qa` (ID `14463562848`) was downloaded and inspected. It reports 34 collections, 32 apps, 34 wrappers, 34 desktop pages, 68 mobile pages, 96 iframe loads, 204 mobile reader controls, 34 reader navigation menus, 7 direct mature-app gate tests and zero issues.
- GitHub Pages deployment job success is confirmed. An independent live HTTP fetch could not be completed from this environment because the site was inaccessible to the browser fetcher and outbound DNS/network resolution was unavailable; do not claim a separate live-browser verification beyond the GitHub deployment result.

### Toddler-guide PDF layout corrections
- The initial corrected-PDF review identified a two-line “10” badge in each toddler guide and two missing-glyph squares after “Happy reading.” in `Three_Year_Old_Reading_Guide (1).pdf`.
- The correction script now centers “10” on one line in both badges, removes the unsupported footer glyphs cleanly, and fixes the two whitespace-normalization expressions in its 647-PDF idempotence checks.
- Workflow [44381955172](https://github.com/piyushimself/files/actions/runs/44381955172) completed successfully, committed only the two reviewed PDF corrections to the PR branch, and uploaded artifact `toddler-guide-pdf-layout-fixes` (ID 14464436487). Both fresh page-15 renders were inspected at full size and pass the visual checks.
- PR [#18](https://github.com/piyushimself/files/pull/18) remains open pending removal of the temporary one-off workflow, a fresh PR regression run, and merge/deployment verification.

### Remaining work
- PR #16 still needs branch refresh against current main, mergeability/check revalidation and merge if clean. Its run #245 passed the full Chromium suite with zero issues and the static Pine invariants passed; TradingView compilation/backtesting and exchange-specific cost calibration remain external.
- PR #18 still contains only a high-confidence correction pass for ten PDFs; full-page editorial/factual review, remaining count/scope issues, cultural classification, URL verification, table/layout review and rating provenance remain incomplete.
- Rights/ownership evidence is still absent for the source files. Keep them withheld from Pages. The GitHub repository is public, so the root-level source files remain accessible there; changing visibility or rewriting history requires explicit informed authorization.
- The final completion report is not ready. Do not notify completion.


## Branch refresh and PDF validation checkpoint — 19 November 2026, 01:08 IST

- The source-correction branch was merged forward with current main commit `1903c3787156523193380affa23b13ed4c6d2e11` using a two-parent merge commit `f1c30eed140c053f7042d45218d715cfaf90536d`. It is now 18 commits ahead and zero behind main; the PR branch includes the mature-gate QA fix.
- The temporary one-off PDF correction workflow has been removed from the PR branch. The reproducible correction script remains.
- The latest corrected toddler-guide PDF screenshots from workflow run [44381955172](https://github.com/piyushimself/files/actions/runs/44381955172) were inspected at full size. Both page-15 “10” badges now display on one line; the Three-Year-Old guide's footer has no unsupported glyphs or visible cover-up patch.
- Main deployment after PR #17 is confirmed by run [44380872713](https://github.com/piyushimself/files/actions/runs/44380872713): build and deploy succeeded. The post-merge browser artifact (ID 14463562848) reports zero issues across 34 desktop pages, 68 mobile pages, 96 iframe loads, 204 reader controls and 34 reader navigation menus. Independent live HTTP verification remains unavailable in this environment due outbound DNS/network restrictions.
- PR [#18](https://github.com/piyushimself/files/pull/18) still needs a fresh full PR workflow after the branch refresh and final report updates, then merge and post-merge deployment verification.
- The repository remains far from full remediation: the source-document review still lists unresolved count/scope and metadata issues, unverified resource links, remaining layout/editorial checks, missing rating provenance, and absent rights evidence. Pine TradingView validation remains external. Do not notify completion.


## PR consolidation — 19 November 2026, 01:10 IST

- PR #18 was closed as superseded after its source-correction branch was refreshed and the final PDF visual defects were fixed.
- The same reviewed tree is now submitted as PR [#19](https://github.com/piyushimself/files/pull/19) from `source-pdf-corrections-final`, based on main commit `1903c3787156523193380affa23b13ed4c6d2e11`.
- PR #19 must complete a fresh full Chromium/build run on its exact head before merge. The prior PR #18 run #252 predates the final toddler-guide PDF commits and cannot substitute for the new PR check.


## Continuation checkpoint — 19 November 2026, 05:51 IST

### Live repository state
- `main` remains at `1903c3787156523193380affa23b13ed4c6d2e11`. Main workflow [#251](https://github.com/piyushimself/files/actions/runs/44380872713) passed build, Chromium QA and Pages deployment.
- PR [#19](https://github.com/piyushimself/files/pull/19) head `6a69e153b952d69944441c1641906197d362dfe9` is open, clean and mergeable. Exact-head workflow [#256](https://github.com/piyushimself/files/actions/runs/44383657448) passed build, generated-app validation, Pine static invariants, corrected-PDF validation and Chromium QA. Browser artifact ID `14465365791`; source-PDF visual-review artifact ID `14463084897`; redacted document review artifact ID `14463584936`; Pages artifact ID `14465355787`. PR deploy job was skipped as expected.
- The #256 Chromium report records 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, 34 reader menus, 7 direct mature-app gate checks, 21 mature iframe sync checks and zero automated issues. Wrapper screenshots for all 34 pages at desktop/tablet/mobile were reviewed as contact sheets; individual app screenshots and every control have not all received manual visual review.
- The corrected source-PDF artifact was inspected as a contact sheet of the documented modified pages. The ten high-confidence corrections are visually plausible/readable; this does not constitute a complete page-by-page review of every source PDF or rights clearance.
- PR [#16](https://github.com/piyushimself/files/pull/16) remains open at `bc42f2cfa4a3eb82c371a1e5678235771b4fe6f1`, seven commits ahead/two behind current main and reported dirty/not mergeable. Its passing workflow #245 tested older SHA `d17224f32f30cc57c4c238ac2a02bd51d1c147a6`, not the current head. Refresh/rebuild the change on current main and run a new workflow before accepting it.
- The root inventory is 49 source artifacts: 43 PDFs, 3 DOCX, 1 TXT and 2 Pine scripts. One exact duplicate PDF pair leaves 48 unique source documents. The generated publishing report counts 50 withheld items because it also includes a duplicate HTML alias. The previous 48-file/one-Pine inventory statement has been corrected in `DOCUMENT-CONTENT-REVIEW.md` on this branch.

### Current remaining work
1. The source inventory, ATH replacement review and latest regression snapshot have been updated in this PR branch. These documentation changes trigger a new workflow; merge PR #19 only after the new exact-head workflow succeeds, then verify post-merge main deployment and artifacts.
2. Rebuild PR #16's spread-cost and partial-target hardening on a clean branch from updated main, update its documentation, run fresh CI, then merge only if clean.
3. Continue unresolved source-document work in `DOCUMENT-CONTENT-REVIEW.md`: Asian-books placeholders/classification; count reconciliation for fictional books, inspirations, writing prompts, filmography and Cinema 900; verify resource URLs/licence claims; inspect remaining PDF tables, bibliography and rating glyphs; establish rating-source URLs/as-of dates.
4. Keep the source-PDF inventory accurate and all originals withheld. Ownership/republication permission has not been established. The repository is public; withholding from Pages does not make root files private. Do not change repository visibility or rewrite history without informed confirmation.
5. Continue page-level editorial/visual review and keyboard, screen-reader, contrast and reduced-motion checks. Chromium automation is not exhaustive acceptance.
6. TradingView compilation, symbol-specific backtests, Bar Magnifier/order sequencing and venue-specific fee/spread/slippage/funding calibration remain external validation dependencies for both Pine scripts. No performance/live-readiness claims.
7. Independent live HTTP verification of `https://piyushimself.github.io/files/` has not been established in this runtime. GitHub Pages deployment job #251 succeeded; that is not a separate external reachability check.

Do not mark the remediation complete until all actionable findings are corrected and validated or individually documented as blocked with evidence, the site regression evidence is current, the remaining acceptance limitations are explicit, and the final report/handoff is synchronized.


## Continuation checkpoint — 19 November 2026, after refreshed Pine PR and inventory audit

### Latest PR and workflow state
- PR [#19](https://github.com/piyushimself/files/pull/19) is open and reported mergeable. Current head: `7242ce8c53deea353d1406aaf3f81490a0856b3a`. Exact-head workflow [#268](https://github.com/piyushimself/files/actions/runs/44429410787) is queued; push workflow #267 is also in progress. Earlier exact-head run #256 passed, but it does not validate the later documentation/workflow commits. Do not merge until #268 passes and its current browser/source artifacts are inspected.
- PR [#20](https://github.com/piyushimself/files/pull/20) is the clean refresh of the spread-cost/partial-exit hardening. Its current head is `a1f808afb06454acdcc20a3678608520e99f3f8a`; workflow [#263](https://github.com/piyushimself/files/actions/runs/44428949496) is in progress. It adds a per-side spread estimate to entry/partial/final exit costs, caps partial target at 99%, corrects the dashboard cost label and extends static assertions. TradingView compilation/backtesting remains external.
- PR #16 is now superseded by PR #20 but remains open/dirty. Close #16 only after #20's exact-head CI passes; do not merge the stale branch.
- The PR #19 branch now uses a same-ref concurrency group so later pushes supersede earlier builds. Older runs created before that change may still finish; only exact-head #268 is the merge gate.

### New document audit evidence
- The extraction manifest confirms 49 source artifacts (43 PDFs, 3 DOCX, 1 TXT, 2 Pine scripts), one exact duplicate PDF pair, and zero extraction errors. OCR pages are Aag_Ki_Kavitayen.pdf 27 and 90, and 1000_Creative_Educational_Cultural_Links.pdf 82.
- `asian_books_curriculum.pdf` contains at least 25 literal placeholder markers and 40 “Not Asian” statements. The markers are not unique invalid-title counts: some are replacement instructions, while other global works are intentionally described as irreplaceable. The document needs an explicit editorial decision between comparative Asian/world literature and strict Asian-only scope before a safe rewrite.
- `PAGE-AUDIT.md` still has 11 unchecked manual acceptance items. Automated Chromium QA has passed on the earlier #256 head, and wrapper screenshot contact sheets were swept at desktop/tablet/mobile; this is not exhaustive app/control review, keyboard-only or screen-reader certification, or a formal contrast audit.

### Acceptance status
- `main` remains `1903c3787156523193380affa23b13ed4c6d2e11`; main workflow #251 build and Pages deployment succeeded.
- Independent live HTTP verification still fails at DNS resolution in this runtime. This is an environment limitation, not proof the site is down.
- Rights/ownership/republication evidence remains absent. All source artifacts remain withheld from Pages, but the public repository exposes root-level files; do not change visibility or rewrite history without informed confirmation.
- Remaining source work includes other count/scope discrepancies, link/licence verification, bibliography and attribution review, remaining PDF table/layout checks, rating provenance/as-of dates and complete editorial review. Pine validation on intended symbols/venues remains external.

Do not mark complete until PR #19 and #20 are validated/merged with post-merge deployment evidence, all actionable content and page findings are corrected or individually evidence-blocked, the 11 manual acceptance items are resolved or explicitly documented as blocked, and the final report is synchronized.


## Continuation checkpoint — 19 November 2026, 06:35 IST

### Verified repository state
- `main` advanced to `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0` when PR #20 merged. Its main-branch build/deployment workflow [#283](https://github.com/piyushimself/files/actions/runs/44435251703) was still running at this checkpoint; verify its final build, Chromium QA and Pages deployment before treating this commit as deployed.
- PR [#20](https://github.com/piyushimself/files/pull/20) merged successfully as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`. Exact-head workflow [#272](https://github.com/piyushimself/files/actions/runs/44434546875) passed static Pine checks and Chromium QA. The final code includes estimated spread cost on entry, partial exits and final exits; the static validator now asserts all three paths. The report recorded 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls and zero automated issues. The change remains an indicator simulation, not a Strategy Tester strategy; TradingView compile/backtest and venue-specific calibration are external.
- PR [#16](https://github.com/piyushimself/files/pull/16) is closed as superseded by PR #20. Its stale/diverged branch must not be merged.
- PR [#19](https://github.com/piyushimself/files/pull/19) is still open on `source-pdf-corrections-final`. Its head at this checkpoint is `855ae60bb65b249489468ff55e1f178d49857c12`. Workflow [#282](https://github.com/piyushimself/files/actions/runs/44434859798) was still in progress after build, generated-app, Pine static and source-PDF validators passed; Chromium QA was starting. This checkpoint update itself will trigger a newer exact-head run, so only the newest PR event run for the final branch SHA is a merge gate.
- The previous exact-head PR workflow [#271](https://github.com/piyushimself/files/actions/runs/44429510208) passed. Its report recorded 34 desktop collection pages, 68 mobile page loads, 96 iframe loads, 204 mobile reader controls, 34 reader menus, 7 direct mature-app gate tests and zero issues. The report, Pages artifact and source-PDF review artifact were downloaded and inspected.
- Visual review included contact sheets for all 34 wrapper screenshots at desktop, tablet and mobile sizes, plus app screenshot contact sheets. Individual screenshots were inspected for the homepage, Big Library, Asian Cinema, Complete Film Collection and several mature apps. This does not equal pixel-by-pixel inspection of every control or a formal accessibility audit.
- The 19 documented corrected PDF pages were rendered into a contact sheet and inspected; representative full-size pages included the sensitive-cinema correction and the 647-ratings statistics page. This is not a page-by-page review of all 43 PDFs.

### New catalogue metadata defects found and corrected in PR #19
- The rendered Complete Film Collection app showed 1,629 records, but the homepage catalogue card/search metadata still said 1,619.
- The 296 animated-film correction was present in the app title, but catalogue search metadata still included 300.
- Big Library rendered 98 of 4,942 in its default section, while catalogue search text retained the source placeholder “Showing 0 of 0”.
- The generated build and `tools/validate_site.py` now correct/assert these three metadata cases. The root-level source HTML files remain unchanged. The final exact-head workflow must pass before merging these corrections.

### Remaining findings and blockers
1. The source inventory is 49 artifacts (43 PDFs, 3 DOCX, 1 TXT, 2 Pine scripts); one byte-identical PDF pair leaves 48 unique source documents. The publishing review counts 50 withheld items because it also includes the duplicate HTML alias. No source document is rights-cleared.
2. The Asian-books curriculum has at least 25 literal placeholder markers and 40 “Not Asian” statements. These are not unique invalid-title counts. The safe correction depends on the content owner's decision whether the intended scope is comparative Asian/world literature or strict Asian literature.
3. Other unresolved content findings include fictional-books section/unique-title counts and mixed non-fiction; inspiration and writing-prompt totals; filmography entry/numbering discrepancies; the Cinema 900 cover/section count and 835-versus-900 relationship; remaining catalogue count reconciliation; resource URL/licence verification; bibliography/attribution; rating-source URLs/as-of dates; and remaining PDF table/layout/OCR review.
4. The corrected PDF pages are not publication-cleared. Ownership and republication permission have not been established. Source PDFs remain excluded from Pages, but root-level files are still accessible in this public repository. Do not change visibility or rewrite history without informed confirmation.
5. `PAGE-AUDIT.md` still has 11 unchecked manual acceptance items. Chromium automation does not establish exhaustive per-control review, formal contrast/WCAG conformance, keyboard-only completeness, screen-reader behavior or reduced-motion behavior.
6. TradingView compilation, Strategy Tester/backtest, Bar Magnifier/order sequencing, symbol-specific data and exchange/broker fee, spread, slippage and funding calibration remain external dependencies. Do not claim validated performance or live readiness.
7. Independent live HTTP verification of `https://piyushimself.github.io/files/` failed with a DNS resolution error in this runtime. This does not prove the site is down; verify from an independent network. GitHub Pages deployment job evidence remains separate.

Do not mark the remediation complete until every remaining finding is corrected or individually evidence-blocked, the newest exact-head and post-merge main regression/deployment checks pass, the manual page/accessibility acceptance items are resolved or explicitly dispositioned, and the final status report is synchronized.


## Final checkpoint for this continuation — 19 November 2026, 06:38 IST

- The latest PR #19 branch head before this handoff commit is `65944ce3b4288b8c0540c5408b9645b2f6459dc5`. Exact-head PR workflow [#289](https://github.com/piyushimself/files/actions/runs/44435563042) is pending; push workflow #290 is queued. This handoff update will create one final branch head and supersede those runs. Use the newest PR event workflow for the resulting live PR head as the merge gate.
- PR #19 includes the ten high-confidence corrected PDFs, 647-row manifest/parser/audit, source-PDF correction validator, source inventory correction, latest QA/handoff updates, and generated catalogue metadata fixes for 296 animated films, 1,629 Complete Film Collection records and Big Library's 98-of-4,942 default state.
- PR #19 is reported mergeable/clean. Do not merge until the newest exact-head PR workflow passes and its browser/source/Pages artifacts are inspected. After merge, verify a fresh main workflow and deployment.
- PR #20 is merged as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`; PR #16 is closed as superseded. Main workflow #283 has passed build, generated-script validation and Pine static validation and is running Chromium QA; confirm its final QA and deploy result.
- The corrected PDFs and audit are not publication-cleared. All source documents remain withheld. The repository remains public; root-level source files are still accessible.
- The PAGE-AUDIT inventory now states 49 source artifacts (43 PDFs, 3 DOCX, 1 TXT, 2 Pine scripts), 48 unique source documents after the duplicate PDF pair. Eleven manual acceptance items remain unchecked.
- The Asian-books curriculum scope decision, Cinema 900 cover/count and 835-vs-900 reconciliation, other collection count discrepancies, unverified links/licences, bibliography/attribution, rating provenance/as-of dates, remaining PDF layout/OCR review and broad editorial review remain open. Rights evidence and TradingView/venue validation remain blockers as documented.
- A direct live-site request from this runtime failed due DNS resolution. That is not evidence of an outage; independent network verification is still required.

**Status: IN PROGRESS.** This handoff is the current continuation record, not a completion certificate. Do not notify the user of completion until every remaining finding is corrected or individually evidence-blocked, all final main-branch regression/deployment checks pass, the page/accessibility acceptance items are dispositioned, and the status report is synchronized.


## Follow-up documentation checkpoint — 19 November 2026, 06:40 IST

The per-file review table has now been reconciled with the corrections already present in PR #19 and the merged PR #20. It distinguishes corrected findings from remaining restrictions for the Campion claim, Sensitive Cinema framing, Miyazaki attribution, both ratings PDFs, the stale streaming disclaimer, cybersecurity timelines, toddler-guide science/layout, and Crypto Trend Rider spread accounting. Remaining rights, rating provenance, cultural scope and broader content/layout reviews are still open.

The latest PR #19 head before this final handoff update is `766bd1f9cd0983bf4cff96d7561e8c006fc5af53`; exact-head PR workflow [#294](https://github.com/piyushimself/files/actions/runs/44435801050) is pending. This handoff update will produce the next branch head; use the newest PR event workflow for the live head, not #294, as the final merge gate. The PR is reported mergeable and clean.

Main workflow [#283](https://github.com/piyushimself/files/actions/runs/44435251703) for PR #20's merge commit `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0` has passed build, generated-script and Pine static checks; it is still running Chromium setup/QA and has not yet established post-merge deployment success.

No other source-document findings have been closed by this documentation update. The Cinema 900 cover/count issue, Asian-books editorial decision, remaining count reconciliations, link/licence verification, attribution/bibliography, rating provenance, unreviewed PDF pages and manual accessibility checks remain outstanding.


## Latest automation checkpoint — 19 November 2026, 07:38 IST

- PR #19 was merged after exact-head workflow [#299](https://github.com/piyushimself/files/actions/runs/44436114541) passed on head `0f3bc8f57e0a0381397a5b8ce6f1d477e2102e0e`. Merge commit: `0699b3a10090ddb9c018ba37116078597d8b0ccd`.
- PR #19's workflow #299 passed build, generated-app validation, Pine static checks, corrected-source-PDF validation, Chromium desktop/mobile QA and artifact upload. Its deploy job was skipped as expected for a pull request.
- The #299 browser report: 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, 34 reader menus, 7 direct mature-app gate checks, 63 filter disclosures and zero automated issues. Contact sheets for all 34 wrapper pages at desktop/tablet/mobile and the 33 app-mobile captures were visually swept. This is not a per-control, keyboard-only, screen-reader or formal WCAG sign-off.
- The #299 Pages artifact was inspected: 34 published HTML collections, 123 entries, no PDF/DOCX/Pine/source-document files; `robots.txt` was the only .txt match. The publishing review lists 50 withheld items (49 source artifacts plus one duplicate HTML alias).
- Main workflow [#283](https://github.com/piyushimself/files/actions/runs/44435251703) for PR #20 commit `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0` completed successfully, including Chromium QA and Pages deployment. Its browser report has the same 34 desktop / 68 mobile / 96 iframe coverage and zero automated issues.
- **The merge commit `0699b3a10090ddb9c018ba37116078597d8b0ccd` still needs its own fresh main workflow, regression artifact inspection and Pages deployment confirmation.** Do not treat #283 as deployment evidence for the later PR #19 merge.
- PR #20 is merged as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`; PR #16 is closed as superseded. No open PRs were present after PR #19 merged.
- The corrected-PDF artifact was inspected. Selected changed pages across the ten corrected PDFs were rendered and visually checked; this is not a full page-by-page review of every source document.
- The source inventory is 49 artifacts (43 PDFs, 3 DOCX, 1 TXT, 2 Pine) and 48 unique documents after one exact duplicate PDF pair. All source files remain withheld from Pages, but the repository is public and root-level originals/history remain accessible.
- Outstanding findings remain: Asian-books scope decision; Cinema 900 cover/count and 835-vs-900 reconciliation; fictional-books, inspiration, writing-prompt and filmography count discrepancies; 647/649 encyclopedia reconciliation; resource links/licences, bibliography/attribution, rating source URLs/as-of dates; remaining PDF/OCR/layout and factual review; 11 manual page/accessibility acceptance items; rights/ownership; and TradingView/venue-specific validation.
- A direct live-site request from this runtime failed DNS resolution. This is not evidence of an outage; independently verify after the new main deployment.

**Status: IN PROGRESS.** See [REMEDIATION-STATUS.md](REMEDIATION-STATUS.md) for the current acceptance ledger. Do not send a completion notification until all remaining findings are corrected or individually evidence-blocked, and the post-merge deployment and all required acceptance checks are complete.


## Latest main deployment and regression checkpoint — 19 November 2026, 08:48 IST

This section supersedes older checkpoint notes that said a fresh main deployment after PR #19 was still pending.

- Current `main`: `0bbe318ae4341aa16393ff95d9dd24452bed46d7` — “Expand Reading Room status with remaining per-file findings”.
- There are no open pull requests in the current GitHub open-PR listing. PR #19 and PR #20 are merged; PR #16 is closed as superseded.
- Main workflow [#305](https://github.com/piyushimself/files/actions/runs/44442583472) completed successfully for the exact current main SHA. Build and deploy jobs both succeeded. The build passed generated-app validation, Pine static invariants, corrected-PDF validation, redacted document extraction and Chromium QA.
- Browser artifact ID `14492822395`: 34 desktop wrappers, 68 mobile page checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync checks, 34 reader menus, 204 mobile reader controls, 63 filter disclosures, 33 theme-sync, 32 font-sync, 32 text-scale checks, zero automated issues; 337 screenshots.
- The latest QA artifact was downloaded. Contact sheets were inspected for all 34 wrappers at desktop/tablet/mobile and 33 app captures at desktop/mobile. This is broad page-level visual review, not exhaustive pixel/control-state or accessibility certification.
- Pages artifact ID `14492268281` was downloaded and its tar contents inspected. No PDF, DOCX or Pine source files are included; `robots.txt` is the only `.txt` file. The 50 withheld items remain withheld.
- A separate live-site fetch remains unavailable from this runtime: the web fetcher cannot access `https://piyushimself.github.io/files/`. GitHub Actions deployment success is confirmed, but independent live HTTP reachability is not.
- The project remains **IN PROGRESS**. The detailed remaining findings in `REMEDIATION-STATUS.md` and `DOCUMENT-CONTENT-REVIEW.md` are still actionable: count/scope discrepancies, Asian-books editorial scope, Cinema 900 reconciliation, resource/licence/attribution checks, ratings provenance, remaining source-page and factual review, 11 manual page/accessibility acceptance items, rights/ownership evidence and TradingView/venue validation.
- Do not claim completion from workflow #305. It closes the post-PR #19 main deployment gate only.

Next: continue the objective source corrections and evidence gathering, update the manual acceptance matrix with per-item outcomes, keep source files withheld until rights are established, and preserve exact external TradingView/venue limitations.

## Continuation checkpoint — 19 November 2026, 09:40 IST

- Current main SHA: `53d14aee33383421e640af3b59126ca6a2f47edb`.
- Main workflow [#309](https://github.com/piyushimself/files/actions/runs/44450778850) passed build, generated-app validation, Pine static invariants, corrected-source-PDF validation, redacted extraction, Chromium browser QA, and Pages deployment.
- Browser QA artifact [14494544620] was downloaded and report inspected: 34 catalogue items, 32 apps, 34 desktop pages, 68 mobile checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync, 33 theme-sync, 32 font-sync, 32 scale-sync, 63 filter disclosures, 204 mobile reader controls, 34 reader menus, zero automated issues. Screenshots include desktop/tablet/mobile and app states. This is not formal WCAG, screen-reader or keyboard-only sign-off.
- GitHub Pages deployment job succeeded for this exact main SHA. The Pages artifact for #309 is available (ID 14494998543) but has not yet been downloaded and inspected. Prior Pages artifact #305 was inspected and contained no source PDF/DOCX/Pine files.
- Run #300 was cancelled during OCR setup before build/QA; newer run #309 passed and supersedes it.
- No open PRs were reported at this check.
- Independent live-site HTTP reachability is still not verified from this runtime. Deployment success is not the same as an independent browser/network check.
- All previously listed open content, source-document, rights, page/accessibility, and TradingView/venue-validation items remain open. Status: **IN PROGRESS**.


## Follow-up main verification — 19 November 2026, 10:00 IST

- Current main: `8c279d771b1b4a59ca81a10f5a8c0aa9d3c7f40c`.
- Main workflow [#312](https://github.com/piyushimself/files/actions/runs/44456566278) completed successfully for this exact SHA. Build and Pages deploy both succeeded; generated-app checks, Pine static invariants, corrected-source-PDF validator, redacted extraction and Chromium desktop/mobile QA passed.
- Browser artifact [14498832464](https://github.com/piyushimself/files/actions/runs/44456566278) was downloaded and inspected. It reports 34 catalogue items, 32 apps, 34 desktop wrappers, 68 mobile checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls, 34 reader menus and zero automated issues.
- Pages artifact [14498473147](https://github.com/piyushimself/files/actions/runs/44456566278) was downloaded and inspected: 123 tar entries, 69 HTML files; no PDF, DOCX or Pine source files. Only one .txt file is present (robots.txt).
- Redacted extraction artifact [14498725745](https://github.com/piyushimself/files/actions/runs/44456566278) was inspected: 49 source artifacts processed, one exact duplicate group, zero extraction errors. This confirms extraction only; it does not establish content correctness, visual completeness or publication rights.
- No open PRs are currently reported. No additional source-document finding has been closed by this run. Independent live HTTP reachability remains unverified from this runtime.

**Status remains IN PROGRESS.** All outstanding content/count, rights, accessibility/manual acceptance and TradingView/venue validation items remain as previously listed.

## Latest main verification — 19 November 2026, 12:48 IST

- Current main: `b6d68eff58469c7adda14cc9edee3ed04ef01101`. The three commits after the #312 checkpoint are documentation-only changes to the status report, page audit and this handoff; no app/source code changed after #312.
- Main workflow [#315](https://github.com/piyushimself/files/actions/runs/44458475169) passed build and Pages deployment for this exact SHA. The build log checked out `b6d68eff58469c7adda14cc9edee3ed04ef01101`; the deploy log created and reported success for the Pages deployment of the same SHA.
- Browser artifact [14497854888](https://github.com/piyushimself/files/actions/runs/44458475169) was downloaded and inspected: 34 desktop pages, 68 mobile checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls, 34 reader menus, zero automated issues and 337 screenshots. Contact sheets were swept for 34 wrapper desktop/mobile captures, 33 app-mobile captures and 32 app-initial-mobile captures; representative full-size mobile screenshots were inspected.
- Pages artifact [14498089145](https://github.com/piyushimself/files/actions/runs/44458475169) was inspected: 123 tar entries, 69 HTML files, no PDF/DOCX/Pine source files; `robots.txt` is the only text file.
- Redacted extraction artifact [14498613806](https://github.com/piyushimself/files/actions/runs/44458475169) reports 49 source artifacts, one exact duplicate group, zero extraction errors and OCR on 1000 Creative Links p.82 and Aag Ki Kavitayen pp.27/90, with no OCR errors. Extraction is not editorial or rights clearance.
- The #315 step that uploads temporary source PDFs for visual review was skipped; no new source-PDF visual review is claimed.
- No open PRs are reported. PR #19 and #20 are merged; PR #16 is closed as superseded. The independent live-site HTTP check remains unavailable from this runtime; Pages deployment is confirmed by GitHub Actions.
- Status remains **IN PROGRESS**. The source-content/count and editorial findings, unverified links/licences/attribution/ratings provenance, remaining document-page review, 11 manual page/accessibility acceptance items, rights/ownership and external TradingView/venue validation remain unresolved or dependent on owner evidence/decisions/external validation. Do not mark complete from #315.



## Continuation checkpoint — 19 November 2026, 14:15 IST

### Merged work and deployment
- PR #21 (preliminary accessibility QA and The Loom date-picker accessible name) is merged as `52fcc6033f31b562bd87d851c832f779a9e4c52c`. Exact-head PR workflow #322 passed with 34 collection pages, 32 apps, 96 iframe loads, 0 functional issues and 0 preliminary accessibility findings. This is not a formal WCAG audit.
- The first post-PR #21 main run #323 was cancelled when a newer main commit arrived. Do not treat cancellation as a deployment failure or success; the newer main run is the active gate.
- PR #22 (documentation of verified source-PDF visual/count findings) passed exact-head workflow #324 and was squash-merged as `e0c00b55504efecfa5d91e1c8486f03ef7a90b03`.
- Main run #325, [44540106449](https://github.com/piyushimself/files/actions/runs/44540106449), is the current build/QA/deployment gate for that commit. At checkpoint it is running real-browser QA; deploy has not yet been confirmed.

### Global Kids Books PDF layout — final generated correction in PR review (22 November 2026)
- The source PDF has 30 pages. A full drawing-bounds audit found horizontal overflow on pages 4–12 and 14–28: x=-73.46 to x=668.74 points on A4 pages only 595.28 points wide.
- The source also contains a genuinely blank page 13 (no text, vector drawings, images, annotations or page content). The generated output removes this empty page; it does not remove any content-bearing page.
- The generator expands all pages to a consistent 743.2 pt canvas without scaling or rasterizing vector/text content. It repairs 11 two-digit row numbers that previously wrapped vertically in the narrow first column, removing the original stacked glyphs from the text layer and reinserting the numbers horizontally over the correct alternating row background.
- Local validation reports a 29-page output, zero horizontal-overflow pages, 11 repaired number cells, zero remaining stacked-number pairs, and text extraction increasing from 34,670 to 44,394 characters. The complete 29-page contact sheet and full-size renders of all six affected pages were inspected.
- Latest generator commit: `cd11cf83a4e468cb060de8e0829b80feeb19de8a`. Documentation update commit: `5cfb3c557e2d8265884fe772e5f913779628c1b5`. Exact-head workflow #344 / [45007404965](https://github.com/piyushimself/files/actions/runs/45007404965) is the latest CI gate; do not merge or replace the source PDF until it passes and the final artifacts are inspected.
- The corrected PDF remains a separate generated output; the original source file is not overwritten. All source PDFs remain withheld from GitHub Pages. This layout correction does not establish rights, resolve the 600+ inventory count, reconcile the near-duplicate FINAL guide, or source the developmental claims.

### Immediate next actions
1. Poll PR #23 exact-head workflow #344; inspect the final generator, corrected output and artifact evidence. Merge only if the latest run passes and the 29-page result is verified.
2. Verify post-merge main build and Pages deployment for PR #24 and the latest remediation-status updates; workflow #337 passed its exact PR head, but main deployment is a separate gate.
3. Continue objective source-document count, bibliography, quotation, link, licensing and content checks. Do not mark the 600+ inventory, near-duplicate guide reconciliation or rights as resolved.
4. Continue page-by-page keyboard, screen-reader, contrast and interaction acceptance; the expanded Chromium visual sweep is not exhaustive manual QA or WCAG certification.
5. Continue external TradingView and venue-specific validation; static Pine checks do not establish compilation or strategy performance.
