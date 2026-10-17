"""Download artist portraits from public Deezer and Spotify profile metadata."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import urllib.parse

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'artists'
ARTISTS = {
    'cup-of-joe': 'Cup of Joe',
    'arthur-nery': 'Arthur Nery',
    'fitterkarma': 'fitterkarma',
    'ben-and-ben': 'Ben&Ben',
    'skusta-clee': 'Skusta Clee',
    'sb19': 'SB19',
    'iv-of-spades': 'IV OF SPADES',
    'december-avenue': 'December Avenue',
    'bini': 'BINI',
    'rob-deniel': 'Rob Deniel',
}
SPOTIFY = {
    'bini': '7tNO3vJC9zlHy2IJOx34ga',
    'rob-deniel': '7dFzqx2qyelGPiBKmdSEOT',
}


def fetch(url):
    return subprocess.run(
        ['curl.exe', '--fail', '--location', '--silent', '--show-error',
         '--max-time', '30', url], check=True, capture_output=True,
    ).stdout


def portrait(item):
    slug, name = item
    if slug in SPOTIFY:
        source = 'https://open.spotify.com/artist/' + SPOTIFY[slug]
        api = 'https://open.spotify.com/oembed?' + urllib.parse.urlencode({'url': source})
        data = json.loads(fetch(api))
        if data['title'].casefold() != name.casefold():
            raise ValueError(f'Wrong Spotify artist: {name}')
        artist = {'link': source}
        image_url = data['thumbnail_url']
    else:
        api = 'https://api.deezer.com/search/artist?' + urllib.parse.urlencode(
            {'q': name, 'limit': 25})
        results = json.loads(fetch(api))['data']
        matches = [artist for artist in results if artist['name'].casefold() == name.casefold()]
        if not matches:
            raise ValueError(f'No exact artist match for {name}')
        artist = max(matches, key=lambda result: result.get('nb_fan', 0))
        image_url = artist['picture_xl']
    content = fetch(image_url)
    if not content.startswith(b'\xff\xd8'):
        raise ValueError(f'Not a JPEG portrait: {name}')
    filename = slug + '-profile.jpg'
    (OUT / filename).write_bytes(content)
    print(f'{name}: {artist["link"]} -> {filename}', flush=True)
    return {'artist': name, 'source': artist['link'], 'api': api,
            'image_url': image_url, 'file': filename,
            'retrieved_at': datetime.now(timezone.utc).isoformat()}


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        manifest = list(pool.map(portrait, ARTISTS.items()))
    (OUT / 'profile-sources.json').write_text(
        json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
