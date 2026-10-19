# Codebase guide

This guide explains where the website's content and behavior live. All paths are relative to the project root. The public site runs directly from HTML and CSS, with no JavaScript or build step.

## 1. Folder and file map

| File or folder | What it does | Edit it when… |
| --- | --- | --- |
| `index.html` | Homepage: hero, all ten artist cards, genre links, About, team, and listening guide | Changing homepage copy, artist order, or team credits |
| `artists/*.html` | One complete listening room per artist | Changing a biography, song, cover, media source, or platform link |
| `css/style.css` | Shared colors, typography, glass surfaces, components, and CSS interactions | Changing the overall appearance or a component |
| `css/responsive.css` | Layout changes for smaller screens, motion preferences, and accessibility fallbacks | Adjusting phone/tablet layouts |
| `css/artist-type.css` | Each artist's font, text color, capitalization, and heading size | Changing an artist's visual signature |
| `assets/logo-mark.svg` | Original moon-and-record brand symbol | Changing the brand mark |
| `assets/favicon.svg`, `favicon.ico`, `apple-touch-icon.png` | Browser tab and saved-site icons | Changing browser or device branding |
| `assets/artists/` | Ten portraits used in the directory and artist avatars | Replacing an artist photograph |
| `assets/covers/` | Featured-song artwork, including record labels and background fallbacks | Replacing a song cover |
| `assets/audio/` | Thirty supplied MP3 recordings | Adding/replacing playable audio |
| `assets/videos/` | Twenty-four supplied muted decorative MP4s | Adding/replacing a background video |
| `assets/icons/` | Local Bootstrap Icons 1.13.2 stylesheet/font and MIT license | Adding icons or updating the icon library |
| `assets/artists/profile-sources.json` | Research record of portrait sources | Tracking image provenance; never loaded by the website |
| `assets/covers/sources.json` | Research record of cover sources | Tracking artwork provenance; never loaded by the website |
| `docs/` | This guide, verification, inventory, and research records | Maintaining the project documentation |
| `scripts/validate-site.py` | Checks local links, IDs, labels, images, media, and script-free HTML | Running a pre-release sanity check |
| `scripts/package-site.py` | Copies only validated runtime files into a new `dist/` | Preparing files to upload to a static host |
| `.gitattributes` | Tells Git to store DUNGKA's video in Git LFS | Changing large-file storage rules |
| `.gitignore` | Keeps generated previews, Python caches, and `dist/` out of commits | Adding development-only output |
| `README.md` | Quick-start preview and production instructions | Changing the project entry-point instructions |

The runtime does not read JSON or Markdown. Research records stay in the source repository but are excluded from the production output. `dist/` is generated, ignored by Git, and contains only files the public site needs.

## 2. How an HTML page is arranged

Every page starts with a `head`: UTF-8 encoding, viewport, theme color, a unique page title and description, icons, fonts, and stylesheet links. The styles load in this order:

1. Local Bootstrap Icons: supplies the icon glyphs.
2. `style.css`: shared design and interactions.
3. `responsive.css`: tablet/mobile and accessibility overrides.
4. `artist-type.css`: artist-specific typography.

The body has a skip link, Still mode checkbox, header, main content, and footer. The skip link lets keyboard users go directly to `main`. The shared header uses normal links. Supported browsers highlight the section crossing a line one quarter down the viewport using CSS view timelines and `timeline-scope`. This tracks manual scrolling in both directions, including reduced-motion mode; the indicator changes state without moving. Browsers without these CSS features fall back to highlighting the clicked URL anchor. No JavaScript is used. Desktop navigation stays visible at the top; phones get a fixed bottom navigation bar and enough page padding to keep content accessible above it.

The markup is repeated in eleven files because there is no template engine. If changing the shared header or footer, make the equivalent edit in `index.html` and all ten artist files. Homepage asset paths start with `assets/`; artist-page paths start with `../assets/` because those files are one folder deeper.

## 3. Homepage sections

| Selector in `index.html` | Purpose |
| --- | --- |
| `.hero`, `.hero-copy` | Main headline, introduction, and discovery buttons |
| `.hero-record`, `.record-sleeve`, `.turntable` | Decorative glass record-player illustration, made from HTML and CSS |
| `.collection-meta`, `.collection-strip` | Artist/track counts and the small visual divider |
| `#artists`, `.artist-grid`, `.artist-tile` | All ten artists in an ordinary linked grid; no hidden carousel items |
| `.directory-source` | Source for the directory order |
| `#genres`, `.genre-grid`, `.genre-group` | Genre links; All OPM returns to the full artist directory |
| `#about`, `.about-intro` | Website description and introduction |
| `.about-pillars` | Who, What, and Why explanations |
| `.inspiration` | Vinyl, late-night listening, and visual inspiration |
| `.team-grid`, `.team-card` | Researchers, programmers, and designers with their names |
| `.listening-guide` | Native expandable help for audio, platform links, and Still mode |
| `.about-outro` | Return-to-artists call to action |

