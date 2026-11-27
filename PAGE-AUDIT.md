## Latest verified checkpoint — 27 November 2026, 23:17 IST (Asia/Kolkata)

- Exact PR head [`6a05295abb4fe7b84a873e7e30fe0ecc3c4da8b6`](https://github.com/piyushimself/files/commit/6a05295abb4fe7b84a873e7e30fe0ecc3c4da8b6) passed exact-head workflow [#371](https://github.com/piyushimself/files/actions/runs/45983167157). Build, generated-app validation, Pine static checks, corrected-PDF validation and Chromium desktop/mobile automation passed; deploy was skipped correctly for a PR event.
- Browser-QA artifact [15190741334](https://github.com/piyushimself/files/actions/runs/45983167157) contains 528 files, including 525 screenshots. It records 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader-shell controls, zero automated issues and zero preliminary accessibility warnings. It contains no dark-mobile screenshots.
- Pages preview artifact [15190487267](https://github.com/piyushimself/files/actions/runs/45983167157) contains 122 tar entries and 68 HTML files, with no source PDFs, DOCX, Pine files or internal publishing-review inventory.
- Visual inspection: homepage mobile is readable; 300 Animated Films mobile ranks 7–16 remain on one line; Manga & Comics Archive's dark-desktop filter/sidebar labels remain subdued. The archive mobile capture is light mode, so it does not close dark-mobile acceptance.
- All 11 manual acceptance items below remain unchecked. Automated zero-issue/zero-warning output is not measured contrast, full keyboard/screen-reader/reduced-motion acceptance, or exhaustive human review. Keep every checkbox open until individually validated with evidence or explicitly blocked with a concrete dependency/permission reason.

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

### Manual acceptance disposition at this checkpoint

The 11-item checklist below remains entirely unchecked. #370's zero automated issues and zero preliminary accessibility findings do not close manual acceptance. The sampled screenshots reviewed here were the homepage mobile, 300 Animated Films mobile middle rows, and Manga & Comics Archive dark desktop. The mobile ranks 7–16 remain on one line. The dark sidebar/filter labels remain visually subdued. No dark-mobile screenshots were generated, and no measured contrast, keyboard-only, real screen-reader, reduced-motion or exhaustive per-page interaction pass was performed.

Keep all 11 checklist items open until each is individually passed with evidence or explicitly blocked with a concrete dependency/permission/evidence reason. Do not mark full page review complete based on a screenshot sample or automated zero-warning report.

---

# Page-by-page editorial and publishing audit

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

### Manual acceptance disposition at this checkpoint

The 11-item checklist below remains entirely unchecked. The #369 report's zero automated issues and zero preliminary accessibility findings do not close manual acceptance. Actual sampled screenshots reviewed in this checkpoint: homepage desktop and mobile; Manga & Comics Archive dark desktop and light mobile; Manga & Comics Master dark desktop; and 300 Animated Films mobile middle rows. The Manga & Comics Archive dark-desktop sidebar/filter labels remain visually subdued. No dark-mobile screenshot set was generated. No measured contrast, keyboard-only, real screen-reader, reduced-motion or exhaustive per-page interaction pass was performed in this checkpoint.

Keep all 11 checklist items open until each is individually passed with evidence or explicitly blocked with a concrete dependency/permission/evidence reason. Do not mark the full page-review item complete based on a screenshot sample or a zero-warning automated report.


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

### Manual acceptance disposition

The 11-item manual checklist remains open. Automated Chromium coverage is useful but does not close keyboard-only operation, real screen-reader behavior, reduced-motion behavior, measured contrast, complete content review or every interaction state. The current screenshot evidence is sampled: homepage desktop/mobile and 300 Animated Films mobile rows were inspected; five dark-desktop targets were reviewed, with four materially improved and Manga & Comics Archive still visually subdued in part. No dark-mobile screenshot set was generated by #368.

Do not convert a zero-warning automated report into a pass for any manual checklist item. Record each item as passed only with its own evidence, or blocked only with a concrete dependency/permission/evidence reason.



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


## Current checkpoint — 27 November 2026, 06:17 IST (Asia/Kolkata)
- Latest `main`: [`d146196bf3490ca4fff0a982dcd2ec6c669e0c0e`](https://github.com/piyushimself/files/commit/d146196bf3490ca4fff0a982dcd2ec6c669e0c0e). Main workflow #356 / run [45794785456](https://github.com/piyushimself/files/actions/runs/45794785456) passed build and Pages deployment for that exact SHA.
- PR [#28](https://github.com/piyushimself/files/pull/28) remains open at head `1e6fab3cd995bf61b6c5cbca1d3a235cb81257ce`, based on current main. It has no submitted reviews or inline review threads; no open repository issues were found.
- Exact-head workflow #359 / run [45882706873](https://github.com/piyushimself/files/actions/runs/45882706873) passed build and Chromium desktop/mobile QA for the exact PR head; deployment was skipped for the PR event. The complete build log contains no document-review extraction step or per-file source-review inventory.
- Browser artifact [15148637645](https://github.com/piyushimself/files/actions/runs/45882706873) contains 528 files and reports 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, zero automated issues and zero preliminary accessibility warnings. The report also records 20 search, 14 select, 15 filter, 3 tab, 4 shell, 7 direct mature-app, 21 mature iframe-sync, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter-disclosure and 34 reader-menu checks.
- I downloaded the #359 browser artifact and inspected its report and actual screenshots: homepage desktop/mobile are readable; 300 Animated Films middle desktop/mobile captures are readable; ranks 10–16 remain on one line on mobile. This is sampled visual evidence, not exhaustive manual acceptance.
- Pages preview [15147284705](https://github.com/piyushimself/files/actions/runs/45882706873) contains 122 archive entries / 68 HTML files. No source PDFs, DOCX, Pine files, extracted source text or internal reports are present.
- Existing main source-review artifact [15103848500] remains downloadable (`expired: false`) and expires **27 November 2026, 09:46:13 UTC (15:16:13 IST)**. It contains 49 extracted files and empty redaction maps; it is not a verified sanitized copy. Old browser QA [15105410621] contains generated `PUBLISHING-REVIEW.md`; main corrected-PDF preview [15104820560] and PR corrected-PDF preview [15132451495] also remain downloadable until December. No artifact-deletion operation is available through the connected GitHub integration.
- Production remains on main SHA `d146196...`; #359 is a PR preview, not a deployment. The main deploy log confirms Pages success for the exact main SHA. Independent live-site HTTP reachability remains unconfirmed through the external browser.
- The 11 manual acceptance items below remain unchecked. Editorial findings remain open: Asian Books 25 placeholders / 40 “Not Asian” statements; Cinema 900 300/900/835 discrepancy; Global Kids Books 317-versus-600+ count, ~55% overlap and uncited developmental claims; other catalogue counts, URLs, bibliographies, quotations, attribution, metadata, age suitability and rating provenance.
- All 49 source artifacts remain withheld from Pages because publication permissions are unestablished, but the originals remain accessible in the public GitHub repository. Do not change visibility or rewrite history without informed confirmation.
- **Status: IN PROGRESS.** Automated desktop/mobile regression and sampled visual checks pass on the PR preview; old public artifact exposure, manual acceptance, editorial disposition and post-merge production verification remain outstanding.

**Status: IN PROGRESS.** Historical checkpoints below are retained; this checkpoint supersedes their repository and workflow state.


## Latest main-branch regression snapshot — 19 November 2026, 12:48 IST

Main workflow [#315](https://github.com/piyushimself/files/actions/runs/44458475169) passed for exact main commit `b6d68eff58469c7adda14cc9edee3ed04ef01101`. Build and GitHub Pages deployment both succeeded; the deployment log confirms the same Pages build version. The preceding #312-verified commit was `8c279d771b1b4a59ca81a10f5a8c0aa9d3c7f40c`; the three commits since then changed only this audit, the handoff and the status report.

Browser artifact [14497854888](https://github.com/piyushimself/files/actions/runs/44458475169) reports 34 desktop pages, 68 mobile checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls, 34 reader menus and zero automated issues. The 337-screenshot artifact was downloaded; contact sheets were inspected for all 34 wrapper desktop/mobile captures, 33 app-mobile captures and 32 app-initial-mobile captures. Representative full-size mobile pages were also inspected. This does not replace exhaustive control-state testing or formal accessibility review.

Pages artifact [14498089145](https://github.com/piyushimself/files/actions/runs/44458475169) was inspected: 123 tar entries, 69 HTML files, no PDF/DOCX/Pine source files, and `robots.txt` as the only text file. Redacted document-review artifact [14498613806](https://github.com/piyushimself/files/actions/runs/44458475169) reports 49 source artifacts, one exact duplicate group, zero extraction errors and OCR on three pages (1000 Creative Links p.82; Aag Ki Kavitayen pp.27 and 90). The source-PDF visual-review upload step was skipped in #315, so no new PDF page-level visual acceptance is claimed.

All 11 manual acceptance items below remain unchecked. The 34 desktop / 68 mobile automated checks and screenshot sweep are not a formal WCAG contrast audit, screen-reader or keyboard-only certification, reduced-motion review, or page-by-page factual/editorial review of every source document. Rights/ownership, source-content, catalogue reconciliation and external TradingView/venue validation remain open as recorded below.


## Earlier main-branch regression snapshot — 19 November 2026, 08:48 IST

Main workflow [#305](https://github.com/piyushimself/files/actions/runs/44442583472) passed for exact main commit `0bbe318ae4341aa16393ff95d9dd24452bed46d7`, including build and Pages deployment. Its browser artifact [14492822395](https://github.com/piyushimself/files/actions/runs/44442583472) reports 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, 34 reader menus, 63 filter disclosures, 33 theme-sync, 32 font-sync, 32 text-scale checks and zero automated issues. It also records 20 search, 14 select, 15 filter, 3 tab, 4 shell, 7 direct mature-gate and 21 mature iframe-sync checks.

I downloaded the artifact and inspected its report. Contact sheets were swept for all 34 wrapper pages at desktop/tablet/mobile and 33 app captures at desktop/mobile. The Pages artifact [14492268281](https://github.com/piyushimself/files/actions/runs/44442583472) was inspected: no PDF, DOCX or Pine source files are present; `robots.txt` is the only `.txt` file. This confirms the latest main deployment job and source exclusion from the Pages artifact, not independent live HTTP reachability. The external fetcher cannot access the Pages hostname from this runtime.

The 11 manual acceptance items below remain open or only partially evidenced. The latest automation does not replace exhaustive control/state testing, keyboard-only and screen-reader review, formal contrast/WCAG measurement, reduced-motion testing, or page-by-page review of all source documents.

## Latest regression snapshot — 19 November 2026

- PR #19 exact head `0f3bc8f57e0a0381397a5b8ce6f1d477e2102e0e` passed [workflow #299](https://github.com/piyushimself/files/actions/runs/44436114541). The report records 34 desktop collection pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, 34 reader menus, 7 direct mature-app gates, 63 filter disclosures and **zero automated issues**.
- The artifact's 34 wrapper pages were visually swept in contact sheets at desktop, tablet and mobile widths; the 33 app-mobile screenshots were also swept. This catches page-level outliers but is not a pixel-level review of every app state or control.
- The corrected-source-PDF artifact was inspected. Selected changed pages across the ten corrected PDFs were rendered and visually checked; not every page of every source document has been reviewed.
- Main workflow [#283](https://github.com/piyushimself/files/actions/runs/44435251703) passed build, Chromium QA and GitHub Pages deployment for the earlier main commit `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`. It is not deployment evidence for the later PR #19 merge commit `0699b3a10090ddb9c018ba37116078597d8b0ccd`.
- The Pages artifact from PR #19 contains 34 published HTML collections and no PDF/DOCX/Pine source files. The repository remains public; omission from Pages does not make root-level files private.
- Main workflow #305 now confirms the build, browser QA and Pages deployment for the current main commit `0bbe318ae4341aa16393ff95d9dd24452bed46d7`. Independent live HTTP verification remains unconfirmed because this runtime's web fetcher cannot access the Pages hostname.

Automated Chromium coverage is not a formal WCAG audit, screen-reader certification, exhaustive keyboard-only test, reduced-motion verification, or full factual/editorial review. The 11 manual acceptance items below remain open and must be completed or individually dispositioned with evidence or a specific blocker.

## What has actually been inspected

The following checks were performed against source HTML:
- source byte size and empty-file detection;
- document title, script and form-control counts;
- embedded CSS declarations and class names for the most visibly problematic pages;
- exact duplicate detection for `top500_manga.html` and `top500_adult_manga.html`;
- filename/category matching and obvious false-positive maturity rules.

These checks are useful for triage, but they do **not** replace browser interaction testing, visual checks at desktop/mobile widths, keyboard testing, or a full semantic/content review. The `manga-comics-master.html` source includes a distinct Taboo Comics collection; its mature gate is intentional even though the page is also a broad multi-collection index.

## HTML source findings

| Source file | Finding / next action |
|---|---|
| `manga-1000.html` | Reviewed source CSS and class names. Legacy `.mc`, `.mt`, `.mi`, `.ma`, `.legend`, `.controls` require targeted contrast and sticky-header fixes. |
| `top500_adult_manga.html` | Reviewed source CSS and class names. Legacy `.manga-card`, `.manga-title`, `.manga-author`, `.controls` require coordinated surfaces and readable text. |
| `top500_manga.html` | Byte-identical to `top500_adult_manga.html`; build hashes source HTML and withholds the duplicate instead of showing two copies. |
| `manga-comics-master.html` | Large interactive index with tabs, controls and cards; requires browser interaction and mobile layout testing. |
| `manga-index.html` | Large interactive index; needs the same visual and filter-function checks. Mature/transgressive content must remain gated and noindex. |
| `manga-guide.html` | Static reading guide; verify semantic conversion preserves all sections and sequence. |
| `manga-archive-v4.html` | Large (about 1.2 MB) interactive source. The GitHub file-content preview returned an empty body because of its size, but the generated artifact contains the full app and browser screenshots confirm its collection renders. Retain the mature-content gate and complete filter/interaction checks. |
| `manhwa300.html` | Adult romance manhwa source; retain 18+ gate and noindex; verify filter behaviour after theme changes. |
| `manhwa_300_filter_app.html` | Missing `<title>` tag; visible H1 is `300 Adult Het Romance Manhwa`. Build metadata now uses the visible H1 when the title tag is absent, avoiding a filename-derived title. Retain 18+ gate and noindex. |
| `300_animated_films.html` | Interactive film table with search/filter controls; verify table responsiveness and filter operation. |
| `cinematic-database (1).html` | Large interactive film database; audit table/card contrast, sticky controls and filter combinations. |
| `cinematic_canon (1).html` | Large interactive film canon; verify search, category navigation and small-screen reading. |
| `film_collection_v8.html` | Large interactive collection; verify its 29 form controls and catalogue layout. |
| `sen-mood-movies.html` | Mature/sensual cinema collection; verify correct maturity treatment and filtering. |
| `blackout_poetry_tutorial.html` | Interactive tutorial with many sections and exercise controls; preserve its tutorial flow, not just a generic catalogue layout. |
| `bob_ross_complete_guide.html` | Interactive guide with supplies, legend and episode sections; preserve instructional structure and test toggles. |
| `free-art-resources.html` | Resource catalogue with category tabs and cards; verify all resource links and category filters. |
| `watercolour_tasks (1).html` | Painting journal; “Adult” in its title refers to adult painting tasks and must not automatically trigger an 18+ restriction. |
| `life-fiction-curriculum.html` | Editorial curriculum; preserve stages, book cards and explanatory context. |
| `living-curriculum-2026.html` | Editorial curriculum; preserve sequence and section hierarchy. |
| `human-development-curriculum.html` | Static curriculum with many headings and inline styles; review conversion for loss of visual/semantic structure. |
| `anime-manga-values-curriculum.html` | Interactive curriculum with controls; classify as Learning, with Manga & Comics cross-link where appropriate. |
| `asian_cinema_curriculum (1).html` | Interactive curriculum; verify its 20 controls and reading sequence. |
| `political-comics-list.html` | Interactive comics curriculum; classify under Manga & Comics and consider a Learning cross-link. |
| `four-arcs-library.html` | Large editorial library with interactive controls; preserve its four-part structure and explanatory text. |
| `The_Curators_Library.html` | Large interactive library; needs careful search/navigation and mobile checks. |
| `Qwen_html_20260604_f25nf6z8p.html` | Manga reflection list; use a human-readable page title/description in catalogue metadata. |
| `marginalia-diary.html` | Personal diary tool; retain as an interactive tool, not a static article. |
| `the-loom-tracker.html` | Interactive tracker; verify state persistence and control labels. |
| `typewriter.html` | Small writing tool; add a useful description and test input/output. |
| `collage-idea-generator.html` | Interactive generator; keep task-specific controls and validate generation flow. |
| `collage-idea-generato - Theme.html` | Near-duplicate generator variant; compare behaviour and decide whether both variants deserve separate catalogue entries. |
| `Big_library.html` | Large (about 1.5 MB) interactive source. The API text preview is empty for this file size; the generated artifact contains its embedded dataset. Verified section counts are corrected in the generated copy, not the original source. |
| `grand_library (2).html` | Large (about 1.6 MB) interactive source. The API text preview is empty for this file size; the generated artifact contains the embedded dataset. Verify its count and filters in the browser. |

## Category mapping decisions

- **Family:** children's reading guides and children's book collections are identified in the source inventory, but the underlying PDFs remain unpublished pending content, rights and sensitive-data review.
- **Reading & Literature:** fiction reading lists, poetry and literature-oriented curricula belong here. `blackout_poetry_tutorial.html`, `life-fiction-curriculum.html`, `Aag_Ki_Kavitayen.pdf` and the fictional-books list are mapped accordingly.
- **Security:** cybersecurity story material and the Pine Script/trading source files are identified, but there is no reviewed security HTML page in the current inventory. The PDFs and text/code sources remain unpublished pending review.
- **Learning:** broad personal-development curricula, courses and reflection resources belong here unless their primary purpose is clearly literature, art or another subject.
- **Art:** art tutorials, painting tasks, art resources and the Bob Ross guide belong here.
- **Cinema / Manga & Comics:** keep their specialist catalogue pages in their respective sections.

A document's filename is not proof of its contents or publication rights. No withheld PDF/DOCX/TXT/Pine source is promoted to the public catalogue solely because a category has no entries.

## Document review limitations

The 43 PDFs, 3 DOCX files, 1 legacy TXT file and 2 Pine scripts (49 source artifacts, 48 unique source documents after the exact duplicate PDF pair) have not yet all been inspected page by page in this pass. The GitHub text-file API cannot decode their binary contents as UTF-8; the extraction pipeline can scan/extract text during CI, but a successful scan does not establish copyright permission or human-reviewed content quality. These files remain withheld until the exact content is accessible and reviewed.

## Remaining acceptance checks

- [ ] Browser review of every published page at desktop and mobile widths.
- [ ] Test search, filters, tabs, sorting, pagination, toggles and export controls where present.
- [ ] Test light mode, dark mode, System/Serif/Mono font selection and text scaling on each page.
- [ ] Verify sticky controls do not hide page titles beneath the Reading Room header.
- [ ] Check contrast for every card, badge, legend, metadata label and selected state.
- [ ] Check keyboard focus, reduced motion, accessible labels and iframe titles.
- [ ] Inspect all PDF/DOCX pages (including image-only pages) and OCR output before any publication decision.
- [ ] Confirm source-to-output text completeness for each converted document.
- [ ] Check internal links, image paths, console errors and generated sitemap.
- [ ] Reconcile the published catalogue against this source inventory.
- [ ] Confirm that missing-title fallback uses visible H1 text and review remaining pages with no title/H1.

**Do not mark the archive complete until all acceptance checks are either passed or explicitly recorded as not applicable.**


## Generated-build audit — 17 November 2026

The successful CI artifact was downloaded and its generated `review-report.html`, `data/catalog.json`, and output tree were inspected.

- The artifact contains 27 published interactive HTML collections and 57 withheld source files.
- The current phone-like-number expression (`(?:\\+?\\d[\\s().-]?){9,14}`) is broad enough to flag ordinary numeric sequences. A match is a review signal, not proof of a phone number or personal data.
- The publishing report currently lists sensitive-scan matches before the unconditional manual-review hold for PDF/DOCX. This can mislead readers into interpreting a generic scan match as a confirmed privacy issue, even though every PDF/DOCX is withheld pending human copyright/content review.
- Keep all PDF/DOCX/TXT/Pine sources withheld for now. Do not relax the publication gate based on these findings. Before changing the detector or allowlisting anything, inspect the exact matched context in each flagged file and distinguish genuine personal data, intentional public contact information, and ordinary numeric content.
- The artifact's 27/57 counts are build facts, not evidence that all 27 pages have passed browser-level QA or that all 57 exclusions are justified by confirmed sensitive data.

Follow-up: refine the scan report so it clearly separates (1) mandatory manual content/rights review, (2) potential sensitive-data findings requiring contextual verification, and (3) duplicate/empty-source exclusions. Consider a higher-precision phone-number detector only after reviewing representative false positives and true positives.


## Interactive source checks — 17 November 2026

A generated-artifact script syntax pass checked 25 substantial inline JavaScript blocks across the published interactive apps with Node.js syntax validation.

- `Qwen_html_20260604_f25nf6z8p.html` failed: one manga entry had an unquoted author string (`Ryousuke Takeuchi & Takeshi Obata`), which stopped the entire inline script from parsing. The source entry has been corrected on this branch; the post-fix CI artifact still needs a fresh syntax pass.
- The Film & Art Library source embeds a non-empty dataset (4,942 entries across its data groups), including 98 entries in its “Essential 100” group and 835 in its “900 Curated World Cinema” group. Several labels/counts therefore need editorial reconciliation; do not infer that “0 of 0” is caused by absent data. Verify runtime initialization in a real browser.
- The Complete Film Collection source embeds 1,629 film records, while the catalogue title says 1,619 Films. Its own page heading says 1,629 unique films. This is an explicit metadata mismatch to correct after verifying whether duplicate/filtered records are intended.
- The Curator's Library embeds 1,731 records and its page header reports 1,731 entries. Its initial “Nothing found” state is a UI empty-state element; it is not evidence that the dataset is empty. Browser-level initialization and filter behaviour remain to be tested.
- The Grand Library source contains a large inline database and filter/render pipeline. Static source inspection confirms its data is embedded, but the displayed counts and startup state require browser-level testing; the header's claimed total of 8,335 must be reconciled against actual category array lengths before being treated as verified.

The syntax pass is not a browser test. It cannot validate DOM element IDs, initialization timing, event handlers, rendering correctness, iframe layout, or filtering behaviour.


## Count reconciliation — 17 November 2026

The latest generated artifact was parsed with Node.js against the embedded JavaScript data objects; these are source-data counts, not counts inferred from empty-state placeholders:

| Collection | Actual records | Previous displayed claim | Action |
|---|---:|---:|---|
| Complete Film Collection | 1,629 | 1,619 in document title and initial result counter | Corrected title and initial counter to 1,629 |
| Film & Art Library — Essential Films | 98 | 100 | Corrected section label/title/description to 98 |
| Film & Art Library — Biographical Films | 190 | 200 | Corrected title to 190 |
| Film & Art Library — World Cinema | 563 | 500 | Corrected label/title/description to 563 |
| Film & Art Library — Curated Films | 835 | 900 | Corrected label/title to 835 |
| Film & Art Library — Movie Encyclopedia | 649 | 647 | Corrected description to 649 |
| Film & Art Library — Fictional Books | 484 | 1,000 | Corrected label/title to 484 |
| Film & Art Library — Music | 266 | 500 | Corrected label/title to 266 |
| Grand Library | 8,335 | 8,335 | Verified: category arrays sum to 8,335 (3,420 films + 205 anime + 2,365 manga + 830 books + 365 music + 25 art + 100 poems + 190 thinkers + 835 prompts) |
| The Curator's Library | 1,731 | 1,731 | Verified exact array length |

The earlier note describing Big_library.html and grand_library (2).html as empty was incorrect: the GitHub file-content wrapper returned empty content for these large files, while the repository tree and generated artifact confirm substantial source files and embedded data. This has been superseded by the artifact-based inspection above.

The generated app artifact contains 26 interactive HTML apps. All 26 inline script blocks passed Node.js syntax validation after the Qwen author-string correction. This still does not prove successful runtime initialization or visual correctness in a browser. A headless Chromium smoke-test attempt did not complete within the execution window; browser-level acceptance remains open rather than being marked passed.


## CI and generated-link checks — 17 November 2026

A repository validator now runs after the site build in GitHub Actions. It extracts every non-empty inline script from generated apps and runs Node.js --check; the validator is part of the pull-request workflow so a syntax regression fails CI rather than silently publishing.

- Latest run: 44096128735 — build succeeded; generated-app script validation succeeded; artifact upload succeeded. Deployment was correctly skipped for the pull request.
- Latest generated artifact: 27 collection wrapper pages and 26 interactive app files.
- All 27 collection wrappers have a non-empty document title.
- All local iframe targets referenced by collection wrappers resolve to files in the generated artifact (0 missing targets).
- All 26 generated apps / 26 non-empty inline JavaScript blocks passed an independent Node.js syntax check.
- Headless Chromium did not complete within the available execution window in this environment. Consequently, dynamic browser initialization, actual filter interactions, visual breakpoints, console errors, and keyboard flows remain unverified. Do not treat static validation as a substitute for those checks.


## Readable-content scan correction and regenerated catalogue — 17 November 2026

The previous sensitive-data scanner searched raw HTML markup and binary PDF/DOCX streams. That caused false positives from SVG coordinates, CSS values and compressed document bytes. The scanner now:

- scans visible/searchable HTML text after removing scripts, styles, SVG and markup;
- scans extracted PDF/DOCX text (including OCR text) rather than compressed binary bytes;
- keeps every PDF and DOCX withheld for mandatory manual copyright/content review regardless of scan result;
- labels scan matches as potential indicators requiring contextual review, not confirmed sensitive data.

The regenerated artifact for run 44097584360 was inspected:
- 34 catalogue entries: 32 interactive HTML apps and 2 editorial articles.
- 34 collection wrappers; all have titles and all local iframe targets resolve.
- 32 generated apps / 32 inline JavaScript blocks pass Node.js syntax validation.
- 50 withheld items; the only withheld HTML is the byte-identical duplicate `top500_manga.html`. The other 49 are source documents/text/code held for manual review (43 PDFs, 3 DOCX, 2 TXT including the build requirements file, and 1 Pine file).
- Previously withheld HTML pages including Bob Ross, The Four Arcs, Manga Guide and related collections are now included after their false positives disappeared when scanning visible text. This does not exempt any page from editorial or browser QA.

A catalogue review found `100 Manga That Will Change How You Think` had been placed in `Other` because its source filename does not contain manga/anime keywords. It is now explicitly mapped to `Manga & Comics`.

The earlier 27 published / 57 withheld and 27-wrapper / 26-app figures describe older artifacts and are superseded by this regenerated artifact. The updated 34 / 50 figures above are the current build counts.

Browser-level runtime/visual testing remains unverified: this execution environment blocks Chromium navigation and timed out on a set-content attempt. Do not mark visual, mobile, accessibility or interaction acceptance as passed based on static checks.


## Latest regenerated artifact verification — 17 November 2026

Run 44098125417 completed successfully after the Cross-disciplinary shelf rename and manga category correction. Its uploaded artifact was independently extracted and checked:

- Catalogue: 34 entries (32 interactive HTML, 2 editorial articles).
- Category distribution: Manga & Comics 11; Cinema 6; Art 4; Cross-disciplinary 4; Interactive tools 4; Learning 3; Reading & Literature 2.
- 32 generated apps and 32 non-empty inline JavaScript blocks: all pass Node.js syntax validation.
- 34 collection wrappers: all have non-empty document titles; 0 missing local iframe targets.
- 50 withheld sources: 49 documents/text/code sources pending human review plus 1 exact duplicate HTML source. No unique HTML page is withheld by the readable-text scanner.
- The four broad cross-media library pages are grouped under Cross-disciplinary instead of the generic Other label.

This is build/artifact validation only. Browser runtime, visual regression, mobile layout, accessibility, keyboard interaction and document-by-document editorial/rights review remain outstanding.


## Homepage filter and CI integrity hardening — 17 November 2026

A catalogue review caught a second-order issue from the Cross-disciplinary category rename: the homepage still had a hard-coded `Other` filter and would not offer a Cross-disciplinary filter. The homepage now builds its subject filters from categories actually present in the generated catalogue, preserving the intended subject order and avoiding empty Family/Security filters while those shelves have no published entries.

The CI validator now checks more than JavaScript syntax:
- generated app inline JavaScript syntax;
- catalogue entry count equals collection-wrapper count;
- every category in the catalogue is represented in the homepage filter taxonomy;
- every catalogue destination exists;
- every wrapper has a document title and its iframe target exists;
- every local image, script, stylesheet, source, video and audio reference in generated apps resolves.

Latest workflow run 44098594862 passed the build, generated-site integrity validator and artifact upload. The deploy job was correctly skipped because this is a pull request.


## Responsive metadata and false-positive correction — 17 November 2026

A generated-artifact inspection found three metadata defects that the earlier syntax-only checks could not catch: `manhwa-300-filter-app.html` lacked both a document title and viewport metadata, and `typewriter.html` lacked viewport metadata. The builder now normalizes the document head first and then injects missing metadata, including for legacy files that omit a `<head>` element. The validator now checks all generated apps and collection wrappers for title, viewport metadata, duplicate IDs, and broken local references.

The first stricter run correctly failed on the legacy no-`<head>` document. The builder was fixed rather than weakening the test. The subsequent run passed.

The broad phone-like-number detector also produced false positives from SVG coordinates, year ranges, and CSS numeric values. It was replaced with more specific checks for Indian mobile-number formats and explicitly international `+` formats. This reduced unnecessary holds without removing the independent email, PAN/Aadhaar-like, credential, and token checks. Potential matches remain review indicators, not proof of personal data.

## Latest generated artifact verification — 17 November 2026

- Workflow run `44099484845` succeeded: site build, generated-app validation, and Pages artifact upload all passed.
- Generated artifact contains 32 interactive app HTML files and 34 collection wrappers (34 catalogue entries).
- All 32 apps and 34 wrappers have a non-empty document title and viewport metadata; no duplicate IDs were detected in these generated HTML documents.
- The validator checked 32 apps, 32 inline JavaScript blocks, 34 catalogue entries, 34 wrappers, and 64 local app assets. All checks passed.
- The publishing report lists 34 published HTML collections and 50 withheld sources. Withheld items include 46 PDF/DOCX documents pending manual copyright/content review, 3 text/code sources pending review, and 1 byte-identical duplicate HTML source. Empty HTML source files are excluded.
- This is stronger static/generated-output QA, but not a full interactive browser test. The local Chromium binary hangs even on a trivial data URL in this execution environment, so dynamic rendering, filters, theme switching, keyboard flows, console errors and visual mobile/desktop review remain outstanding.

## Current branch verification — 17 November 2026

- Current branch head: `e0b60d69fd0fd0820344eb75558af04a55dd3c46`.
- Workflow run [44099730334](https://github.com/piyushimself/files/actions/runs/44099730334) completed successfully on that exact head.
- Build, generated-site integrity validation and Pages artifact upload passed. The deploy job was skipped as expected for a pull request.
- The validator checks generated app/wrapper metadata, duplicate IDs, inline JavaScript syntax, catalogue-to-wrapper consistency, homepage category coverage, catalogue destinations, wrapper iframe targets and local app asset references.
- This remains static/build validation. No successful real-browser run has yet established that filters, controls, responsive rendering, keyboard interaction, accessibility or console behaviour work correctly.
- All 43 PDFs, 3 DOCX, 1 TXT and 1 Pine source remain withheld for manual content/rights/privacy review. No binary document has been promoted based only on automated text extraction.
- PR #4 remains a draft and is not merged.


## Browser screenshot review and QA hardening — 17 November 2026

Workflow run [44108196857](https://github.com/piyushimself/files/actions/runs/44108196857) completed successfully. Its Chromium report recorded 34/34 desktop collection pages, 34/34 mobile collection pages, 64 iframe loads, 19 search controls, 13 select controls, 15 filter controls, 3 tabs, 4 shell controls, 15 direct mature-app gate checks, 30 mature iframe-sync checks, 33 theme-sync checks, 32 font-sync checks, 32 text-scale checks, and zero automated issues.

The screenshot artifact was downloaded and reviewed. That visual review found a defect missed by the initial automated test: `Qwen_html_20260604_f25nf6z8p.html` has an unclosed `<style>` element because the source contains the malformed terminator `</ thead>` immediately before `<body>`. The browser therefore treated the app markup as stylesheet text and showed a blank embedded page. The original source remains unchanged.

A generated-copy-only repair was added to `tools/build.py`: when exactly one style element is unclosed and the malformed `</ thead>` occurs immediately before the body, the generated app copy receives the correct `</style>` terminator. The browser QA was also strengthened to:
- obtain the actual iframe content frame from its element handle;
- capture the embedded app body rather than silently falling back to a wrapper screenshot;
- fail on an empty embedded body/DOM; and
- fail when an app defines `#grid` but renders no cards.

The follow-up workflow on the repaired branch is the acceptance gate for this correction. Do not treat the earlier zero-issue report as final: it is superseded by this screenshot finding and the strengthened checks.

The Chromium suite is broad smoke/interaction coverage, not exhaustive testing of every bespoke control or a formal WCAG audit. Keyboard-only navigation, screen-reader behavior, detailed color-contrast measurement, and exhaustive per-control semantics still require separate review.

Document rights/content review remains separate from browser QA. All source PDFs/DOCX/TXT/Pine files remain withheld; extraction and OCR do not establish publication permission or complete human fact-checking.

## Generated-copy-only count and markup corrections — 17 November 2026

The original root-level HTML sources are preserved byte-for-byte against the main baseline. The build applies verified presentation corrections only to generated copies under site/apps/:

- Big_library.html: correct the seven section labels/descriptions to the actual embedded array counts (98, 190, 563, 835, 649, 484 and 266).
- film_collection_v8.html: correct the title and initial result counter from 1,619 to 1,629, matching its embedded 1,629 records.
- Qwen_html_20260604_f25nf6z8p.html: quote the malformed author value and close the malformed style element in the generated copy so the app script and markup parse correctly.

The Qwen, Big Library and Complete Film Collection sources are restored to their exact main blobs. Count/markup repairs do not alter the root source uploads.

## 18 November 2026 — post-merge browser regression and mobile navigation

The previous 17 November statements that real-browser validation was unavailable are superseded by the Chromium workflow evidence below.

- Pull request [#12](https://github.com/piyushimself/files/pull/12) removed duplicate Previous/Next shortcuts from the narrow-screen reader toolbar. Its PR workflow [44355644772](https://github.com/piyushimself/files/actions/runs/44355644772) completed successfully on head `8706ae97ddeef1873881c5aa63b0b5f88a39a813`. Build, generated-script validation, document extraction, Chromium QA and artifact upload all passed.
- The browser report recorded 34 catalogue items, 32 apps, 34 wrappers, 34 desktop pages, 68 mobile page checks, 96 iframe loads, 20 search controls, 14 select controls, 15 filter controls, 3 tabs, 4 shell controls, 7 direct mature-app checks, 21 mature iframe-sync checks, 33 theme-sync checks, 32 font-sync checks, 32 text-scale checks, 63 filter disclosures and **0 automated issues**.
- The QA artifact was downloaded and its report inspected. Representative mobile screenshots were visually sampled for the homepage, Manga & Comics Archive, 300 Animated Films, Cinematic Canon, Manga 1000 and Big Library. The homepage hierarchy and collection content remained readable in the sampled captures. The collection toolbar uses a horizontally scrollable touch rail; the duplicate Previous/Next shortcuts no longer consume its width. This screenshot sample is not a claim that every screenshot received individual human review.
- PR #12 was squash-merged to `main` as [`347fc95e5d5610723eef7e4bc56f5f508074d74d`](https://github.com/piyushimself/files/commit/347fc95e5d5610723eef7e4bc56f5f508074d74d).
- The preceding main-branch run [44356951764](https://github.com/piyushimself/files/actions/runs/44356951764), for document-review commit `3719ade5ba3dab09cc4e66d612dc0eff5d884d8e`, completed successfully, including deployment. The post-merge main run [44357926956](https://github.com/piyushimself/files/actions/runs/44357926956) is the acceptance run for the merged navigation fix; at the time of this update it is still in progress. Do not call the merged commit deployed until that run's deploy job succeeds.
- The automated Chromium suite is broad smoke, interaction and responsive coverage. It is not an exhaustive human visual review of every page/control, a formal WCAG audit, or screen-reader/keyboard-only certification. Those remain separate acceptance work.

## Outstanding repository-level review item

Pull request [#9](https://github.com/piyushimself/files/pull/9) was closed as superseded on 18 November. Its warm-neutral/terracotta proposal conflicted with the blue-led design contract in `DESIGN.md`, and its branch was diverged from current `main`. The historical diff remains available, but it is not a production candidate.


## Catalogue metadata defect found in current QA artifact — 19 November 2026

Review of PR #19 workflow #271 artifacts found two stale strings in the generated homepage search catalogue even though the embedded app screenshots showed the corrected runtime data:

- The Complete Film Collection catalogue card still said **1,619 Films** while the generated app correctly showed 1,629 records.
- Big Library catalogue search text retained the source placeholder **Showing 0 of 0** while the rendered app showed 98 of 4,942 in its default section.

The generated build now corrects the film collection catalogue title/search text and replaces the Big Library placeholder in search metadata. `tools/validate_site.py` asserts both conditions so the mismatch cannot silently return. Root-level uploaded HTML sources remain unchanged. The exact-head workflow after this correction must pass before accepting it; PR #19 remains unmerged until then.


A follow-up check also found that the 296-film correction was applied to the visible app and wrapper title but the homepage search index still contained the source labels “300 Essential Animated Films” and “Films: 300”. The generated search metadata is now normalized to 296 and the site validator asserts the title and search text agree. The original root-level upload is unchanged.


## Latest regression and catalogue metadata review — 19 November 2026

The exact PR #19 head before this documentation refresh passed workflow [#271](https://github.com/piyushimself/files/actions/runs/44429510208). The report records 34/34 desktop wrappers, 68 mobile page checks, 96 iframe loads, 204 mobile reader controls, 34 reader menus, 7 direct mature-app gate tests and **0 automated issues**. Wrapper screenshots for all 34 pages were visually swept in desktop/tablet/mobile contact sheets; app screenshot contact sheets were also reviewed. Individual controls, screen-reader behavior, formal contrast and keyboard-only completeness remain outside that evidence.

During artifact review, three stale homepage catalogue/search strings were found even though the rendered apps showed corrected data: Complete Film Collection still had a 1,619 catalogue title against 1,629 app records; the animated-film search text still said 300 against 296; and Big Library search text retained “Showing 0 of 0” against the rendered 98 of 4,942. The PR #19 generated build now normalizes those values and `tools/validate_site.py` asserts them. The root HTML uploads remain unchanged.

PR #20 merged as `02141201fbe55ef4a1e1306ab91adc8a3f82f1d0`; its exact-head workflow #272 passed static Pine checks and the same desktop/mobile Chromium suite. Main workflow #283 is the post-merge build/deploy gate for that commit and must be checked separately. PR #19's next exact-head workflow must be used as its merge gate after this documentation update.


## Latest main regression snapshot — 19 November 2026, 09:40 IST

Main workflow [#309](https://github.com/piyushimself/files/actions/runs/44450778850) passed build and GitHub Pages deployment for main commit `53d14aee33383421e640af3b59126ca6a2f47edb`. Browser artifact [14494544620](https://github.com/piyushimself/files/actions/runs/44450778850) reports 34 catalog items, 32 apps, 34 desktop pages, 68 mobile checks, 96 iframe loads, 204 mobile reader controls, 34 reader menus, 63 filter disclosures, 33 theme-sync, 32 font-sync, 32 text-scale and zero automated issues. The report was downloaded and inspected. This is automated regression evidence; it does not close the 11 manual acceptance items or the remaining editorial, source-document, accessibility and rights review. Run #300 was cancelled during OCR setup before build/QA and is superseded by #309.


## Follow-up main verification — 19 November 2026, 10:00 IST

- Current main: `8c279d771b1b4a59ca81a10f5a8c0aa9d3c7f40c`.
- Main workflow [#312](https://github.com/piyushimself/files/actions/runs/44456566278) completed successfully for this exact SHA. Build and Pages deploy both succeeded; generated-app checks, Pine static invariants, corrected-source-PDF validator, redacted extraction and Chromium desktop/mobile QA passed.
- Browser artifact [14498832464](https://github.com/piyushimself/files/actions/runs/44456566278) was downloaded and inspected. It reports 34 catalogue items, 32 apps, 34 desktop wrappers, 68 mobile checks, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 7 direct mature gates, 21 mature iframe-sync checks, 33 theme-sync, 32 font-sync, 32 text-scale, 63 filter disclosures, 204 mobile reader controls, 34 reader menus and zero automated issues.
- Pages artifact [14498473147](https://github.com/piyushimself/files/actions/runs/44456566278) was downloaded and inspected: 123 tar entries, 69 HTML files; no PDF, DOCX or Pine source files. Only one .txt file is present (robots.txt).
- Redacted extraction artifact [14498725745](https://github.com/piyushimself/files/actions/runs/44456566278) was inspected: 49 source artifacts processed, one exact duplicate group, zero extraction errors. This confirms extraction only; it does not establish content correctness, visual completeness or publication rights.
- No open PRs are currently reported. No additional source-document finding has been closed by this run. Independent live HTTP reachability remains unverified from this runtime.

**Status remains IN PROGRESS.** All outstanding content/count, rights, accessibility/manual acceptance and TradingView/venue validation items remain as previously listed.
