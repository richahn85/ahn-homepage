"""Create a clean deploy directory; exclude editorial sources, tools and Git."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT.parent/'tmp/ahn-v2-deploy'
DEST.mkdir(parents=True,exist_ok=True)
count=0
for f in ROOT.rglob('*'):
 if not f.is_file():continue
 rel=f.relative_to(ROOT)
 if any(part.startswith('.') for part in rel.parts) or rel.parts[0] in ['scripts','content']:continue
 if f.suffix.lower() not in ['.html','.css','.js','.webp','.png','.jpg','.jpeg','.svg','.pdf','.pptx','.zip','.xml','.txt','.toml','.woff2']:continue
 dest=DEST/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest);count+=1
print(f'Packaged {count} files: {DEST}')
