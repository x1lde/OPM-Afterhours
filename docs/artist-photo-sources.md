# Artist profile photos

The homepage cards and artist-page avatars use ten local portraits. Nine use the `*-profile.jpg` files; Arthur Nery uses the owner-selected `arthur_nery.jfif`.

The original portrait research used Deezer artist profiles, with Spotify portraits for BINI and Rob Deniel. Exact artist pages, metadata endpoints, image URLs, and retrieval timestamps remain in [profile-sources.json](../assets/artists/profile-sources.json).

Unused alternate portraits and duplicate source images were removed during production cleanup. The manifest remains a historical provenance record, so it includes some downloaded alternatives that are no longer deployed. Source attribution does not itself grant an image license.

To change a portrait, replace its file and update both the homepage card and artist-page avatar. See the [codebase guide](html-css-explanation.md) for paths and validation. The old one-time download script was removed after the supplied assets were integrated.
