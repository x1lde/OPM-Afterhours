# Explaining OPM Afterhours with HTML and CSS

## 1. What HTML does

HTML gives each page its meaning and content. `header` holds the wordmark and navigation; `main` contains the page's primary content; `section` groups related topics; `article` represents a track; and `footer` closes the page. Each page has one main `h1`, with `h2` section titles and `h3` card titles beneath it. Ordered lists keep artists in ranking order and preserve the three track slots.

The pages contain their content directly. They do not need a program to fetch or render the catalog. The browser can read them even when JavaScript is disabled.

## 2. What CSS does

`css/style.css` controls the visual design. Its `:root` variables store the colors and fonts used throughout the site. For example, `--accent` is the existing dusty-rose color. Changing that variable changes every element that uses it.

CSS Grid creates columns for the hero, artist room, artist directory, and featured tracks. `minmax(0, 1fr)` lets a column shrink rather than pushing the page wider than the screen. Flexbox arranges the shared header and adjacent navigation. These layouts organize content without changing its meaning.

## 3. How the pages link together

An anchor is a real link: `<a href="artists/cup-of-joe.html">Cup of Joe</a>` opens the artist page from the landing page. From inside `artists/`, `<a href="../index.html#artists">Artist directory</a>` goes up one folder and jumps to the section with `id="artists"`.

All internal paths are relative, so the folder can be moved together. External ranking attribution links go directly to the publisher. No link depends on the original project directory.

## 4. How artist navigation works

Each artist page contains links to its two neighbors. Cup of Joe's previous artist is Rob Deniel; Rob Deniel's next artist is Cup of Joe. This wraps around the fixed catalog order.

Desktop and tablet arrows are ordinary links styled with a circular border and `position: fixed`. Their accessible labels name the destination artist. Below the tracks, visible previous/next links also name the artists. Phones use these larger text links because the floating arrows are hidden at 600px and below. No swipe handling is needed. Links activate with Enter; the browser loads another document and stops the current page's audio.

## 5. How native audio works

Cup of Joe's Multo entry uses:

```html
<audio controls preload="metadata" aria-label="Play Multo by Cup of Joe">
  <source src="../assets/audio/multo.mp3" type="audio/mpeg">
  Your browser does not support audio playback.
</audio>
```

`controls` asks the browser to supply play, pause, seeking, and any available volume controls. `preload="metadata"` requests information such as duration without intentionally preloading the entire song; browsers decide how much to load. There is no `autoplay` attribute on the audio. The browser supplies keyboard operation. The appearance varies between browsers and operating systems.

Tracks without supplied audio show “Audio unavailable” and have no audio element. Multo is never reused as another recording. If future pages have multiple players, listeners must pause one before playing another; HTML/CSS cannot coordinate their playback.

## 6. How native video works

Only Cup of Joe's room includes the supplied MP4:

```html
<video class="background-video" autoplay muted loop playsinline
       aria-hidden="true" tabindex="-1" preload="none">
  <source src="../assets/videos/multo.mp4" type="video/mp4">
</video>
```

`muted` prevents its sound from being used. `loop` repeats it, and `playsinline` requests inline playback on phones. `aria-hidden` marks it as decorative. `preload="none"` is a loading hint; autoplay may still cause loading. CSS uses absolute positioning and `object-fit: cover` to crop the picture inside the room, with a dark overlay for readability. Audio remains separate. If video cannot play, the room still has a charcoal background.

Reduced-motion CSS hides decorative video. HTML/CSS cannot conditionally pause decoding or guarantee that a hidden autoplay video is never downloaded. There is no motion in the vinyl or essential interface.

## 7. How responsive design works

The viewport meta tag lets phones use their actual screen width. `responsive.css` loads after the main stylesheet so its media queries can adjust earlier rules. At 1000px and below, the artist/genre directories use two columns and tracks use a vertical list with artwork beside the text. At 600px and below, the header wraps, directories and rooms stack, tracks use one column, and visible text navigation replaces the floating arrows.

Relative widths, flexible columns, `clamp()` typography, and `aspect-ratio` allow sizes between those breakpoints. Essential content is never hidden to fit the layout. There is no overflow-hiding rule masking layout mistakes. Browser verification covers 320, 390, 768, 1440, and 1920px widths.

## 8. How the vinyl is styled

The record is a square div with `aspect-ratio: 1` and `border-radius: 50%`, making a circle. A `repeating-radial-gradient` draws thin concentric grooves. A smaller circular element holds either the supplied Multo artwork or the OPM Afterhours label. A pseudo-element draws the center hole.

The record is static. CSS cannot reliably tell whether a native audio element is playing, so the illustration does not claim to show playback state.

## 9. Why synchronized lyrics are unavailable

Synchronized lyrics need playback time to select and highlight a line. HTML and CSS cannot read that changing time from native audio. The original Multo demo lines were original presentation text, not Multo's actual lyrics; they are omitted here.

Every track instead has a native `details` song-information panel. `summary` opens and closes it with mouse or keyboard. Its focusable content region can scroll vertically if longer authorized information is added. No highlighted line pretends to follow the recording. No song lyrics have been supplied for this edition.

## 10. Why other features were removed

Live search, dynamic genre filtering, persistent favorites, track switching, custom playback/progress controls, swipe navigation, and cross-tab synchronization all depended on scripting. They are removed entirely. Artist and genre directories provide ordinary links instead. The professor's restriction is met without misleading inactive controls or complex CSS tricks.

## 11. How to add authorized media later

1. Obtain permission for the exact recording, image, video, or text. A research link does not grant permission.
2. Put the real file in `assets/audio`, `assets/videos`, `assets/covers`, or `assets/artists`.
3. In the relevant artist HTML, replace the placeholder with an `img` and useful alt text, or add an `audio` element following the example above. Replace the availability label too.
4. Reference only files that exist. Use `../assets/` from artist pages. Keep decorative video muted and apply the existing background-video class.
5. Place authorized lyrics in that track's information panel only, with an accurate label. Do not insert another song's words.
6. Test the page with JavaScript disabled and at phone width. Do not change the pending Skusta Clee title until it has been approved and verified.

These are future editing instructions. This migration includes only the three already supplied Multo media files.

## 12. A presentation students can demonstrate

Start at the landing page and explain the semantic HTML sections. Open one artist card and show its relative link. Point to the unchanged biography, genre tags, and three track slots. Demonstrate Multo with the browser's audio controls, then open a song-information panel with the keyboard. Navigate from Cup of Joe to the previous artist to demonstrate wrapping.

Resize the browser and show the Grid columns stacking, plus the visible mobile navigation. Explain the variables in `style.css`, the two breakpoints in `responsive.css`, and the circular vinyl styling. Disable JavaScript and repeat the navigation/audio demonstration. Finish by explaining why unavailable tracks have no player and why synchronized lyrics and favorites were removed.

The ranking belongs to Billboard Philippines' first-half 2026 list. Featured songs are project selections, not chart-ranked top-three tracks. Read `verification.md` to distinguish automated browser checks from checks still requiring a human.
