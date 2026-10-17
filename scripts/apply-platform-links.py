"""Apply reviewed platform destinations to static featured-song cards."""
from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parent.parent
path=root/'docs/platform-links.json'
data=json.loads(path.read_text(encoding='utf-8'))
overrides={
'Tingin':('https://music.apple.com/us/song/1693448652','Tingin','Cup of Joe & Janine'),
'Huling Sandali':('https://music.apple.com/us/song/1669550355','Huling Sandali (Tayo Sa Huling Buwan Ng Taon Official Soundtrack)','December Avenue'),
'Pag-Ibig ay Kanibalismo II':('https://music.apple.com/us/song/1834078412','Pag-Ibig ay Kanibalismo II','fitterkarma'),
'Since Day One':('https://music.apple.com/us/song/1874403321','Since Day One (feat. Flow G)','Skusta Clee'),
}
youtube={'maryclaire':'6ElJlioaXEo','Ulap':'nXOe-p94AQI','Kalimutan Ka':'eOAEpMOo-pA'}
assert len(data)==30, f'Lookup still incomplete: {len(data)}/30'
for e in data:
 if e['title'] in overrides:
  url,title,artist=overrides[e['title']]
  e['apple']={'url':url,'title':title,'artist':artist,'verification':'Apple Music page reviewed October 17, 2026'}
 assert e['apple'],f"Needs review: {e['title']}"
path.write_text(json.dumps(data,indent=2,ensure_ascii=True),encoding='utf-8')
for p in (root/'artists').glob('*.html'):
 s=p.read_text(encoding='utf-8')
 def update(m):
  card=m.group(0)
  title=html.unescape(re.search('<h3>(.*?)</h3>',card).group(1))
  e=next(e for e in data if e['page']==p.name and e['title']==title)
  links=re.search(r'<div class="listening-links">(.*?)</div>',card,re.S)
  anchors=re.findall(r'<a\b.*?</a>',links.group(1),re.S)
  spotify=next(a for a in anchors if 'open.spotify.com/' in a)
  apple=next((a for a in anchors if 'music.apple.com/' in a),None)
  if not apple:
   apple=f'<a href="{html.escape(e["apple"]["url"],quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Listen to {html.escape(title,quote=True)} on Apple Music (opens in a new tab)"><i class="bi bi-apple" aria-hidden="true"></i> Listen on Apple Music</a>'
  yt=next((a for a in anchors if 'youtube.com/' in a),None)
  if not yt:
   yt=f'<a href="https://www.youtube.com/watch?v={youtube[title]}" target="_blank" rel="noopener noreferrer" aria-label="Watch {html.escape(title,quote=True)} on YouTube (opens in a new tab)"><i class="bi bi-youtube" aria-hidden="true"></i> Watch on YouTube <span class="link-format">music video</span></a>'
  return card[:links.start()]+'<div class="listening-links">'+spotify+apple+yt+'</div>'+card[links.end():]
 s=re.sub(r'<article class="track-card">.*?</article>',update,s,flags=re.S)
 p.write_text(s,encoding='utf-8')
print('All 30 cards now have Spotify, Apple Music and YouTube in consistent order.')
