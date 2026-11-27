## Latest verified checkpoint — 28 November 2026, 00:13 IST (Asia/Kolkata)

- PR [#28](https://github.com/piyushimself/files/pull/28) remains open and unmerged on `remediation/stop-public-source-review-artifacts-2026-11-26`. Exact current head: [`f8df4ba2f07b8f9896856f41df8c0271371c5e20`](https://github.com/piyushimself/files/commit/f8df4ba2f07b8f9896856f41df8c0271371c5e20); compare against `main` confirms 30 commits ahead and zero behind. No submitted reviews, inline review threads or PR conversation comments exist.
- Exact-head workflow [#372 / run 46045016330](https://github.com/piyushimself/files/actions/runs/46045016330) completed successfully for `f8df4ba2f07b8f9896856f41df8c0271371c5e20`. Build, generated-app validation, Pine static checks, corrected-source-PDF validation and Chromium desktop/mobile QA passed. The deploy job was correctly skipped for a `pull_request` event.
- The #372 build log (71,945 characters) was inspected. It contains no `document_review_extract.py`, source-review artifact upload, source-PDF upload, corrected-source-PDF artifact upload or `PUBLISHING-REVIEW.md` upload.
- Browser-QA artifact [15221928089](https://github.com/piyushimself/files/actions/runs/46045016330) was downloaded and inspected: 528 files (525 screenshots plus report JSON/Markdown and catalogue JSON); 34 desktop pages, 68 mobile checks, 96 iframe loads, 20 search controls, 14 select controls, 15 filter controls, 3 tabs, 4 shell controls, 7 direct mature-app gates, 21 mature iframe-sync checks, 33 theme-sync checks, 32 font-sync checks, 32 scale-sync checks, 63 filter disclosures, 34 mobile reader-shell pages, 204 mobile reader-shell controls and 34 reader navigation menus. It reports zero automated issues and zero preliminary accessibility warnings. These are automated checks, not WCAG conformance or assistive-technology certification.
- Pages preview artifact [15221698024](https://github.com/piyushimself/files/actions/runs/46045016330) was downloaded and inspected: 122 tar entries, 83 files and 68 HTML files. It contains no PDF, DOCX, Pine source, source-review inventory or internal publishing report; `robots.txt` is the only `.txt` file.
- Visual sampling of #372 screenshots: homepage mobile is readable; 300 Animated Films mobile ranks 7–16 remain on one line; Manga & Comics Master dark-desktop content is legible, although small filter/metadata labels still need measured contrast review. No dark-mobile screenshots are present. This remains sampling, not exhaustive page-by-page manual acceptance.
- Main remains at `d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`. Main workflow [#356 / run 45794785456](https://github.com/piyushimself/files/actions/runs/45794785456) remains the latest verified production Pages deployment; its build and deploy jobs succeeded. Its build still runs source extraction and uploads corrected-source-PDF and temporary source-review material. The #356 browser-QA artifact [15105410621] still contains `PUBLISHING-REVIEW.md`; the corrected-source-PDF artifact [15104820560] also remains downloadable.
- Historical artifacts [15105410621](https://github.com/piyushimself/files/actions/runs/45794785456) and [15104820560](https://github.com/piyushimself/files/actions/runs/45794785456) are still marked unexpired. Scheduled expiry is 10 December 2026 at 15:26:13 IST and 15:16:04 IST respectively. The connected GitHub integration exposes no artifact-deletion action; owner deletion or verified expiry remains required. Earlier artifacts 15103848500 and 15104822142 return 404.
- All 11 manual acceptance checkboxes in `PAGE-AUDIT.md` remain unchecked. They cover exhaustive desktop/mobile page review, interaction states, themes/fonts/scaling, sticky controls, measured contrast, keyboard/screen-reader/reduced-motion behavior, full PDF/DOCX/OCR inspection, source-to-output completeness, links/images/console/sitemap, catalogue reconciliation and missing-title/H1 fallback.
- Editorial findings remain open: Asian Books scope/placeholders (25 placeholder markers and 40 “Not Asian” statements); Cinema 900's 300/900/835 count discrepancy; Global Kids Books' 317-versus-600+ count, roughly 55% overlap and uncited developmental claims; plus other catalogue counts, URLs, bibliographies, quotations, attribution, metadata, age suitability and rating provenance.
- The 49 original source artifacts remain excluded from Pages because publication-permission evidence is absent, but the originals remain accessible in this public repository. This is a documented permission limitation, not private storage. Preserve originals and do not change repository visibility or rewrite history without an informed owner decision.
- Pine static validation passes. TradingView compilation/backtesting and venue-specific calibration remain external dependencies and are not Reading Room website deployment gates.

**Status: IN PROGRESS — not a completion certificate.** Exact-head PR automation and its artifacts are validated, but historical artifact exposure, all 11 manual acceptance items, editorial findings, independent PR review and production deployment verification remain open.

### Current completion gates

1. Obtain owner deletion of artifacts 15105410621 and 15104820560, or verify direct download failure after their 10 December expiries.
2. Complete or individually evidence-disposition all 11 manual acceptance items, including measured contrast, dark-mobile evidence, keyboard/screen-reader/reduced-motion checks and exhaustive page review.
3. Correct or individually document evidence/permission blocks for every remaining editorial finding.
4. Resolve the publication-permission decision for the 49 original source artifacts without implying that public repository copies are private.
5. Obtain independent PR review; keep PR #28 open until acceptance is complete.
6. After acceptance and merge, run a fresh main workflow; inspect complete logs and artifacts; verify production desktop/mobile behavior and confirm the deployed SHA.
7. Update the final status report on main against the actual production deployment.
---

## Latest verified checkpoint — 27 November 2026, 16:00 IST (Asia/Kolkata)

- Default branch `main` remains at [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e). Main workflow [#356](https://github.com/piyushimself/files/actions/runs/45794785456) is still the latest successful production Pages deployment for that exact SHA. PR #28 has not been merged and no post-merge production deployment exists.
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open on `remediation/stop-public-source-review-artifacts-2026-11-26`, based on main. At the start of this checkpoint its head was [`ec8734401b39a10d6329a8b23dd30d6904d5fa56`](https://github.com/piyushimself/files/commit/ec8734401b39a10d6329a8b23dd30d6904d5fa56), 28 commits ahead and zero behind. It has no submitted reviews, inline review threads or conversation comments.
- Exact-head PR workflow [#370 / run 45970222950](https://github.com/piyushimself/files/actions/runs/45970222950) completed successfully for `ec8734401b39a10d6329a8b23dd30d6904d5fa56`. The build, generated-app validation, Pine static checks, corrected-source-PDF validation and Chromium desktop/mobile QA all passed. The deploy job was correctly skipped for a `pull_request` event.
- The complete #370 build-job log was inspected. It contains no `tools/document_review_extract.py` step, no source-review inventory/redaction/OCR output and no `PUBLISHING-REVIEW.md` upload. Tesseract/OCR-engine installation remains a build dependency but did not execute the removed extraction step.
- Browser-QA artifact [15184827869](https://github.com/piyushimself/files/actions/runs/45970222950) was downloaded and inspected: 528 files; 34 desktop pages; 68 mobile checks; 96 iframe loads; 20 search, 14 select and 15 filter controls; 3 tabs; 4 shell controls; 7 direct mature-app gates; 21 mature iframe-sync checks; 33 theme-sync; 32 font-sync; 32 scale-sync; 63 filter disclosures; 34 reader menus; and 204 mobile reader-shell controls. The report contains 525 screenshot entries, zero automated issues and zero preliminary accessibility findings. These automated results are not WCAG conformance or assistive-technology certification.
- Pages preview artifact [15185866420](https://github.com/piyushimself/files/actions/runs/45970222950) was downloaded and inspected: 122 tar entries, 68 HTML files, no PDF/DOCX/Pine files and only `robots.txt` as a text file. No source-review inventory or internal publishing report was present.
- Visual sampling of #370 screenshots confirmed a readable homepage mobile layout and 300 Animated Films mobile ranks 7–16 on one line. The Manga & Comics Archive dark-desktop screenshot still shows subdued sidebar/filter labels. The report contains 32 dark-desktop captures but no dark-mobile screenshots. This is a sample, not a full page-by-page manual acceptance pass; measured contrast remains open.
- Historical artifacts [15103848500] (source-review extraction) and [15104822142] (older Pages preview) now return GitHub API 404 on direct download attempts after their scheduled expiries. Treat them as no longer downloadable through GitHub Actions; the earlier 49-file source-review ZIP is no longer available through this integration.
- Two older artifacts remain publicly downloadable: browser-QA artifact [15105410621] still contains `PUBLISHING-REVIEW.md` listing 50 withheld filenames/reasons and expires 10 December 2026 at 15:26:13 IST; corrected source-derived PDF preview [15104820560] remains downloadable and expires 10 December 2026 at 15:16:04 IST. The connected GitHub integration has no artifact-deletion action. Owner deletion or verified automatic expiry is still required.
- All 11 manual acceptance items in `PAGE-AUDIT.md` remain unchecked. They cover complete desktop/mobile page review; interaction states; light/dark themes, fonts and scaling; sticky controls; measured contrast; keyboard, screen-reader and reduced-motion behavior; complete PDF/DOCX/OCR review; source-to-output completeness; links/images/console/sitemap; catalogue reconciliation; and missing-title/H1 fallback.
- Editorial findings remain open: Asian Books scope/placeholders (25 placeholder markers and 40 “Not Asian” statements); Cinema 900 cover/body 300-versus-900 and 835-item comparison; Global Kids Books 317-versus-600+, roughly 55% overlap and uncited developmental claims; other catalogue-count conflicts; URL validation; bibliographies, quotations, attribution, author/edition metadata, age suitability and rating provenance.
- All 49 original source artifacts remain excluded from Pages because publication-permission evidence is absent, but the public GitHub repository still exposes the originals. This is a documented rights/permission block, not evidence that the source copies are private. Preserve originals and do not change visibility or rewrite history without the owner's informed decision.
- Pine static checks pass. TradingView compilation/backtesting and venue-specific calibration remain external dependencies and are not Reading Room website deployment gates.
- **Status: IN PROGRESS — not a completion certificate.** Exact-head PR automation and new Pages/browser artifacts are validated, and two expired artifacts are no longer downloadable. The older publishing-review and corrected-PDF artifacts remain accessible; manual/editorial acceptance, PR review/merge and post-merge production verification remain outstanding.

### Current completion gates

1. Obtain owner deletion of artifacts 15105410621 and 15104820560, or re-check after their 10 December expiries and verify direct download failure.
2. Complete or individually evidence-disposition all 11 manual acceptance items. Include measured contrast, dark-mobile evidence, keyboard/screen-reader/reduced-motion checks and exhaustive page review.
3. Resolve or individually document the editorial findings and source-permission decisions.
4. Obtain independent PR review. Do not merge solely because #370 passed.
5. After review and acceptance, merge only when ready; run a fresh main workflow, inspect logs/artifacts, verify production desktop/mobile regression and confirm the Pages deployment SHA.
6. Update the final status report on main against the deployed commit. The main-branch report is still dated 23 November and is not current.

---

# Reading Room remediation — current status

## Latest verified checkpoint — 27 November 2026, 14:27 IST (Asia/Kolkata)

- Default branch `main` remains at [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e). Main workflow [#356](https://github.com/piyushimself/files/actions/runs/45794785456) remains the latest successful production build and GitHub Pages deployment for that exact SHA. No post-merge deployment of PR #28 exists.
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open on `remediation/stop-public-source-review-artifacts-2026-11-26`, based on current main. Before this checkpoint it was at [`4f849f6a589f20c46d52e9c995f3382ed9199ef8`](https://github.com/piyushimself/files/commit/4f849f6a589f20c46d52e9c995f3382ed9199ef8), 27 commits ahead and zero behind. It has no submitted reviews, review threads or conversation comments. This checkpoint is being added as a new PR-branch documentation commit; that new head requires its own exact-head workflow before it can be called validated.
- Exact-head PR workflow [#369 / run 45953382752](https://github.com/piyushimself/files/actions/runs/45953382752) completed successfully for the pre-checkpoint head `4f849f6a589f20c46d52e9c995f3382ed9199ef8`. The build and Chromium desktop/mobile QA passed; deployment was correctly skipped for a `pull_request` event. All build, generated-app, Pine static, corrected-source-PDF and browser-QA steps succeeded.
- The complete #369 build-job log was inspected. It contains no `tools/document_review_extract.py` step, no source-review inventory/redaction/OCR output and no `PUBLISHING-REVIEW.md` upload. Tesseract/OCR-engine installation still occurs as a build dependency; that installation did not run the removed document-review extraction step. The workflow uploads only the browser-QA report/screenshots and generated Pages preview.
- Browser-QA artifact [15178166776](https://github.com/piyushimself/files/actions/runs/45953382752) was downloaded and inspected: 528 files; 34 desktop pages; 68 mobile checks; 96 iframe loads; 20 search, 14 select and 15 filter controls; 3 tabs; 4 shell controls; 7 direct mature-app gates; 21 mature iframe-sync checks; 33 theme-sync; 32 font-sync; 32 scale-sync; 63 filter disclosures; 34 reader menus; and 204 mobile reader-shell controls. It reports zero automated issues and zero preliminary accessibility findings. These are automated checks, not WCAG conformance or assistive-technology certification.
- Pages preview artifact [15177758557](https://github.com/piyushimself/files/actions/runs/45953382752) was downloaded and inspected: 122 tar entries, 83 regular files, 68 HTML files, zero PDF/DOCX/Pine files and one TXT file (`robots.txt`). No internal publishing report, source inventory or extracted source text is present.
- Visual inspection of #369 screenshots confirmed readable homepage desktop/mobile layouts and the 300 Animated Films mobile middle rows; ranks 7–16 remain on one line. The Manga & Comics Archive dark-desktop screenshot still has subdued sidebar/filter labels on its dark panel. The #369 artifact has dark-desktop captures but no dark-mobile screenshot set. Measured contrast and dark-mode mobile acceptance remain open. Sampled screenshot review is not a full page-by-page manual pass.
- Existing main-run artifacts remain exposed at this checkpoint. GitHub artifact metadata still reports `expired: false` for source-review artifact [15103848500](https://github.com/piyushimself/files/actions/runs/45794785456), expiry 27 November 2026 09:46:13 UTC (15:16:13 IST), and old Pages artifact [15104822142], expiry 09:56:16 UTC (15:26:16 IST). The source-review ZIP was previously downloaded and inspected: it contains 49 extracted source-text files and all 49 manifest redaction maps are empty. Old browser-QA artifact [15105410621] still contains `PUBLISHING-REVIEW.md` and expires 10 December 2026 09:56:13 UTC; corrected source-derived PDF preview [15104820560] expires 10 December 2026 09:46:04 UTC. The GitHub integration exposes no artifact-deletion action. Re-check actual downloadability after expiry; an expiry timestamp alone is not proof of removal.
- All 11 manual acceptance items in `PAGE-AUDIT.md` remain unchecked. They cover complete desktop/mobile page review; interaction states; light/dark themes, fonts and scaling; sticky controls; measured contrast; keyboard, screen-reader and reduced-motion behavior; complete PDF/DOCX/OCR review; source-to-output completeness; links/images/console/sitemap; catalogue reconciliation; and missing-title/H1 fallback.
- Editorial findings remain open: Asian Books scope/placeholders (25 placeholder markers and 40 “Not Asian” statements); Cinema 900 cover/body 300-versus-900 and 835-item comparison; Global Kids Books 317-versus-600+, roughly 55% overlap and uncited developmental claims; other catalogue-count conflicts; URL validation; bibliographies, quotations, attribution, author/edition metadata, age suitability and rating provenance. Workflow #369 did not perform a new source-content review or close these findings.
- All 49 original source artifacts remain excluded from Pages because publication-permission evidence is absent, but the public GitHub repository still exposes the originals. This is a documented rights/permission block, not evidence that the source copies are private. Do not change repository visibility, delete originals or rewrite history without the owner's informed decision.
- Pine static checks pass. TradingView compilation/backtesting and venue-specific calibration remain external dependencies and are not Reading Room website deployment gates.
- **Status: IN PROGRESS — not a completion certificate.** Exact-head PR automation is validated for the prior head, but this documentation refresh still needs exact-head validation; historical artifacts have not yet expired/been verified unavailable; manual and editorial acceptance remain open; PR review/merge and post-merge production deployment/regression remain outstanding.

### Current completion gates

1. After 15:16 IST and 15:26 IST on 27 November, re-fetch metadata and attempt downloads for artifacts 15103848500 and 15104822142; record expiry only if GitHub reports expired and download is unavailable.
2. Keep artifacts 15105410621 and 15104820560 on the exposure watch until their December expiries or owner deletion; verify actual unavailability.
3. Complete or individually disposition all 11 manual acceptance items with evidence, including measured contrast, keyboard/screen-reader/reduced-motion behavior and dark-mobile screenshots.
4. Resolve or individually document the editorial findings and source-permission decisions.
5. Obtain PR review. Do not merge solely because #369 passed; validate the new documentation head first.
6. After review/acceptance and merge, run a fresh main workflow, inspect logs/artifacts, verify desktop/mobile regression against production and confirm the Pages deployment SHA.
7. Refresh the final status report on main against the deployed commit.

---


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

### Current completion gates

1. Delete or verify expiry of the old source-review, publishing-review and source-derived PDF artifacts; re-check their downloadability after the recorded expiry times.
2. Finish or individually disposition every manual acceptance item with evidence, not just a green automated run.
3. Resolve or individually document the editorial findings and source-permission decisions.
4. Obtain review of PR #28. Keep it open until the evidence and description are current.
5. After merge, run a fresh main build, inspect its logs and artifacts, verify desktop/mobile regression against production, and confirm the Pages deployment SHA.
6. Refresh the final report on main against the deployed commit.



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


**Status: IN PROGRESS — not a completion certificate.**  
**Last verified:** 27 November 2026, 09:40 IST (Asia/Kolkata)
**Repository:** [piyushimself/files](https://github.com/piyushimself/files)  
**Published site:** https://piyushimself.github.io/files/

## Current verified checkpoint — 27 November 2026, 06:17 IST (Asia/Kolkata)

### Repository, pull requests and workflows
- Default branch `main` remains at [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e). Main workflow #356 / run [45794785456](https://github.com/piyushimself/files/actions/runs/45794785456) passed build and GitHub Pages deployment for that exact SHA. The deploy log created the Pages deployment for the same SHA and reported success.
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open on `remediation/stop-public-source-review-artifacts-2026-11-26`, latest head `6bfa3896eefab97f0dcc4c0431144191095ee40d`, based on the current main SHA. It has 17 commits, no submitted reviews, no inline review threads, and no open repository issues. Its description was refreshed at 06:17 IST to record workflow #359's completion and the updated documentation; the new documentation-only head still requires exact-head workflow validation.
- Exact-head workflow #359 / run [45882706873](https://github.com/piyushimself/files/actions/runs/45882706873) completed successfully for `1e6fab3cd995bf61b6c5cbca1d3a235cb81257ce`. Build and Chromium desktop/mobile QA passed; deployment was correctly skipped for a pull-request event.
- The #359 build steps passed site generation, generated-app validation, Pine static invariants, corrected-source-PDF validation and real-browser QA. The complete build log contains no `document_review_extract` step, source-review inventory, filenames, rights-marker categories or redaction-count output.

### PR #28 browser and Pages preview artifacts
- Browser QA artifact [15148637645](https://github.com/piyushimself/files/actions/runs/45882706873) contains 528 files. Its report records 34 desktop pages, 68 mobile checks, 96 iframe loads, 20 search controls, 14 select controls, 15 filter controls, 3 tabs, 4 shell controls, 7 direct mature-app gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader-shell controls and 34 reader menus. It reports zero automated issues and zero preliminary accessibility warnings.
- I downloaded and inspected the #359 ZIP and report. Actual homepage desktop/mobile screenshots are readable. The 300 Animated Films middle desktop/mobile captures are readable; ranks 10–16 remain on one line on mobile. This is sampled visual confirmation plus automated regression, not exhaustive human review or formal accessibility certification.
- Pages preview artifact [15147284705](https://github.com/piyushimself/files/actions/runs/45882706873) contains 122 archive entries and 68 HTML files. Its file types are HTML, CSS, JS, JSON, SVG, XML, webmanifest and `robots.txt`; no source PDFs, DOCX, Pine files, extracted source text or internal review reports are present.
- #359 produced only the browser QA and Pages artifacts. It did not upload a corrected source-derived PDF preview. The corrected Personal Reference PDF validator passed ephemerally in the build job; this does not constitute a fresh public PDF artifact or full-page content acceptance.

### Existing public workflow artifacts and expiry
- Main run #356 artifact [15103848500](https://github.com/piyushimself/files/actions/runs/45794785456) remains listed as `expired: false` at this checkpoint. It contains 49 extracted source-text files, a manifest, summary and README (5,457,766 characters / 915,683 words); all 49 manifest `redactions` maps are empty. It is not a verified sanitized copy. Its expiry is **27 November 2026, 09:46:13 UTC (15:16:13 IST)**.
- Main browser QA artifact [15105410621](https://github.com/piyushimself/files/actions/runs/45794785456) remains downloadable and contains generated `PUBLISHING-REVIEW.md`; it expires **10 December 2026, 09:56:13 UTC (15:26:13 IST)**.
- Main corrected-PDF preview [15104820560](https://github.com/piyushimself/files/actions/runs/45794785456) expires **10 December 2026, 09:46:04 UTC (15:16:04 IST)**. PR #28's earlier corrected-PDF preview [15132451495](https://github.com/piyushimself/files/actions/runs/45848514609) expires **10 December 2026, 15:24:54 UTC (20:54:54 IST)**.
- Earlier PR browser QA [15134060952](https://github.com/piyushimself/files/actions/runs/45848514609) expires **10 December 2026, 15:32:58 UTC (21:02:58 IST)**; its Pages preview [15134215945](https://github.com/piyushimself/files/actions/runs/45848514609) expires **27 November 2026, 15:33:02 UTC (21:03:02 IST)**.
- New #359 Pages preview [15147284705] expires **27 November 2026, 19:27:58 UTC (28 November, 00:57:58 IST)**; #359 browser QA [15148637645] expires **10 December 2026, 19:27:55 UTC (11 December, 00:57:55 IST)**.
- The connected GitHub integration exposes no workflow-artifact deletion action. Existing artifacts remain downloadable until their recorded expiry unless the repository owner deletes them through GitHub Actions. PR #28 prevents future recurrence; it does not revoke old artifacts.
- `PUBLISHING-REVIEW.md` is not a tracked repository-root file; it was generated during the old main build and included in the old #356 browser QA ZIP.

### Production deployment
- Production remains on the successful main workflow #356 for SHA `d146196...`; the deployment log confirms the Pages build version and reports success for `https://piyushimself.github.io/files/`.
- PR workflow #359 did not deploy. A fresh main-branch build, browser regression and Pages deployment are still required after PR #28 is reviewed and merged.
- An independent live-site fetch through the external browser was attempted but the Pages hostname was inaccessible through that route. GitHub's deployment record is confirmed; independent HTTP reachability is not.

### Editorial findings and manual acceptance still open
- Asian-books curriculum: 25 placeholder markers and 40 “Not Asian” statements; comparative-vs-Asian-only scope and repeated/comparator entries need an editorial decision.
- Cinema 900: cover/body 300-versus-900 contradiction and the 835-entry `library-3` comparison need a documented deduplication rule.
- Global Kids Books: eight age-band counts total 317 rather than “600+”; roughly 55% overlap with the FINAL guide; developmental claims, age suitability, metadata and canonical-version decision remain open. Its layout correction is separately validated.
- Other count/scope issues remain across fictional books, inspirations, writing prompts, Frida film list, filmography and ratings/encyclopedia collections. Resource URLs, bibliographies, quotations, attribution, author/edition metadata, age suitability, selection rationale and rating provenance are not fully reconciled.
- All 11 manual acceptance items in `PAGE-AUDIT.md` remain unchecked/incomplete: full page-by-page desktop/mobile human review; all control/interaction states; theme/font/text-scale behavior; sticky-header behavior; measured contrast; keyboard, screen-reader and reduced-motion acceptance; full PDF/DOCX/image-only-page/OCR inspection; source-to-output completeness; links, console and sitemap; catalogue reconciliation; and missing-title/H1 fallback review.
- All 49 original source artifacts remain withheld from Pages because publication permission evidence has not been established. The repository itself is public, so the originals remain accessible in GitHub. Do not change repository visibility or rewrite history without the user's specific informed confirmation. This is a republication/visibility blocker, not a reason to mark unrelated editorial findings complete.
- Pine Script findings are statically reviewed, but TradingView compilation/backtesting and venue-specific fee, spread, slippage and funding validation remain external checks; do not present indicator metrics as validated strategy performance.
- **Status: IN PROGRESS — not a completion certificate.**

### Next acceptance gates
1. Refresh the PR description against workflow #359 and the current head after the documentation update.
2. Have the repository owner delete the exposed #356 source-review artifact before its 15:16 IST expiry, or verify its automatic expiry immediately afterward; then verify it is no longer downloadable.
3. Allow older browser/PDF artifacts to expire or have the owner delete them; verify their unavailability.
4. Complete or individually evidence-disposition all 11 manual acceptance items.
5. Resolve or explicitly disposition every remaining editorial finding and permission-dependent publication decision.
6. Obtain review and merge only after exact-head evidence is current; then require a fresh main-branch build, production desktop/mobile regression and Pages deployment.
7. Update this report after the post-merge main run.

Historical checkpoints below are retained for traceability and are superseded by this section.



## Historical checkpoint — 21 November 2026

- Application/deployment checkpoint: `0bb979ecaeac463f0fdb4805ad9b8f1e394b0a28` (PR [#25](https://github.com/piyushimself/files/pull/25), squash-merged). The status-document refresh is commit `a385b394ca0dacb82e8ab4819455eca210e26686` on `main` (documentation-only); its follow-up workflow #335 is pending.
- PR #25 adds accessible names to the known unlabeled input, textarea and select controls in generated app copies. The original root-level source HTML files are not changed by this patch.
- Exact-head PR workflow [#333](https://github.com/piyushimself/files/actions/runs/44787046143) passed on `1701041da7e033d7519eeaade9f0d7af64241ca8`. Build succeeded; deploy was correctly skipped for the pull-request event.
- Post-merge main workflow [#334](https://github.com/piyushimself/files/actions/runs/44875546466) passed for the exact merge commit `0bb979ecaeac463f0fdb4805ad9b8f1e394b0a28`. Both build and GitHub Pages deploy jobs succeeded.
- Browser QA artifact [14696205084](https://github.com/piyushimself/files/actions/runs/44875546466) was downloaded and inspected. It reports 34 catalogue items, 32 apps, 34 wrappers, 34 desktop pages, 68 mobile page checks, 96 iframe loads, 20 search controls, 14 select controls, 15 filter controls, 3 tabs, 4 shell controls, 7 direct mature-app gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls and 34 reader menus. It reports **0 automated issues and 0 preliminary accessibility warnings**.
- The #334 result supersedes the earlier #325 warning inventory of 93 repeated capture-level warnings. The zero-warning result is scoped to the current automated scanner and known controls; it is not a WCAG audit, screen-reader certification or proof that every interactive element is accessible.
- The PR #25 run artifact also reported zero warnings, and the post-merge #334 run independently confirms the fix survived merge and deployment.
- The Pages deployment is confirmed by the successful deploy job. Independent external HTTP reachability from this runtime remains unverified.
- The latest redacted document-review artifact is available in run #334 (artifact [14696115498](https://github.com/piyushimself/files/actions/runs/44875546466)); this artifact is extraction/triage evidence, not full human content review or rights clearance.

**Current disposition: IN PROGRESS.** The accessible-name remediation is merged, the main build and deployment passed, and the current automated browser report is clean. The remaining content, source-document, rights, manual accessibility and TradingView validation work below is still open unless explicitly closed by newer evidence.

---

# Reading Room remediation — current status

**Status: IN PROGRESS — not a completion certificate.**  
**Last verified:** 19 November 2026, 12:48 IST  
**Repository:** [piyushimself/files](https://github.com/piyushimself/files)  
**Published site:** https://piyushimself.github.io/files/

## Current repository state

- Last fully validated `main`: `b6d68eff58469c7adda14cc9edee3ed04ef01101` (main workflow #315 passed for this exact SHA). The subsequent documentation-only sync commits are `e6521137c65590d1d30e4463c78239d7a8fc24b9` (status), `a9b1570a83fe3d1ad249d62008fb15b6f1561b59` (page audit) and `3503549b1d205446305fca5d5d6e7cddd7e98100` (handoff). The latest main tip before this status refresh is `3503549b1d205446305fca5d5d6e7cddd7e98100`; the follow-up workflow/deployment for the documentation-only updates still needs verification.
- PR [#19](https://github.com/piyushimself/files/pull/19) was squash-merged as `0699b3a10090ddb9c018ba37116078597d8b0ccd`. It applies ten narrowly scoped source-PDF corrections, adds the reproducible 647-row film manifest/audit and validator, reconciles the source inventory, fixes three generated homepage catalogue/search metadata mismatches, and refreshes the review documentation. Later documentation-only commits brought `main` to `b6d68eff58469c7adda14cc9edee3ed04ef01101`.
- PR [#20](https://github.com/piyushimself/files/pull/20) was merged earlier as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`. It adds per-side spread-cost estimates to entry, partial-exit and final-exit legs and caps partial allocation below 100%. PR #16 was closed as superseded.
- PR [#17] age-gate QA fix is included in main at `1903c3787156523193380affa23b13ed4c6d2e11`.
- No open pull requests are currently reported by GitHub.

## Latest CI and browser evidence

### Latest main-branch regression and deployment — workflow #315 (19 November 2026, 12:48 IST)

- Last fully validated `main`: `b6d68eff58469c7adda14cc9edee3ed04ef01101`. A compare against the preceding #312-verified commit `8c279d771b1b4a59ca81a10f5a8c0aa9d3c7f40c` shows three documentation-only commits touching `PAGE-AUDIT.md`, `REMEDIATION-HANDOFF.md` and `REMEDIATION-STATUS.md`; no application/source-code changes were introduced after that checkpoint.
- Main workflow [#315](https://github.com/piyushimself/files/actions/runs/44458475169) completed successfully for the exact `b6d68eff58469c7adda14cc9edee3ed04ef01101`. The build and deploy jobs both succeeded. The build log checked out this SHA; the deploy log created a Pages deployment for the same SHA and reported success.
- Browser QA artifact [14497854888](https://github.com/piyushimself/files/actions/runs/44458475169) was downloaded and inspected. Its report records 34 desktop pages, 68 mobile page checks, 96 iframe loads, 20 search controls, 14 select controls, 15 filter controls, 3 tabs, 4 shell controls, 7 direct mature-app gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls, 34 reader menus and **zero automated issues**. The ZIP contains 337 screenshots. Contact sheets were inspected for all 34 wrapper desktop/mobile captures, 33 app-mobile captures and 32 app-initial-mobile captures; representative full-size mobile captures were also inspected. This remains automated plus broad visual regression evidence, not exhaustive per-control or accessibility certification.
- Pages artifact [14498089145](https://github.com/piyushimself/files/actions/runs/44458475169) was downloaded and inspected. Its tar contains 123 entries and 69 HTML files; no PDF, DOCX or Pine source files are present. `robots.txt` is the only text file.
- Redacted document-review artifact [14498613806](https://github.com/piyushimself/files/actions/runs/44458475169) was inspected. It records 49 source artifacts, one exact duplicate group and zero extraction errors. OCR was applied to page 82 of `1000_Creative_Educational_Cultural_Links.pdf` and pages 27 and 90 of `Aag_Ki_Kavitayen.pdf`, with no OCR errors. This is extraction evidence only; it does not establish factual correctness, page-layout completeness or publication rights.
- The build step “Upload temporary source PDFs for visual review” was skipped. Therefore #315 produced no fresh source-PDF visual-review artifact and closes no additional PDF page-inspection findings.
- GitHub reports no open PRs. PR #19 and #20 are merged; PR #16 is closed as superseded. After #315, the three documentation-only sync commits listed above were pushed; they do not alter application/source code, but their latest main workflow/deployment has not yet been verified. Independent live-site HTTP reachability remains unverified from this runtime; the #315 Pages deployment itself is confirmed.
- **Status remains IN PROGRESS.** The unresolved content/count, editorial, link/licence/attribution, ratings-provenance, full source-page review, 11 manual page/accessibility acceptance items, rights/ownership and TradingView/venue-validation findings remain open or dependent on owner evidence/decisions/external validation.

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

### Earlier main-branch regression and deployment (#305)

[Main workflow #305](https://github.com/piyushimself/files/actions/runs/44442583472), for `main` commit `0bbe318ae4341aa16393ff95d9dd24452bed46d7`, completed successfully on 19 November 2026. Both jobs passed: build and GitHub Pages deployment. The build ran generated-app validation, Pine static invariants, corrected-source-PDF validation, redacted extraction, and real-browser Chromium QA.

The #305 browser report (artifact [14492822395](https://github.com/piyushimself/files/actions/runs/44442583472)) records:
- 34 desktop collection pages, 68 mobile page checks and 96 iframe loads;
- 20 search, 14 select, 15 filter, 3 tab and 4 shell controls tested;
- 7 direct mature-app gates and 21 mature iframe-sync checks;
- 34 reader menus, 204 mobile reader controls and 63 filter disclosures;
- 33 theme, 32 font and 32 text-scale synchronization checks; and
- **zero automated issues** across 337 screenshots.

I downloaded the latest QA artifact and inspected its report. Contact sheets were visually swept for all 34 wrapper pages at desktop, tablet and mobile widths, and for 33 app captures at desktop and mobile widths. This is broad page-level visual evidence, not pixel-by-pixel review of every state or exhaustive testing of every bespoke control.

The matching Pages artifact [14492268281](https://github.com/piyushimself/files/actions/runs/44442583472) was downloaded and inspected. It contains the generated site; no PDF, DOCX or Pine source files are present, and `robots.txt` is the only `.txt` file. Source documents remain withheld from Pages.

At that checkpoint, the main deployment was confirmed by GitHub Actions for `0bbe318ae4341aa16393ff95d9dd24452bed46d7`. An independent fetch of the published URL still cannot be completed from this runtime: the web fetcher reports the Pages URL is inaccessible. This is an environment/network limitation, not proof of an outage.

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

GitHub Actions confirms the latest Pages deployment in workflow #305 for main commit `0bbe318ae4341aa16393ff95d9dd24452bed46d7`. A separate live HTTP fetch remains unverified: the web fetcher cannot access the Pages URL from this runtime. This does not prove the site is down; verify from an independent network if live reachability is a required sign-off item.

## Next acceptance work

1. Workflow #305 now confirms the main build, Chromium QA and Pages deployment for `0bbe318ae4341aa16393ff95d9dd24452bed46d7`; verify the published URL from an independent network if possible.
2. Continue objective count reconciliation and correct source documents where the evidence is sufficient; preserve explicit uncertainty where it is not.
3. Obtain the Asian-books scope decision and Cinema 900 deduplication rule before rewriting those works.
4. Complete the remaining page-by-page interaction, visual and accessibility checks; disposition every one of the 11 manual acceptance items with evidence or a specific blocker.
5. Verify resource URLs, licences, bibliographies, quotations, rating provenance and as-of dates; record source and date for every time-sensitive claim.
6. Obtain rights/ownership evidence or keep sources withheld and make an informed decision about public-repository exposure.
7. Complete external TradingView and venue-specific validation or document each exact dependency and the limits on any performance claims.

**Completion rule:** do not mark this project complete until every actionable finding is corrected and validated or individually documented as blocked by concrete evidence, permissions, an owner decision or an external dependency; the final main-branch regression and deployment are confirmed; the manual acceptance list is fully dispositioned; and this status report is synchronized with the final evidence. Workflow #305 closes the previously pending post-PR #19 main build/deployment gate, but it does not close the remaining editorial, rights, accessibility or external TradingView findings.


## Latest main regression and deployment — 19 November 2026, 09:40 IST

- Current main: `53d14aee33383421e640af3b59126ca6a2f47edb` (commit: “Record latest main deployment in document review”).
- Main workflow [#309](https://github.com/piyushimself/files/actions/runs/44450778850) completed successfully. Build and GitHub Pages deploy both succeeded; generated app validation, Pine static invariants, corrected-PDF validation, redacted extraction, and Chromium QA all passed.
- Browser artifact [14494544620](https://github.com/piyushimself/files/actions/runs/44450778850) was downloaded and its report inspected: 34 catalog items, 32 apps, 34 desktop pages, 68 mobile checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tab, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls, 34 reader-menu checks, and zero automated issues. Screenshots for desktop/tablet/mobile and app initial/interaction states are included. This report is automated evidence, not an accessibility certification or exhaustive content review.
- The Pages artifact was generated and deployment succeeded. The Pages artifact from this run has not yet been downloaded/inspected in this checkpoint; the previous verified Pages artifact (#305) excluded source PDFs, DOCX and Pine files.
- Run #300 was cancelled during OCR setup before build/QA; it is superseded by successful run #309 and is not a failed test.
- There are no open PRs at this check. No new source-document findings are closed by this deployment.
- Independent live HTTP reachability remains unverified from this runtime. GitHub Pages deployment success is confirmed; external DNS/fetch limitations do not prove the site is down.

**Status remains IN PROGRESS.** The unresolved count/scope, link/licence/attribution, ratings provenance, page-by-page source review, 11 manual acceptance items, rights/ownership, and TradingView/venue-validation items listed above remain open or blocked. Do not claim 100% completion.


## Follow-up main verification — 19 November 2026, 10:00 IST

- Current main: `8c279d771b1b4a59ca81a10f5a8c0aa9d3c7f40c`.
- Main workflow [#312](https://github.com/piyushimself/files/actions/runs/44456566278) completed successfully for this exact SHA. Build and Pages deploy both succeeded; generated-app checks, Pine static invariants, corrected-source-PDF validator, redacted extraction and Chromium desktop/mobile QA passed.
- Browser artifact [14498832464](https://github.com/piyushimself/files/actions/runs/44456566278) was downloaded and inspected. It reports 34 catalogue items, 32 apps, 34 desktop wrappers, 68 mobile checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls, 34 reader menus and zero automated issues.
- Pages artifact [14498473147](https://github.com/piyushimself/files/actions/runs/44456566278) was downloaded and inspected: 123 tar entries, 69 HTML files; no PDF, DOCX or Pine source files. Only one .txt file is present (robots.txt).
- Redacted extraction artifact [14498725745](https://github.com/piyushimself/files/actions/runs/44456566278) was inspected: 49 source artifacts processed, one exact duplicate group, zero extraction errors. This confirms extraction only; it does not establish content correctness, visual completeness or publication rights.
- No open PRs are currently reported. No additional source-document finding has been closed by this run. Independent live HTTP reachability remains unverified from this runtime.

**Status remains IN PROGRESS.** All outstanding content/count, rights, accessibility/manual acceptance and TradingView/venue validation items remain as previously listed.
