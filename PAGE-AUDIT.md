# Page-by-page editorial and publishing audit

Audit branch: `content-and-visual-qa`  
Base reviewed: `main` at `48bb7c7d156cdb1763c99048d68083d4e05566e8`  
Status: **in progress — not a 100% sign-off**

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
| `manga-archive-v4.html` | Empty source file; cannot be published as a useful page. |
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
| `Big_library.html` | Empty source file; cannot be published as a useful page. |
| `grand_library (2).html` | Empty source file; cannot be published as a useful page. |

## Category mapping decisions

- **Family:** children's reading guides and children's book collections are identified in the source inventory, but the underlying PDFs remain unpublished pending content, rights and sensitive-data review.
- **Reading & Literature:** fiction reading lists, poetry and literature-oriented curricula belong here. `blackout_poetry_tutorial.html`, `life-fiction-curriculum.html`, `Aag_Ki_Kavitayen.pdf` and the fictional-books list are mapped accordingly.
- **Security:** cybersecurity story material and the Pine Script/trading source files are identified, but there is no reviewed security HTML page in the current inventory. The PDFs and text/code sources remain unpublished pending review.
- **Learning:** broad personal-development curricula, courses and reflection resources belong here unless their primary purpose is clearly literature, art or another subject.
- **Art:** art tutorials, painting tasks, art resources and the Bob Ross guide belong here.
- **Cinema / Manga & Comics:** keep their specialist catalogue pages in their respective sections.

A document's filename is not proof of its contents or publication rights. No withheld PDF/DOCX/TXT/Pine source is promoted to the public catalogue solely because a category has no entries.

## Document review limitations

The 43 PDFs, 3 DOCX, 1 TXT and 1 Pine source have not yet all been inspected page by page in this pass. The GitHub text-file API cannot decode their binary contents as UTF-8; the extraction pipeline can scan/extract text during CI, but a successful scan does not establish copyright permission or human-reviewed content quality. These files remain withheld until the exact content is accessible and reviewed.

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
- [ ] Reconcile the published catalogue against this source inventory.\n- [ ] Confirm that missing-title fallback uses visible H1 text and review remaining pages with no title/H1.

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
