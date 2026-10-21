"""Convert page screenshots to WebP and point <img> tags at them.
icon.png and any image used as og:image stay PNG (favicons, social previews)."""
import os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
htmls = [os.path.join(d, f) for d, _, fs in os.walk('.') if '.git' not in d for f in fs if f == 'index.html']

keep = set()
for h in htmls:
    for m in re.findall(r'og:image" content="https://projectjlab\.github\.io/([^"]+\.png)"', open(h, encoding='utf-8').read()):
        keep.add(os.path.normpath(m))
for d, _, fs in os.walk('.'):
    if 'icon.png' in fs:
        keep.add(os.path.normpath(os.path.join(d, 'icon.png')))

converted = 0
for d, _, fs in os.walk('.'):
    if '.git' in d or 'tools' in d:
        continue
    for f in fs:
        if not f.endswith('.png'):
            continue
        p = os.path.normpath(os.path.join(d, f))
        w = p[:-4] + '.webp'
        if not os.path.exists(w):
            im = Image.open(p)
            im = im.convert('RGBA') if im.mode in ('RGBA', 'LA', 'P') else im.convert('RGB')
            im.save(w, 'WEBP', quality=82, method=6)
            converted += 1
        if p not in keep:
            os.remove(p)

for h in htmls:
    s = open(h, encoding='utf-8').read()
    fix = lambda m: m.group(0) if m.group(2).endswith('icon.png') else m.group(1) + m.group(2)[:-4] + '.webp' + m.group(3)
    s2 = re.sub(r'(<img[^>]*?src=")([^"]+\.png)(")', fix, s)
    s2 = re.sub(r'(url\()([^)]+\.png)(\))', fix, s2)
    if s2 != s:
        open(h, 'w', encoding='utf-8').write(s2)
print('converted', converted, 'kept png', len(keep))
