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
