# Release verification

Reviewed October 20, 2026 (Asia/Manila), using a local Python static server and desktop Chromium with responsive viewport emulation.

## Completed

- All 11 pages checked at 1440, 768, 390, and 320px viewport widths: no horizontal document overflow and one h1 per page.
- Homepage, About/team section, and SB19 listening room visually inspected; the mobile headline spacing, decorative sleeve bounds, and glow overflow were corrected during review.
- All 10 artist cards directly accessible as ordinary links. Header anchors and the About active state work.
- All 30 MP3s and 24 MP4s returned readable media metadata in Chromium. Two deferred MP3s were retried with explicit loading and passed. DUNGKA's actual 158 MB video was restored from Git LFS and decoded successfully.
- Song selection by pointer and arrow keys, native song-information disclosure, and Still mode checked in a separate browser context with JavaScript disabled.
- Still mode hides decorative video and stops CSS animation. The operating system reduced-motion setting was separately emulated and passed.
- Local Bootstrap icon font loaded successfully. All eight team names verified against the supplied spelling and roles.
- `python scripts/validate-site.py` passed: local files/fragments, case-sensitive paths, labels, unique IDs, one h1 per page, image alt attributes, three audio players per artist, safe new-tab links, CSS font references, and real media rather than Git LFS pointers.
- Unused duplicate portraits/favicon exports, obsolete CSS overrides, one-time download/migration scripts, outdated milestone/checklist reports, and browser-preview artifacts removed. Research and provenance records retained.

## Production output

`python scripts/package-site.py` validates and writes a fresh `dist/` containing only referenced runtime files and the icon license. The reviewed output has 115 files and is approximately 952.3 MiB, primarily supplied audio/video. A production-directory smoke check passed homepage navigation, team counts, song selection, artwork fallback, and local HTTP resource loading. Source documentation, research JSON, Python scripts, Git metadata, and browser artifacts are excluded. Upload the contents of this directory to a static host with MP3/MP4 MIME types and preferably byte-range support.

## Limits of this review

This is not a full accessibility certification, screen-reader audit, or physical-device test. Firefox, Safari/iOS, external platform-link availability, and the final host's caching/range behavior were not independently tested. Google Fonts remains an optional network dependency with system fallbacks.

Native HTML/CSS cannot pause a hidden audio player, coordinate audio/video timing, remember Still mode across pages, or stop video decoding merely by hiding it. The interface explains independent playback and asks listeners to pause before switching. Autoplay videos can still consume bandwidth; the original supplied media quality is retained. MP3s now request no preload until listening begins.

Six tracks use artwork backgrounds. Four are intentionally without MVs (Autumn, Kalapastangan, Mundo, Kabisado); Step Back and Huling Sandali have no supplied MP4. See `content-audit.md` for the exact inventory.

DUNGKA is stored in Git LFS. Fresh checkouts must run `git lfs pull` before packaging, or use a host checkout that retrieves LFS assets. The validator blocks deployment packaging when only a pointer is present.

Packaging does not publish the site. No commit or push is part of this UI refresh.

## Header section highlight follow-up

The original highlight followed only the URL fragment. CSS view timelines now track the visible homepage section in supported browsers, with clicked-anchor highlighting as a fallback. Desktop forward/backward scrolling and mobile reduced-motion behavior were checked in Chromium. The changed stylesheet and cache-versioned HTML pages were copied into `dist/`.

## Subsequent motion update ? untested

Added same-document homepage anchors, scroll-entry reveals, disclosure and record entrances, and hover refinements. Source and dist were updated. Browser testing and validation were explicitly skipped at the owner's request; the earlier results above predate these motion changes.
