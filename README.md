# OPM Afterhours

**Discover Filipino music, one artist at a time.**

OPM Afterhours is a music discovery website dedicated to Original Pilipino Music (OPM). It features 10 Filipino artists, 30 songs, and individual artist pages where visitors can explore music, listen to tracks, and enjoy a visually immersive experience.

The website is built entirely using **HTML and CSS**, without JavaScript, frameworks, or a backend.

## About the Project

OPM Afterhours was created to showcase Filipino music while exploring what can be achieved using only HTML and CSS.

The goal is to build a simple, visually appealing, and easy-to-navigate website that celebrates Filipino artists and their music.

## Features

- **10 Featured Artists** — Explore individual pages dedicated to Filipino musicians.
- **30 Songs** — Listen to three selected tracks from each artist.
- **Music Player** — Play and pause songs using built-in browser audio controls.
- **Animated Vinyl Records** — Music-inspired visuals created with CSS.
- **Video Backgrounds** — Selected songs feature background videos.
- **Responsive Design** — Layouts designed for desktop and mobile screens.
- **Still Mode** — An option to reduce decorative motion.
- **No JavaScript Required** — The website works using HTML and CSS alone.

## Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Structures the website and its content |
| CSS3 | Handles styling, layouts, and animations |
| HTML Audio | Provides music playback controls |
| HTML Video | Displays background videos |
| Google Fonts | Provides custom typography |

No additional frameworks, databases, or JavaScript libraries are needed to run the website.

## Getting Started

You don't need advanced programming knowledge to explore this project.

### Option 1: Download the Website

1. Open this GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file to a folder on your computer.
5. Open `index.html` in your web browser.

The homepage should now appear.

**Note:** The website can run locally, but some media files may require Git LFS to be downloaded separately.

### Option 2: Using Visual Studio Code

If you want to explore or edit the source code:

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open `index.html` in your browser to preview the homepage.
5. Edit the HTML or CSS files and refresh your browser to see your changes.

You can also run a local development server if Python is installed:

```bash
python -m http.server 5500
```

Then visit:

`http://localhost:5500`

Python is optional and is not used by the website itself.

## Project Structure

```text
opm-afterhours-html-css/
│
├── index.html          # Main homepage
├── artists/            # Individual artist pages
├── assets/             # Images, music, videos, and icons
├── css/                # Website styling and animations
├── docs/               # Project documentation
├── scripts/            # Validation and packaging tools
│
└── README.md           # Project information
```

### Understanding the Folders

**`artists/`**

Contains the individual HTML pages for the featured OPM artists.

**`assets/`**

Stores the media files used throughout the website, including images, audio, videos, and icons.

**`css/`**

Contains the stylesheets responsible for the website's appearance, layouts, responsiveness, and animations.

**`docs/`**

Contains additional documentation, including the codebase guide, media inventory, and content references.

**`scripts/`**

Contains Python tools for checking and preparing the website for deployment. These are optional maintenance tools and are not needed for ordinary browsing.

## How the Website Works

The website uses standard HTML elements and CSS to provide its main features.

**Navigation:** Visitors can browse the homepage and open individual artist pages through links.

**Music Playback:** Each song uses the browser's built-in HTML audio player.

**Animations:** Vinyl rotation and other visual effects are created with CSS animations.

**Background Videos:** Selected tracks display videos using HTML video elements.

**Responsive Layouts:** CSS adjusts the website's layout to fit different screen sizes.

Because the website does not use JavaScript, some features are intentionally limited.

For example, starting a new song does not automatically pause another audio player. Users may need to pause the previous song manually.

Decorative animations are also independent of music playback.

## Preparing the Website for Deployment

This section is optional and intended for anyone who wants to publish or maintain the project.

First, make sure Python and Git LFS are installed.

Download the Git LFS media files:

```bash
git lfs pull
```

Check the website for common issues:

```bash
python scripts/validate-site.py
```

Prepare the website files:

```bash
python scripts/package-site.py
```

The packaging script creates a `dist/` folder containing the files needed to host the website.

You can upload the contents of that folder to a static hosting service.

For Netlify, drag the **`dist` folder** into [Netlify Drop](https://app.netlify.com/drop), or into the deployment drop zone of your existing Netlify project. `index.html` is directly inside the folder, alongside `artists/`, `assets/`, and `css/`. No build command is needed for this upload.

The complete package includes the original audio and video and is approximately **953 MiB**. [Netlify's upload guidance](https://docs.netlify.com/start/quickstarts/netlify-drop-quickstart/#troubleshooting-tips) says deployments under 50 MB work best and individual files over 10 MB may stall. If drag-and-drop stalls, use the Netlify CLI from the project root instead (requires Node.js and Netlify sign-in):

```bash
npx netlify-cli deploy --dir=dist --prod
```

Select your intended Netlify project when prompted. `dist/` is generated locally and excluded from Git; the source files, member photos, and packaging script are tracked so the package can be recreated.

**Important:** If `dist/` already exists, the packaging script will not overwrite it. Move or remove the existing folder before creating a new package.

## Additional Documentation

For more detailed information, check the `docs/` folder.

It contains guides covering the codebase, content sources, media inventory, and verification results.

## Project Limitations

Since this project uses only HTML and CSS:

- Music playback is controlled individually through each audio player.
- Vinyl animations do not automatically synchronize with audio.
- Some songs use static cover backgrounds instead of videos.
- Google Fonts requires an internet connection, although fallback fonts are available.
- Large media files may require Git LFS when cloning the repository.

These limitations are part of the project's HTML-and-CSS-only approach.

## Disclaimer

OPM Afterhours is an independent educational project created to showcase Filipino music and practice front-end web development.

All featured songs, artist images, and other third-party media belong to their respective copyright owners.

This project does not claim ownership of those materials. Any public deployment or redistribution of copyrighted media requires appropriate permission or licensing.

---

**Made with appreciation for Filipino music.**
