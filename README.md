# OPM Afterhours — HTML/CSS edition

A cinematic Filipino music discovery school project. This separate edition uses only HTML5 and CSS3. Open it directly or serve it through VS Code Live Server; no build step is required.

## Technology restrictions

The submitted website contains no JavaScript, inline event handlers, frameworks, package manifests, build tools, backend, or API integrations. Native HTML links, audio, video, and details panels provide the interactions. The original implementation remains separate.

## File structure

```text
index.html
artists/
  cup-of-joe.html
  arthur-nery.html
  fitterkarma.html
  ben-and-ben.html
  skusta-clee.html
  sb19.html
  iv-of-spades.html
  december-avenue.html
  bini.html
  rob-deniel.html
css/
  style.css
  responsive.css
assets/
  audio/multo.mp3
  videos/multo.mp4
  covers/multo.jpg
  artists/                 (empty; portraits not supplied)
docs/
  html-css-explanation.md
  verification.md
README.md
```

## Run the website

1. Open this folder in VS Code.
2. With the Live Server extension installed, right-click `index.html` and choose **Open with Live Server**.
3. Follow the artist links and use the browser's audio controls on Cup of Joe's page.
4. Disable JavaScript in your browser and reload to demonstrate that the pages and controls still work.

Live Server is an editor development tool, not a website dependency. Its default live-reload mode can inject a development script into served responses. The files on disk contain no such script. For a strictly script-free preview, enable Live Server's **Use Browser Extension** setting without installing the browser extension; it serves the pages without injected reload code. Refresh manually after edits. Testing used this setting with the installed Live Server engine.

## Implemented features

- Cinematic near-black/charcoal design, dusty-rose accents, Palatino-style headings and system body text.
- Landing page with hero, ranked artist directory, static genre groups, and About section.
- Ten dedicated artist pages with unchanged catalog biographies and genre metadata.
- Three featured slots per artist: 29 verified titles and one pending selection.
- Circular desktop/tablet navigation arrows and visible mobile previous/next links, wrapping at either end.
- One native audio player for the supplied Multo MP3, without audio autoplay.
- Muted decorative Multo video and cover artwork on Cup of Joe's page.
- Static CSS vinyl and native expandable song-information panels.
- Responsive Grid/Flexbox layouts, skip links, visible focus, and reduced-motion styling.

## Known limitations and removed features

Page navigation reloads the document and ends playback. Multiple future native players could play simultaneously; HTML/CSS cannot coordinate them. No search, dynamic filtering, favorites, custom playback controls, synchronized lyrics, dynamic progress display, track switching, swipe gestures, or cross-tab synchronization is included. Genre links navigate directly to artist pages.

The vinyl is static and does not represent playback state. Song-information panels replace synchronized lyrics. The original Multo demonstration text was not the song's lyrics and is omitted to avoid confusion. No song lyrics are currently presented.

Decorative video is always muted. Browser autoplay policy may prevent it from playing; the charcoal composition remains complete. Reduced-motion CSS hides the video; CSS cannot guarantee that a hidden video stops decoding or downloading.

## Media requirements and inventory

Only the supplied `multo.mp3`, `multo.mp4`, and `multo.jpg` were copied. No media was downloaded. Supplied assets are reused under the project owner's existing authorization; this migration does not independently establish licensing. Metadata sources establish titles and artist information, not media permission.

Missing media:

- 28 selected recordings have no supplied audio, cover artwork, decorative video, or authorized song lyrics.
- Skusta Clee's third slot awaits an approved and verified title, then authorized media.
- All 10 artist portraits are unavailable.
- Multo has no supplied authorized song lyrics; its original demo prose is not song lyrics.

The artist pages individually identify the unavailable tracks. No broken player or missing-file image request is rendered. Optional video and artwork need not be supplied for the site to work. An unrelated PDF in the original cover folder was not copied.

To add media later, first obtain permission, place the real file in the appropriate asset folder, and edit the relevant HTML. Use `../assets/...` from artist pages and `assets/...` from the landing page. Add audio controls only after the recording exists. Do not use Multo's files for other songs. See the student explanation for examples.

## Ranking and content attribution

Artist order is preserved from the original project's verified catalog: Cup of Joe, Arthur Nery, fitterkarma, Ben&Ben, Skusta Clee, SB19, IV OF SPADES, December Avenue, BINI, Rob Deniel.

Source: [Billboard Philippines — Top 10 Artists of 2026 (So Far)](https://billboardphilippines.com/music/news/billboard-philippines-top-opm-artists-h1-2026/). The original project records Ralph Regis as author, July 24, 2026 as publication date, and October 13, 2026 as its verification date. This is the **first-half / mid-year 2026 list**, not a final full-year ranking. These details are inherited from the inspected catalog; no new chart calculation was performed. Featured songs are project selections and are not chart-ranked top-three songs.

Biographies, spellings, featured credits, and genre tags are retained from the existing catalog. OPM describes Filipino music broadly. See `docs/verification.md` for performed checks and `docs/html-css-explanation.md` for the presentation guide.

## Remaining owner decisions

Choose and verify Skusta Clee's third track. Supply authorized recordings, portraits, covers, optional videos, and lyrics if desired. No further media integration is included in this migration.
