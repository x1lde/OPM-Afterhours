# OPM Afterhours

A Filipino music discovery website with ten artist rooms, thirty audio tracks, and a charcoal-and-rose glass interface. Built with **HTML and CSS only**; there is no website JavaScript, framework, backend, or build dependency.

## Preview

From this folder, run:

```powershell
python -m http.server 5500 --bind 127.0.0.1
```

Open http://127.0.0.1:5500. You can also open `index.html` directly. Python is only a local preview/maintenance tool, not a website dependency.

## Where to find things

- [Codebase guide](docs/html-css-explanation.md): every folder, component, CSS section, interaction, and common edit.
- [Verification](docs/verification.md): what was checked and the remaining limitations.
- [Content and media inventory](docs/content-audit.md): all thirty songs and supplied videos.
- [Content sources](docs/content-sources.md), [cover sources](docs/cover-sources.md), and [portrait sources](docs/artist-photo-sources.md): research and attribution records.

## Production

```powershell
git lfs pull
python scripts/validate-site.py
python scripts/package-site.py
```

Upload the **contents of `dist/`** to your static host. The package contains only the eleven HTML pages, three stylesheets, referenced images/media, and local icons with their license. Documentation, Python scripts, research JSON, previews, and Git metadata stay out of the deployment.

`package-site.py` intentionally refuses to overwrite an existing `dist/`. Review and remove or move the old output before making a fresh package.

DUNGKA's video uses Git LFS. `git lfs pull` must restore the actual MP4 before packaging; the validator rejects LFS pointer files. For automated hosting, enable LFS checkout or publish this prepared directory. A plain Git checkout that contains only the pointer will not play the video.

All thirty MP3s are supplied. Twenty-four songs have local video backgrounds. Autumn (Reimagined), Kalapastangan, Mundo, and Kabisado intentionally use cover backgrounds; Step Back and Huling Sandali also use covers because no video files were supplied.

## Interaction notes

Choose an artist, select a mini record, and use the browser's audio controls. Pause one track before selecting another: CSS cannot coordinate media players. Decorative videos and vinyl rotation are independent of audio. Still mode hides video and stops CSS animation on the current page; the operating system's reduced-motion setting does the same automatically. Google Fonts needs internet; system fonts provide a fallback. Icons are served locally.

The current changes are prepared locally for review. Packaging does not deploy, commit, or push the site.
