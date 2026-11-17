# Codex INS & GSFA Lookup

Searchable reference for **CXG 36-1989** (Class Names and the International Numbering System for Food Additives, Rev. 2026) cross-referenced with **CXS 192-1995** (GSFA, Rev. 2026).

- 674 INS entries · 27 functional classes · 10,842 GSFA provisions · 869 notes
- Static site: no server, no tracking. Works on iOS/Android/desktop browsers once hosted.

## Layout
| Path | Purpose |
|---|---|
| `data/*.json` | Source-faithful extracted data (the single source of truth) |
| `src/template.html` | App shell (UI + search logic) |
| `scripts/build.py` | Builds `docs/index.html` (self-contained) |
| `docs/` | Published site (GitHub Pages: Settings → Pages → Deploy from branch → `main` / `/docs`) |

## Build locally
`python3 scripts/build.py` then open `docs/index.html`.

## Updating after a new Codex revision
Replace the JSON in `data/`, add a Changelog note below, commit, push. Pages redeploys automatically.

## Disclaimer
Reference only; not an official regulatory or enforcement document. Inclusion in the INS does not imply approval by Codex for use as food additives. GSFA "YES" is not a permission and "NO" is not a prohibition. For enforcement refer to the original Codex texts and the Food Regulations 1985.

**Licence:** check the FAO/WHO terms printed in the Codex publications before making this repository or site public.

Developed by Ts. Amira Zainudin © 2026
