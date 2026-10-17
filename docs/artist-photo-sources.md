# Artist profile photos

The homepage artist cards and artist page avatars use local profile photos in
`assets/artists/*-profile.jpg` downloaded from Deezer artist profiles, with
Spotify portraits for BINI and Rob Deniel. Each downloaded photo was visually
reviewed before use.

Exact artist pages, metadata endpoints, image URLs, and retrieval timestamps are
recorded in [profile-sources.json](../assets/artists/profile-sources.json).
The original supplied `.jfif` files are retained. Arthur Nery's homepage card and
profile avatar use the original `arthur_nery.jfif` at the user's preference;
the downloaded Deezer portrait is unused.

To refresh the downloads, run `python scripts/fetch-artist-photos.py` with network
access, then review the photos before publishing. Profile images can change on
the source services. Source attribution does not grant an image license.
