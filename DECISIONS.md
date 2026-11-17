# Build Decisions

## 2026-11-17 — Baseline and safety
- Created `backup-before-build` and `site-build` from the same verified `main` commit.
- Created and verified the `pre-build` tag at that same baseline commit.
- All implementation work is confined to `site-build`; do not push to `main`.
- Preserve all source files unchanged. Generated/publication outputs belong under `/site/`.

## Content integrity
- The repository contains 35 HTML files, 43 PDFs, 3 DOCX files, 1 TXT file, 1 Pine script, and README.
- Several HTML files are large, script-driven indexes or tools. Treat source HTML as immutable and host it inside same-origin frames rather than rewriting it.
- PDF/DOCX material is not automatically publishable. A filename or apparent subject is not enough to establish copyright status or whether a document contains personal data. Require a reviewed allowlist before publishing extracted content.
- Files that trigger a sensitive-data scan or remain unreviewed must not be copied into the public site. Report only filename and issue category; never reproduce matched values.

## Architecture
- Plain HTML, CSS, and vanilla JavaScript; no framework, CDN, analytics, or external font dependency.
- A Python build script owns scanning, catalog generation, conversion, and QA.
- GitHub Actions builds and deploys GitHub Pages from the repository. The build must fail closed when dependencies or safety checks fail.
- Source documents remain at repository root; all generated web output is under `site/`.


## 2026-11-17 — Implementation and publication gate
- Static HTML pages are converted into semantic editorial reading pages with a generated contents list, estimated reading time, and in-page find/highlight controls.
- Script-driven or control-heavy HTML is copied byte-for-byte into `site/apps/` and presented in a same-origin frame; the original root files are not changed.
- Mature pages and their generated copies receive `noindex,nofollow` and an 18+ confirmation remembered in local storage.
- The build extracts PDF and DOCX text and OCRs image-only PDF pages (English and Hindi) before sensitive-data scanning. Documents remain unpublished pending human rights/content review; successful extraction does not establish publication rights.
- A conservative scan checks credentials, private keys, email addresses, phone-like numbers, selected national-ID patterns, password assignments, JWT-like tokens, and private/internal URLs. A match withholds the entire source file; false positives are possible and must be reviewed without exposing matched values.
- CI build and artifact upload succeeded. The GitHub Pages deployment action failed. Do not repeatedly retry deployment; after merging, configure repository Settings → Pages → Build and deployment → Source: GitHub Actions if it is not already enabled.
- The Pages workflow runs on both `site-build` and `main`, so merging the final PR to `main` will trigger the production build.

- 2026-11-17 publication configuration: GitHub Pages source was corrected from branch publishing (`main` root) to GitHub Actions so the generated `site/` artifact is deployed by the repository workflow.
