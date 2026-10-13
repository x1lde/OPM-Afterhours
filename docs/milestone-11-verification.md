# Milestone 11 verification — October 13, 2026

This report covers the enriched HTML/CSS edition in `D:\opm-afterhours-html-css`. The earlier migration report remains historical. No Git commits were made, and no original JavaScript-project files were edited.

## Environment

Python's static HTTP server served the project at localhost port 5502 without injecting scripts. External Playwright tooling controlled Chromium 155.0.8059.40. Website contexts used `javaScriptEnabled: false`. Browser evaluation inspected layout and media state only; no testing code was added to the submitted website. Screenshots were stored in the operating-system temporary directory.

Only Chromium was tested. Firefox and Microsoft Edge were not found at their usual installation paths. No cross-engine browser, screen reader, or physical phone test was performed.

## Responsive and navigation checks

- Checked all 11 pages at 320, 390, 768, 1440, and 1920 px, with a 900 px viewport height: **55 page/viewport combinations**.
- Opened every song-information panel in each combination. Document/body layout and headings, track cards, artwork/placeholders, biographies, metadata, platform links, audio, vinyl, portraits, and footer stayed within the viewport bounds. No horizontal overflow or HTTP errors were observed.
- Rechecked after adding longer verified credits. The tap-size audit found the short BINI and SB19 breadcrumb labels narrower than 44 px. Added a minimum width and confirmed both labels meet 44 × 44 px at all five widths.
- Primary platform links, summaries, navigation arrows, and adjacent-artist links meet the checked 44 px target dimensions. This is not a claim that every inline prose link is 44 px wide.
- Clicked all ten homepage artist cards, all twenty previous/next artist links, the wrapping desktop/tablet previous arrow, and the header-to-P-Pop-to-BINI genre route. All reached the intended destinations.
- Visually reviewed representative full-page screenshots of the 1440 px homepage, the 320 px Cup of Joe page, and the 768 px BINI page with expanded information. Portrait placeholders, track artwork, long credits, and platform link labels retained their intended composition.

## Keyboard, media, and accessibility checks

- Tab focused the visible skip link with a solid outline; Enter focused main content.
- Enter opened the native song-information panel. Native details/summary elements remain independently operable without scripting. Expanded information grows naturally rather than requiring nested scrolling.
- Space on the focused native Multo audio element started playback; time advanced to approximately 1.279 seconds. A second Space paused it. Loaded duration was approximately 240.164 seconds; no audio error was reported.
- Reduced-motion emulation hid the decorative video. CSS cannot guarantee that hidden video stops downloading or decoding.
- Verified both existing Multo image uses load. Real source dimensions are 1200 × 1200; HTML dimension attributes now match and CSS reserves square artwork space.
- Opened Multo's Spotify anchor in a new tab with JavaScript disabled on the local site; the popup URL matched the submitted destination. Platform playback itself was not audited.
- Reviewed semantic landmarks, one main h1 per page, descriptive image alternatives, labeled navigation, named external listening links, English page language, visible focus rules, and static current-page indicators.
- Recalculated contrast against the lightest common charcoal surface: primary text **12.84:1**, secondary text **7.59:1**, dusty-rose accent **6.30:1**. This is a calculation for those text/surface pairs, not formal WCAG certification or an audit of browser-drawn audio controls.

## HTML/CSS compliance and assets

- The W3C Nu HTML checker accepted all 11 documents with zero errors and zero warnings. Final checks were repeated after the content/metadata refinements.
- Parsed HTML attributes and elements: no script, iframe, object, embed, event-handler attributes, or executable URL schemes. No JavaScript-dependent platform player was shipped.
- Resolved **205 local link/source occurrences** to existing files or valid anchors, including the favicon. No missing images, incorrect audio paths, or broken internal anchors were found.
- All 11 titles and descriptions are unique and page-specific. Each page has a viewport meta tag, UTF-8 declaration, English language metadata, and one static current-page marker.
- Exactly one native audio player, with controls and no audio autoplay. Decorative video remains muted. The supplied Multo MP3, MP4, and JPEG matched their pre-milestone SHA-256 hashes exactly.
- CSS inspection found no executable legacy constructs or external imports. Both stylesheets loaded into the browser CSS object model. The existing `scroll-behavior` property is normal CSS, not an executable `behavior` declaration. This is not a standalone CSS-validator certification.
- Parsed the original favicon as XML and restricted its content to static svg/title/rect/circle elements, with no event attributes, links, scripts, animation, or external resources.
- Final submission inventory contains only HTML, CSS, Markdown, MP3, MP4, JPEG, and the explicitly permitted static SVG favicon. Temporary implementation helpers and their JSON baseline were removed. No packages, manifests, build tools, or executable JavaScript are included.

## Listening destination checks

- All **29 Spotify track URLs** returned public track metadata matching the selected title, performer, featured collaborator where present, and version label. All were marked playable in the research context. This is not a guarantee of availability in every region or account.
- All **26 YouTube URLs** returned successful YouTube oEmbed identity responses matching the song and official artist/label or licensed distributor Topic channel. Formats are labeled, including official audio, lyric video, and performance visualizer.
- Cross-checked the two Ben&Ben Reimagined titles separately from the original recordings. Excluded acoustic, stripped-down, live, and unrelated recordings unless explicitly labeled; none was substituted in the catalog.
- Some research-browser requests for YouTube pages returned cache/fetch errors. The independent oEmbed responses and artist/label references established the submitted destinations; full visual/audio playback of all external videos was not tested.
- Exact official YouTube uploads for maryclaire, Kalimutan Ka, and Ulap remain unresolved. Their verified Spotify destinations are provided. A falsely labeled Kalimutan Ka reupload was excluded.
- Metadata notes distinguish original release dates from subsequent album/reissue dates and video upload dates. Credits without reliable evidence remain omitted.

## Outstanding work

All ten portraits and 28 selected songs' local covers/recordings still need supplied or licensed assets if local hosting is wanted. The third Skusta Clee selection remains pending client approval; Bebe is a researched recommendation only. No new photographic or commercial media was downloaded.

Screen-reader operation, physical-phone behavior, cross-engine browser compatibility, audible recording quality, full seek/volume behavior, and every possible text-zoom/viewport-height combination remain untested. Full external-platform playback and login/subscription flows are outside the local-site checks. See the content audit and client asset checklist for precise content and media status.
