# The Reading Room — Design Direction

## Subject and audience
A personal, cross-disciplinary library for curious readers: cinema, manga and comics, art practice, literature, learning, family reading, and security research. The experience should feel like a considered independent journal and archive, not a file dump or a generic dashboard.

## Concept
**The Reading Room is an editorial atlas.** The home page is a calm index of collections, while each source work keeps its own voice and original interaction model. Navigation is quiet and predictable; typography carries the hierarchy; metadata helps readers choose without reducing every item to a statistic. The visual language is contemporary and paper-like without using a cream-and-terracotta palette.

## Color tokens
| Token | Light | Dark | Use |
|---|---|---|---|
| Canvas | #F4F6F8 | #111820 | Main background |
| Surface | #FFFFFF | #1B2631 | Panels and tiles |
| Ink | #172B3A | #EAF0F4 | Main text |
| Muted | #586B78 | #A6B5BF | Supporting text |
| Accent | #176B68 | #70C9B8 | Links and active controls |
| Line | #D9E1E6 | #34434E | Dividers and borders |

## Type
Use system stacks only: a readable UI sans stack for navigation and body copy; a system monospace stack for code and technical metadata. No remote fonts or CDN dependencies. Body copy targets 65–72 characters per line and comfortable 1.65 line-height. Headings use restrained weight and clear size steps.

## Layout
Mobile-first single-column reading flow, expanding to a restrained two-column collection index on wide screens. The masthead remains compact. Search and filters are grouped as tools, not oversized hero elements. Article content is constrained for reading; original HTML tools run in same-origin frames with an explicit open-original link.

## Memorable move
Collection entries use a narrow vertical color rail and a short editorial description. The rail is a quiet classification cue, not a decorative card system. Focus states, selected filters, and saved items are clear without motion.

## Interaction and accessibility
- Light/dark follows system preference until the reader chooses; manual choice is remembered.
- Keyboard-visible focus, semantic landmarks, reduced-motion support, and adequate contrast in both themes.
- No autoplay, scroll-triggered animation, or hover-only information.
- Mature entries are marked clearly and require an 18+ confirmation before opening.
- Favourites and reading history are optional enhancements and must fail safely when storage is unavailable.
