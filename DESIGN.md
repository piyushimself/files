# The Reading Room — Design Direction

## Subject and audience
A personal, cross-disciplinary library for curious readers: cinema, manga and comics, art practice, literature, learning, family reading, and security research. The experience should feel like a considered independent journal and archive, not a file dump or a generic dashboard.

## Concept
**The Reading Room is an editorial atlas.** The home page is a calm index of collections, while each source work keeps its own voice and original interaction model. Navigation is quiet and predictable; typography carries the hierarchy; metadata helps readers choose without reducing every item to a statistic. The visual language is contemporary and paper-like without using a cream-and-terracotta palette.

## Color tokens — Blue editorial system
| Token | Light | Dark | Use |
|---|---|---|---|
| Canvas | #E8EEF7 | #0B1627 | Whole-page background; never pure white |
| Surface | #F1F5FB | #12233A | Reading areas, cards and menus; blue-tinted, not white |
| Raised surface | #DCE6F2 | #1A304D | Inputs, selected rows and filter controls |
| Ink | #142B49 | #E4EDF8 | Main text and headings |
| Muted | #526984 | #A9BDD4 | Secondary text and metadata |
| Accent | #2868B2 | #78B5F4 | Links, selected filters and primary controls |
| Accent strong | #1D5596 | #9AC9FA | Hover and high-emphasis links |
| Line | #C6D4E5 | #2A4260 | Dividers and control borders |
| Focus | #1F70C8 | #9BC AFF | Keyboard focus indicator |

No pure-white page panels, arbitrary red/green heading colors, or unrelated accent colors. Keep semantic status colors only where color communicates a real state (for example, an error or success); never use them decoratively. Blue is the brand accent, not a reason to recolor photographs, artwork, charts or meaningful content.

## Type
Use one system sans-serif family for navigation, headings, controls and body text; reserve monospace only for code. No remote fonts or CDN dependencies. Normal body text targets 16–17px with 1.6–1.7 line-height and roughly 65–75 characters per line. Use a compact scale: page title 28–35px, section title 22–24px, subsection 18–19px, body 16–17px, metadata at least 13–14px. Avoid oversized hero headings and tiny metadata.

## Layout
Mobile-first single-column reading flow, expanding to a restrained two-column collection index on wide screens. The masthead remains compact. Search and filters are grouped as tools, not oversized hero elements. Article content is constrained for reading; original HTML tools run in same-origin frames with an explicit open-original link.

## Contextual page patterns
- Cinema and filmography: catalogue-first layouts, useful filters for genre, year, country, director or rating only when those fields exist in the source; compact result rows or poster grids when real artwork is available.
- Manga and comics: reading/discovery layouts with format, demographic, genre, status and creator filters only when grounded in the data; do not invent tags.
- Art and tutorials: visual lesson or resource layouts with clear materials, technique, difficulty and step order when available.
- Reading lists and curricula: structured reading paths, topic groupings, progress or sequence cues where the source supports them.
- Interactive tools: preserve the tool's task-specific layout and controls, but unify its typography, shell, palette, filters, forms and focus states.
- Long-form reference pages: comfortable reading column, table of contents, in-page find and well-structured tables/lists.

The shared identity is carried by color, typography, spacing, navigation and controls; page composition is chosen to fit the content rather than forcing every subject into identical cards.

## Interaction and accessibility
- Light/dark follows system preference until the reader chooses; manual choice is remembered.
- Keyboard-visible focus, semantic landmarks, reduced-motion support, and adequate contrast in both themes.
- No autoplay, scroll-triggered animation, or hover-only information.
- Mature entries are marked clearly and require an 18+ confirmation before opening.
- Favourites and reading history are optional enhancements and must fail safely when storage is unavailable.

## 2026-11-17 — Unified second-pass system
- Every generated collection page uses one shared navigation shell: home, searchable collection directory, previous/next, theme control, and text-size controls.
- Editorial pages and interactive app wrappers share the same header, navigation, spacing, footer, and design tokens.
- Embedded interactive pages keep their source functionality, but receive a local, no-CDN theme layer for the Reading Room palette, typography, controls, focus states, and dark-mode synchronization.
- Theme and text-size preferences are shared across the parent shell and same-origin embedded pages using local storage and a small postMessage bridge.
- The original root-level HTML files remain untouched; the styling layer is applied only to generated copies under site/apps/.
- Visual normalization is intentionally conservative around charts, illustrations, and app-specific components so functional meaning is not flattened.

## Research basis
- U.S. Web Design System collection guidance recommends using metadata-rich collections for grouped resources, and a separate archive/index pattern for large searchable catalogs: https://designsystem.digital.gov/components/collection/
- U.S. Web Design System typography guidance emphasizes readable type, whitespace relationships, and restrained use of bold/uppercase: https://designsystem.digital.gov/components/typography/
- The practical type and line-length targets above are our project defaults, not universal laws; validate them against actual page content and mobile rendering.

## 2026-11-17 — Blue editorial refinement
- Replace the teal/red palette with a restrained blue system in both themes.
- Use blue-tinted slate surfaces rather than pure-white panels; dark mode uses deep navy rather than black.
- Normalize all generated page titles and text to a compact, readable scale and a single sans-serif family.
- Keep page-specific layouts and meaningful status colors only where they carry semantic meaning.
- Standardize common filter chips, selected states, forms, tabs, tables, panels and buttons in preserved interactive pages without flattening meaningful charts, imagery or subject-specific visualizations.
