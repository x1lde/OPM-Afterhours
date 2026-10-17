from pathlib import Path
import subprocess,re,html,json
root=Path(__file__).resolve().parent.parent
url='https://music.apple.com/us/album/bebe-single/1853581405'
def fetch(url):
 return subprocess.run(['curl.exe','--fail','--location','--silent','--show-error','--max-time','30',url],check=True,capture_output=True).stdout
page=fetch(url).decode('utf-8')
match=re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]+)"',page)
if not match: raise ValueError('No Apple Music artwork found')
image=html.unescape(match.group(1))
content=fetch(image)
if not content.startswith(b'\xff\xd8'): raise ValueError('Expected JPEG artwork')
(root/'assets/covers/skusta-clee-bebe.jpg').write_bytes(content)
manifest=root/'assets/covers/sources.json'
data=json.loads(manifest.read_text(encoding='utf-8'))
data=[e for e in data if e['title']!='Bebe' or e['page']!='skusta-clee.html']
data.append({'page':'skusta-clee.html','title':'Bebe','artist':'Skusta Clee','source':url,'source_title':'Bebe - Single','image_url':image,'file':'skusta-clee-bebe.jpg'})
manifest.write_text(json.dumps(data,indent=2,ensure_ascii=True),encoding='utf-8')
print('Downloaded Bebe cover from verified Apple Music release; source recorded.')
