from pathlib import Path
import subprocess,urllib.parse,json,re,html,time,unicodedata
root=Path(__file__).resolve().parent.parent
output=root/'docs/platform-links.json'
results=json.loads(output.read_text(encoding='utf-8')) if output.exists() else []
def norm(s): return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
for p in sorted((root/'artists').glob('*.html')):
 for card in re.findall(r'<article class="track-card">.*?</article>',p.read_text(encoding='utf-8'),re.S):
  title=html.unescape(re.search('<h3>(.*?)</h3>',card).group(1))
  artist=html.unescape(re.search('<h1[^>]*>(.*?)</h1>',p.read_text(encoding='utf-8')).group(1))
  if any(e['page']==p.name and e['title']==title for e in results): continue
  url='https://itunes.apple.com/search?'+urllib.parse.urlencode({'term':artist+' '+title,'entity':'song','country':'ph','limit':25})
  try:
   response=subprocess.run(['curl.exe','-fLsS','--max-time','25',url],check=True,capture_output=True)
   data=json.loads(response.stdout)
   candidates=[{'title':e.get('trackName'),'artist':e.get('artistName'),'url':e.get('trackViewUrl'),'album':e.get('collectionName')} for e in data.get('results',[]) if norm(e.get('artistName',''))==norm(artist)]
   exact=[e for e in candidates if norm(e['title'])==norm(title)]
   entry={'page':p.name,'title':title,'artist':artist,'apple':exact[0] if exact else None,'candidates':candidates}
   results.append(entry)
   output.write_text(json.dumps(results,indent=2,ensure_ascii=True),encoding='utf-8')
   print(json.dumps({'title':title,'match':entry['apple'],'candidates':candidates if not exact else []}),flush=True)
  except Exception as e: print(title,str(e),flush=True)
  time.sleep(3)