Artist order follows the recorded Billboard Philippines first-half 2026 list. The three songs per artist are project selections, not a top-three chart ranking. The About copy describes the website and the supplied team roles; it does not invent personal biographies for team members.

## 4. Artist listening rooms

Each artist page contains:

- `.breadcrumb`: a link back to the directory and the current artist.
- `.artist-room`: the rounded listening room, cover background, and muted video layers.
- `.artist-identity`: portrait and artist heading.
- `.biography`: an independently scrollable story with keyboard focus.
- `.genre-labels`: the artist's genre tags.
- `.song-picker`: labels styled as three mini vinyl records.
- `.record-region`: the selected large record, song title, and audio player.
- `.track-grid`: three track cards with official platform links and expandable information.
- `.adjacent-navigation`: visible previous/next artist links after the tracks.

### How song selection works without JavaScript

Three native radio inputs share `name="song-choice"`. Only one can be checked. The first is checked by default. Labels with `for="song-choice-1"`, `-2`, and `-3` select the corresponding input when clicked. Keyboard users can focus the group and use the arrow keys.

CSS matches the checked radio with `:has()`:

```css
.artist-room:has(#song-choice-2:checked) .selected-record-2 {
  display: block;
}
```

The same suffix connects four elements: `song-choice-2`, `.selected-record-2`, `.song-background-2`, and `.song-video-2`. Their numbers must match. Records and media default to hidden; only the selected numbered elements become visible. The selected mini record receives a rose border and tint, and keyboard focus receives an outline.

If a song has no local video, omit its video element. Its cover background remains visible. Do not add a fake source or an empty media player.

### Audio and video behavior

`audio controls` uses the browser's play, pause, seek, and volume interface. `preload="none"` asks the browser to defer loading audio until requested. Audio never autoplays. MP4s are muted, looping, inline decorative backgrounds. `aria-hidden="true"` and `tabindex="-1"` keep them out of the assistive-technology reading order.

Selecting another radio changes visibility, not playback. Pause the current audio before choosing another. The videos, audio, and vinyl rotation are independent. The site states this beside the picker. CSS cannot synchronize players, seek one medium with another, preserve playback across pages, or remember Still mode between pages.

Autoplay may cause browsers to download and decode multiple videos even with `preload="none"`. Still mode and reduced-motion CSS hide them but cannot stop their network requests or decoders. A host that supports byte-range media requests is preferable for seeking. Do not describe this site as having adaptive streaming or a synchronized music player.

## 5. CSS explained

`style.css` has nine numbered sections, with comments you can search for:

| Section | Responsibility |
| --- | --- |
| 01 Foundation | Theme variables, type scale, links, focus indicators, glass panels, buttons |
| 02 Navigation | Header, current navigation link, and Still mode switch |
| 03 Hero | Record sleeve, vinyl grooves, record label, equalizer decoration |
| 04 Collection | Artist cards, image treatment, hover states, genres |
| 05 About | Who/What/Why cards, inspiration, team, help, closing link |
| 06 Artist rooms | Background layers, biography, mini records, selected record/audio |
| 07 Tracks | Artwork, listening links, song metadata, adjacent artists |
| 08 Footer | Branding, project note, back-to-top link |
| 09 Motion | Keyframes and Still mode overrides |

### Theme variables

The main palette is in `:root`: `--background: #121113`, `--surface: #1b191d`, `--text: #f5eee9`, `--muted: #c1b6bc`, and `--accent: #e2afba`. Change these values to update the shared palette. `--glass`, `--glass-border`, and `--radius` set the glass surfaces. `--gutter` sets page side spacing.

Glass combines a translucent gradient, fine border, inset highlight, shadow, and `backdrop-filter`. `responsive.css` supplies an opaque background when blur is unsupported. Artist rooms use a dark overlay to keep text readable against moving imagery.

CSS Grid makes columns for the hero, artists, team, and tracks. `minmax(0, 1fr)` lets long text shrink instead of forcing horizontal overflow. Flexbox handles navigation, buttons, and small horizontal groups. `clamp()` scales headings smoothly between minimum and maximum sizes.

### Responsive and accessible behavior

The breakpoints are 1150px, 900px, 700px, and 360px. Desktop has five artist columns; tablets have three; phones have two. Genre, About, team, and listening-room layouts collapse as space decreases. The track cards switch to horizontal rows at tablet widths and stack their platform links on phones. Artist headings have their own small-screen rules in `artist-type.css`.

