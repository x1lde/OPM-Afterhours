"""Create a fresh deployable dist/ from validated runtime files only."""
from pathlib import Path
import runpy
import shutil

ROOT = Path(__file__).resolve().parent.parent
tools = runpy.run_path(str(ROOT / 'scripts' / 'validate-site.py'))
files = tools['validate']()
files.add(ROOT / 'assets' / 'icons' / 'LICENSE.txt')
destination = ROOT / 'dist'
if destination.exists():
    raise SystemExit('dist/ already exists. Move it aside or remove the reviewed old output before packaging again.')
destination.mkdir()
for source in sorted(files):
    target = destination / source.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
size = sum(p.stat().st_size for p in files)
print(f'Prepared {len(files)} production files in dist/ ({size / 1024**2:.1f} MiB). Upload its contents to your static host.')
