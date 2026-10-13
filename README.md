# OPM Afterhours — HTML/CSS edition

A school music discovery website featuring ten Filipino artists: read artist stories, open featured-song information, follow official listening links, and play the supplied Multo recording.

## Technology rule

The submitted site uses **HTML5 and CSS3 only**. No JavaScript, event handlers, frameworks, packages, build tools, backend services, or platform embeds are included. Content is written directly in HTML and works with JavaScript disabled. The original JavaScript project remains separate. No Git commits were made for Milestone 11.

## Project structure

```text
index.html                  Homepage, artists, genres, and About
artists/                    Ten artist pages
css/style.css               Shared design and content styles
css/responsive.css          Tablet, phone, and reduced-motion rules
assets/favicon.svg          Original static vinyl favicon
assets/artists/             Empty: portraits need authorization
assets/covers/multo.jpg      Existing supplied artwork
assets/audio/multo.mp3       Existing supplied recording
assets/videos/multo.mp4      Existing supplied decorative video
docs/content-sources.md     Research evidence and unresolved details
docs/content-audit.md       Actual completion counts
docs/client-asset-checklist.md  Per-artist asset checklist
docs/milestone-11-verification.md  Current QA results and limits
docs/verification.md         Historical migration checks
docs/html-css-explanation.md Presentation guide
```

## Open in VS Code

1. Open this folder in VS Code.
2. Install the Live Server editor extension if needed.
3. Right-click `index.html` and choose **Open with Live Server**.
4. Open an artist page and expand a song-information panel.
5. Play Multo with the browser's own audio controls.
6. Disable JavaScript in the browser and repeat these steps.

You can also open `index.html` directly. No installation or build step is needed for the website.

Live Server is an editor tool. Its normal live-reload mode can inject a development script into responses even though the submitted files contain no scripts. For a strictly script-free preview, enable **Use Browser Extension** without installing the browser extension, and refresh manually. Milestone 11 checks used Python's static HTTP server, which injects no reload code.

## Milestone 11 content

- Ten original biographies of 100–160 words, in two paragraphs.
- Expanded metadata and original 30–60-word descriptions for 29 selected songs.
- 29 direct Spotify links and 26 verified YouTube links.
- Artist-specific portrait placeholders and song-specific cover placeholders.
- Original static SVG favicon, unique page metadata, and current-page indicators.

Artist order follows [Billboard Philippines' first-half 2026 list](https://billboardphilippines.com/music/news/billboard-philippines-top-opm-artists-h1-2026/), not a final full-year ranking. The original catalog records Ralph Regis as author and July 24, 2026 as publication date. Featured songs are project selections, not chart-ranked top-three songs. Existing titles, collaborators, and genre tags were retained.

## Edit biographies and song information

Open the matching file in `artists/`. Find `<div class="biography">` and edit its two `<p>` paragraphs. Write original summaries supported by reputable sources; record source titles, URLs, access dates, and unresolved facts in `docs/content-sources.md`. Keep approved artist and track selections. Save as UTF-8. Write `&amp;` for an ampersand, as in `Ben&amp;Ben`.

Each `<article class="track-card">` contains a native `<details>` panel. Its `<summary>` opens with a click or Enter/Space. Inside `<dl class="track-metadata">`, add verified information using:

```html
<div><dt>Release</dt><dd>2024</dd></div>
```

Edit the paragraph with class `song-description` and its research link. Use a verified year when the exact date is uncertain. Omit unverified credits and do not copy lyrics. Expanded panels grow naturally; they need no scripted accordion.

## Replace a portrait placeholder

First establish the image's identity and reproduction permission. Put the authorized file in `assets/artists/`. Replace the matching placeholder on both the homepage and artist page:

```html
<img class="artist-image" src="../assets/artists/cup-of-joe.jpg"
     alt="Cup of Joe band members in an authorized group portrait"
     width="800" height="600" loading="lazy">
```

This is an editing example; that file is **not supplied**. Use `assets/artists/...` on the homepage and `../assets/artists/...` inside artist pages. Use real dimensions and accurate alt text. CSS reserves a 4:3 area and crops consistently; check that faces remain visible. Update the media inventory and required attribution.

## Add authorized cover artwork

Put the exact song/release image in `assets/covers/`, then replace only its matching placeholder:

```html
<img class="track-artwork" src="../assets/covers/approved-song.jpg"
     alt="Cover artwork for the approved song by its performing artist"
     width="600" height="600" loading="lazy">
```

Replace the example path, dimensions, and text with real details. Track artwork uses a consistent square area. Never reuse Multo's cover for another song. Retain existing authorized media unless a separate replacement is approved.

## Add an authorized MP3

Put the real recording in `assets/audio/`. Add a player only to its matching track card:

```html
<audio controls preload="metadata" aria-label="Play the approved song by its artist">
  <source src="../assets/audio/approved-song.mp3" type="audio/mpeg">
  Your browser does not support audio playback.
  <a href="../assets/audio/approved-song.mp3">Open the authorized recording</a>.
</audio>
```

Update the availability label after the file exists. The browser supplies play/pause, seeking, and available volume controls. Audio does not autoplay. Leaving the page ends playback. With multiple players, listeners must pause one before starting another; HTML/CSS cannot coordinate playback.

Only Multo has a supplied MP3, JPEG, and muted decorative MP4. These were retained byte-for-byte under the owner's inherited authorization; this milestone does not independently establish a license. No commercial recordings or publicity images were downloaded.

## Add official listening links

Verify the artist, title, and exact version using an official artist/label upload or licensed platform listing. Add a regular anchor inside the matching card's `listening-links` div:

```html
<a href="https://open.spotify.com/track/5tlb0AxuzsMWL2GtEppXGX"
   target="_blank" rel="noopener noreferrer"
   aria-label="Listen to Multo by Cup of Joe on Spotify (opens in a new tab)">
  Listen on Spotify
</a>
```

This is Multo's verified destination; use the correct verified URL for any other song. Label formats such as official audio, music video, or performance visualizer. Avoid generic search pages, fan reuploads, and unlabeled alternate versions. Record evidence and update audit counts.

Platform links open another tab. The platform's own website may require JavaScript, an account, or a subscription; OPM Afterhours remains script-free. A listening link does not grant permission to host audio or artwork locally.

## Metadata and navigation

Each page has a unique title and description, UTF-8 encoding, English language metadata, viewport settings, and a favicon. Home marks its Home link with `aria-current="page"`. Artist pages highlight the Artists parent section using `nav-active` and mark their current artist breadcrumb with `aria-current="page"`. These indicators are written statically in HTML.

## Remaining work

All ten portraits and 28 selected tracks' recordings/covers still need authorized files if local hosting is desired. Skusta Clee's confirmed songs are Since Day One (feat. Flow G) and Kalimutan Ka; slot three remains pending approval. Bebe is a documented recommendation only. Official YouTube uploads for maryclaire, Kalimutan Ka, and Ulap remain unresolved; verified Spotify links provide alternatives.

Live search, dynamic filtering, persistent favorites, uninterrupted cross-page playback, synchronized players, and synchronized lyrics require scripting and are excluded by the professor's rule. The vinyl is static. Reduced-motion CSS hides decorative video but cannot guarantee that it stops decoding or downloading.

Read the content audit, asset checklist, and current verification report to distinguish completed work from missing media and outstanding browser, screen-reader, and physical-device checks.