The mobile header avoids a backdrop-filter containing block so fixed bottom navigation remains attached to the viewport. Navigation has safe-area padding for devices with bottom insets. Interactive links generally provide at least a 44px target.

`prefers-reduced-motion: reduce` disables animations/transitions and visually hides videos. Still mode uses `#still-mode:checked ~ main` for a similar per-page setting. Decorative vinyl rotation and equalizer animation never indicate actual playback. Forced-colors rules preserve visible outlines. A native `details` / `summary` pair expands song notes and help without custom scripting.

## 6. Common edits

### Change an artist biography

Edit the paragraphs inside `.biography` in that artist's HTML file. Keep original prose and maintain the relevant entry in `docs/content-sources.md`. Escape an ampersand as `&amp;` in HTML.

### Change a song

Update its radio's accessible label, matching background cover, mini-record label/cover, selected record/title/audio, and its `track-card`. Keep the slot number consistent. Update all three platform destinations to the exact recording/version, the artwork alt text, song metadata, and documentation inventory.

### Add a supplied video

Put the file in `assets/videos/` and add its numbered video in `.artist-room`, before `.artist-copy`:

```html
<video class="background-video song-video-3" autoplay muted loop playsinline
       aria-hidden="true" tabindex="-1" preload="none">
  <source src="../assets/videos/your-video.mp4" type="video/mp4">
</video>
```

Use an actual file and the correct slot number. Keep the cover fallback. Then validate and check the selected song in the browser.

### Change team credits or About copy

Edit the corresponding `.team-card` list or About paragraph in `index.html`. The team names are ordinary text; they are not a separate data file.

### Add an icon

Use a Bootstrap Icons class from the locally installed 1.13.2 set:

```html
<i class="bi bi-headphones" aria-hidden="true"></i>
```

Always keep visible text or an accessible label on the surrounding control. Icons alone should not be the only way to understand an action. Preserve `assets/icons/LICENSE.txt` in deployments.

### Update assets safely

Replace only the intended image/media file or adjust every path that uses it. Maintain case-sensitive filenames, since Linux hosts treat uppercase/lowercase differently. Keep research provenance in the source JSON and Markdown. The validator discovers runtime assets from HTML and CSS, so new correctly referenced files are included automatically in the package.

## 7. Verification and deployment

Run `python scripts/validate-site.py`. It checks eleven pages, one h1 per page, duplicate IDs, label targets, local files and fragments, filename case, image alt attributes, new-tab link attributes, three audio players per artist, CSS font references, and accidentally unexpanded LFS pointers. It also rejects script elements and inline event handlers. It is a static sanity check, not a full HTML standards validator or accessibility certification.

Run `python scripts/package-site.py` to create a fresh `dist/`. This copies the referenced runtime files plus the icon license. It does not download media, delete existing output, deploy, commit, or push. Preview that output with `python -m http.server 5501 --bind 127.0.0.1 --directory dist` before uploading its contents.

DUNGKA's MP4 is managed by Git LFS. Run `git lfs pull` before packaging on a fresh clone. The actual video must be uploaded, not the small pointer text. For a host that checks out Git, configure LFS support; otherwise deploy the prepared directory. The current media files make the package relatively large; their original quality is preserved.

## 8. Research and design records

`docs/content-sources.md` preserves the original research history. Some early entries describe the state at that time; `docs/content-audit.md` and `docs/verification.md` describe the current release. `docs/platform-links.json` records platform-link research, not runtime configuration. Cover and portrait manifests serve the same evidence purpose.

Design reference review: [LNWY's Awwwards entry](https://www.awwwards.com/sites/lnwy) informed the focus on artists and music; [Perpetuum.inc's Awwwards entry](https://www.awwwards.com/sites/perpetuum-inc) provided a reference for gradients and restrained motion; [Awwwards' design collection](https://assets.awwwards.com/awards/gallery/2023/07/HOT-RIGHT-NOW-BOOK-2023.pdf) provided typography and dark-interface examples. These are visual references, not copied templates or source code. Glass surfaces, the vinyl composition, and the preserved charcoal/rose palette are adapted to this project.

[Bootstrap Icons](https://icons.getbootstrap.com/) supplies the locally hosted icons under its included MIT license. Google Fonts supplies the existing typefaces, each with system fallbacks. No new raster artwork was required.

### Motion refinements

Homepage section links use same-document fragments so native smooth scrolling does not reload the homepage. CSS view timelines reveal cards and section headings as they enter the viewport in supported browsers. Artist rooms, selected records, and opened disclosures have short entrance animations; hover-capable devices also get image zoom and card lift. Still mode and reduced-motion preferences disable decorative animations. This update was not tested, at the owner's request.
