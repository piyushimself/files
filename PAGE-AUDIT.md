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
