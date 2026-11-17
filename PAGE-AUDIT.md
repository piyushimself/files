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

These checks are useful for triage, but they do **not** replace browser interaction testing, visual checks at desktop/mobile widths, keyboard testing, or a full semantic/content review.

## HTML source findings

| Source file | Finding / next action |
|---|---|
| `manga-1000.html` | Reviewed source CSS and class names. Legacy `.mc`, `.mt`, `.mi`, `.ma`, `.legend`, `.controls` require targeted contrast and sticky-header fixes. |
| `top500_adult_manga.html` | Reviewed source CSS and class names. Legacy `.manga-card`, `.manga-title`, `.manga-author`, `.controls` require coordinated surfaces and readable text. |
| `top500_manga.html` | Byte-identical to `top500_adult_manga.html`; keep one canonical published entry and report the duplicate rather than showing two copies. |
| `manga-comics-master.html` | Large interactive index with tabs, controls and cards; requires browser interaction and mobile layout testing. |
| `manga-index.html` | Large interactive index; needs the same visual and filter-function checks. Mature/transgressive content must remain gated and noindex. |
| `manga-guide.html` | Static reading guide; verify semantic conversion preserves all sections and sequence. |
| `manga-archive-v4.html` | Empty source file; cannot be published as a useful page. |
| `manhwa300.html` | Adult romance manhwa source; retain 18+ gate and noindex; verify filter behaviour after theme changes. |
| `manhwa_300_filter_app.html` | Missing document title; add a meaningful title after confirming its actual visible heading and purpose. |
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
- [ ] Reconcile the published catalogue against this source inventory.

**Do not mark the archive complete until all acceptance checks are either passed or explicitly recorded as not applicable.**
