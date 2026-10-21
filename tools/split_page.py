"""App landing page generator (two hero cards + 3 feature screenshots).

Usage: python3 tools/split_page.py tools/apps/<slug>.py
The app file defines SLUG, PKG, CATEGORY, THEME (dict) and L (dict with 'ko' and optional 'en').
Images live in <slug>/img/ (ko) and <slug>/img/en/ (en):
  icon.png, hero1.png, hero2.png, f1.png, f2.png, f3.png
Run tools/optimize.py afterwards to convert screenshots to WebP.
"""
import os, sys, runpy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = 'https://projectjlab.github.io/'
PLAY = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3.6 1.8 13.8 12 3.6 22.2c-.4-.2-.6-.6-.6-1.1V2.9c0-.5.2-.9.6-1.1Zm11.3 11.3 2.6 2.6-11.7 6.7 9.1-9.3Zm0-2.2L5.8 1.6l11.7 6.7-2.6 2.6Zm3.9-1.6 2.8 1.6c.8.5.8 1.7 0 2.2l-2.8 1.6-2.8-2.7 2.8-2.7Z"/></svg>'

# THEME keys: hero_bg, hero_fg, hero_sub, hero_em, btn_bg, btn_fg, hero_btn_bg, hero_btn_fg,
#             accent, card, line, text, sub, kicker_css, card_mark, extra_css
CSS = '''<style>
:root{{--bg:#ffffff;--card:{card};--text:{text};--sub:{sub};--line:{line};--accent:{accent}}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--text);font-family:Pretendard,-apple-system,sans-serif;line-height:1.75;word-break:keep-all;-webkit-font-smoothing:antialiased}}
a{{color:inherit}}
.wrap{{max-width:1040px;margin:0 auto;padding:0 20px}}
.sky{{background:{hero_bg};color:{hero_fg}}}
header .wrap{{display:flex;align-items:center;justify-content:space-between;height:64px}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:700;text-decoration:none;font-size:18px}}
.brand img{{width:32px;height:32px;border-radius:9px}}
.nav{{display:flex;align-items:center;gap:14px;font-size:14px}}
.nav .lang{{text-decoration:none;opacity:.75}}
.btn{{display:inline-flex;align-items:center;gap:8px;background:{btn_bg};color:{btn_fg};text-decoration:none;font-weight:700;border-radius:999px;padding:13px 24px;font-size:15px}}
.btn.sm{{padding:8px 16px;font-size:14px}}
.sky .btn{{background:{hero_btn_bg};color:{hero_btn_fg}}}
.hero{{display:grid;grid-template-columns:1fr 1.15fr;gap:36px;align-items:center;padding:48px 20px 72px}}
.hero .icon{{width:76px;height:76px;border-radius:20px;margin-bottom:22px;box-shadow:0 8px 28px rgba(0,0,0,.12)}}
.hero h1{{font-size:clamp(34px,5.5vw,52px);font-weight:800;line-height:1.3;letter-spacing:-.01em}}
.hero h1 b{{{hero_em}}}
.hero .meaning{{font-size:13px;margin-top:8px;opacity:.8}}
.hero p{{color:{hero_sub};font-size:17px;margin:18px 0 28px}}
.hero p.notice{{font-size:12px;margin:12px 0 0;opacity:.7}}
.art2{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.art2 img{{width:100%;height:auto;border-radius:22px;box-shadow:0 10px 30px rgba(0,0,0,.12);border:1px solid rgba(0,0,0,.05)}}
.feat{{padding:80px 0}}
.feat-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.feat-item{{text-align:center}}
.feat-item .kicker{{{kicker_css}}}
.feat-item h2{{font-size:18px;font-weight:700;line-height:1.6;margin:8px 0 20px;min-height:58px}}
.feat-item img{{width:100%;max-width:300px;height:auto;border-radius:20px;box-shadow:0 6px 24px rgba(0,0,0,.08)}}
.sec{{padding:80px 0;background:var(--card)}}
.sec.plain{{background:transparent}}
.sec-title{{text-align:center;font-size:clamp(26px,4vw,34px);font-weight:800;line-height:1.4;margin-bottom:40px}}
.sec-title b{{color:var(--accent)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}}
.card{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px}}
.card h3{{font-size:18px;font-weight:700;margin-bottom:8px}}
.card h3::before{{{card_mark}}}
.card p{{color:var(--sub);font-size:15px}}
.whom ul{{list-style:none;max-width:600px;margin:0 auto;display:grid;gap:10px}}
.whom li{{background:var(--card);border-radius:14px;padding:14px 20px}}
.whom li::before{{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent);margin-right:12px;vertical-align:middle}}
.cta{{text-align:center;padding:90px 20px}}
.cta h2{{font-size:clamp(28px,5vw,42px);font-weight:800;line-height:1.35;margin-bottom:28px}}
footer{{border-top:1px solid var(--line);padding:28px 0 44px;font-size:12px;color:var(--sub)}}
footer p{{margin:4px 0}}
{extra_css}
@media (max-width:760px){{
  .hero{{grid-template-columns:1fr;text-align:center;padding:24px 16px 48px}}
  .feat-row{{grid-template-columns:1fr;gap:48px}}
  .feat-item img{{max-width:240px}}
  .wrap{{padding:0 16px}}
}}
</style>'''


