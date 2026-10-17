"""Fetch cover art for existing Spotify track links; never fetch audio/video."""
from pathlib import Path
import urllib.parse, re, json, html, time, subprocess
def fetch(url):
    return subprocess.run(["curl.exe","--fail","--location","--silent","--show-error","--max-time","30",url],check=True,capture_output=True).stdout
ROOT=Path(__file__).resolve().parent.parent
out=ROOT/'assets'/'covers'
manifest=[]
for page in sorted((ROOT/'artists').glob('*.html')):
    source=page.read_text(encoding='utf-8')
    for card in re.findall(r'<article class="track-card">(.*?)</article>',source,re.S):
        title=html.unescape(re.search(r'<h3>(.*?)</h3>',card).group(1))
        artist=html.unescape(re.search(r'<p class="track-credit">(.*?)</p>',card).group(1))
        spotify=re.search(r'href="(https://open.spotify.com/track/[^"]+)"',card)
        if not spotify: continue
        entry={'page':page.name,'title':title,'artist':artist,'source':spotify.group(1)}
        try:
            url='https://open.spotify.com/oembed?'+urllib.parse.urlencode({'url':entry['source']})

            data=json.loads(fetch(url))
            entry['source_title']=data['title']
            entry['image_url']=data['thumbnail_url']
            # Preserve the supplied Multo artwork.
            if title=='Multo' and page.stem=='cup-of-joe':
                entry['file']='multo.jpg'
            else:
                slug=re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')
                entry['file']=page.stem+'-'+slug+'.jpg'

                content=fetch(entry['image_url'])
                if not content.startswith(b'\xff\xd8'): raise ValueError('Artwork is not JPEG')
                (out/entry['file']).write_bytes(content)
            print(json.dumps({'title':title,'source_title':entry['source_title'],'file':entry['file']},ensure_ascii=True),flush=True)
        except Exception as e:
            entry['error']=str(e)
            print(json.dumps({'title':title,'error':str(e)}),flush=True)
        manifest.append(entry)
        (out/'sources.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=True),encoding='utf-8')
        time.sleep(.3)