def build(cfg):
    slug, pkg, theme, L = cfg['SLUG'], cfg['PKG'], cfg['THEME'], cfg['L']
    base = BASE_URL + slug + '/'
    css = CSS.format(**{'extra_css': '', **theme})
    has_en = 'en' in L
    for k, v in L.items():
        path = '' if k == 'ko' else 'en/'
        url = base + path
        im = 'img/' if k == 'ko' else '../img/en/'
        icon = 'img/icon.png' if k == 'ko' else '../img/icon.png'
        store = f"https://play.google.com/store/apps/details?id={pkg}&hl={k}"
        alt_links = ''
        lang_link = ''
        if has_en:
            alt_links = (f'<link rel="alternate" hreflang="ko" href="{base}">\n'
                         f'<link rel="alternate" hreflang="en" href="{base}en/">\n'
                         f'<link rel="alternate" hreflang="x-default" href="{base}en/">\n')
            lang_link = (f'<a class="lang" href="en/" hreflang="en">English</a>' if k == 'ko'
                         else f'<a class="lang" href="../" hreflang="ko">한국어</a>')
        # Screenshots that already carry their own headline get no duplicate caption.
        if cfg.get('SHOT_HAS_TEXT'):
            feats = ''.join(
                f'      <div class="feat-item"><img src="{im}f{n + 1}.png" alt="{kk} - {a}" loading="lazy" width="720" height="1280"></div>\n'
                for n, (kk, h, a) in enumerate(v['feats']))
        else:
            feats = ''.join(
                f'      <div class="feat-item"><div class="kicker">{kk}</div><h2>{h}</h2>'
                f'<img src="{im}f{n + 1}.png" alt="{a}" loading="lazy" width="720" height="1280"></div>\n'
                for n, (kk, h, a) in enumerate(v['feats']))
        custom = v.get('custom', '')
        cards = ''.join(f'        <article class="card"><h3>{t}</h3><p>{d}</p></article>\n' for t, d in v['cards'])
        whom = ''.join(f'        <li>{w}</li>\n' for w in v['whom'])
        notice = f'\n      <p class="notice">{v["notice"]}</p>' if v.get('notice') else ''
        og = base + ('img/' if k == 'ko' else 'img/en/') + 'hero2.png'
        html = f'''<!doctype html>
<html lang="{k}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="{theme['theme_color']}">
<title>{v['title']}</title>
<meta name="description" content="{v['desc']}">
<meta name="keywords" content="{v['kw']}">
<link rel="canonical" href="{url}">
{alt_links}<link rel="icon" href="{icon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{v['ogt']}">
<meta property="og:description" content="{v['ogd']}">
<meta property="og:image" content="{og}">
<meta property="og:url" content="{url}">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"MobileApplication","name":"{v['name']}","operatingSystem":"Android","applicationCategory":"{cfg['CATEGORY']}","inLanguage":"{k}","description":"{v['ogd']}","image":"{base}img/icon.png","installUrl":"{store}","offers":{{"@type":"Offer","price":"0","priceCurrency":"{'KRW' if k == 'ko' else 'USD'}"}},"author":{{"@type":"Organization","name":"Project J Lab"}}}}
</script>
{css}
</head>
<body>
<div class="sky">
<header>
  <div class="wrap">
    <a class="brand" href="./"><img src="{icon}" alt="">{v['brand']}</a>
    <nav class="nav">{lang_link}<a class="btn sm" href="{store}">{v['short']}</a></nav>
  </div>
</header>
  <section class="wrap hero">
    <div>
      <img class="icon" src="{icon}" alt="">
      <h1>{v['h1']}</h1>
      <div class="meaning">{v['meaning']}</div>
      <p>{v['lead']}</p>
      <a class="btn" href="{store}">{PLAY} {v['install']}</a>{notice}
    </div>
    <div class="art2"><img src="{im}hero1.png" alt="{v['heroalt']}" width="720" height="1280"><img src="{im}hero2.png" alt="" width="720" height="1280"></div>
  </section>
</div>
<main>
{custom}  <section class="feat">
    <div class="wrap feat-row">
{feats}    </div>
  </section>
  <section class="sec">
    <div class="wrap">
      <h2 class="sec-title">{v['st']}</h2>
      <div class="grid">
{cards}      </div>
    </div>
  </section>
  <section class="sec plain whom">
    <div class="wrap">
      <h2 class="sec-title">{v['st2']}</h2>
      <ul>
{whom}      </ul>
    </div>
  </section>
  <section class="cta sky">
    <h2>{v['cta']}</h2>
    <a class="btn" href="{store}">{v['install']}</a>
  </section>
</main>
<footer>
  <div class="wrap">
    {f"<p>{v['foot']}</p>" if v.get('foot') else ''}
    <p>Project J Lab · <a href="mailto:dhsthdwjd1@gmail.com">dhsthdwjd1@gmail.com</a></p>
  </div>
</footer>
</body>
</html>
'''
        out = os.path.join(ROOT, slug, path)
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(html)
    print('built', slug, list(L))


if __name__ == '__main__':
    build(runpy.run_path(sys.argv[1]))
