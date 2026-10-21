"""Add an app to the home list, sitemap.xml and rss.xml.

Usage: python3 tools/register.py <slug> "<앱 이름>" "<한 줄 소개>"
English pages (<slug>/en/) are added to the sitemap automatically when present."""
import os, re, sys, html, datetime, email.utils

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'https://projectjlab.github.io/'
os.chdir(ROOT)
slug, name, tagline = sys.argv[1], sys.argv[2], sys.argv[3]
today = datetime.date.today()
now = email.utils.format_datetime(datetime.datetime(today.year, today.month, today.day, 9, 0,
                                                    tzinfo=datetime.timezone(datetime.timedelta(hours=9))))

s = open('index.html', encoding='utf-8').read()
if f'href="{slug}/"' not in s:
    card = (f'    <a class="app" href="{slug}/"><img src="{slug}/img/icon.png" alt="{name} 아이콘" width="64" height="64" '
            f'loading="lazy"><div><h2>{name}</h2><p>{tagline}</p></div></a>\n')
    i = s.index('  </div>\n  <footer>')
    s = s[:i] + card + s[i:]
    s = re.sub(r'(<meta name="description" content="[^"]*?)\.">', lambda m: f'{m.group(1)}, {name}.">', s, count=1)
    open('index.html', 'w', encoding='utf-8').write(s)

m = open('sitemap.xml', encoding='utf-8').read()
for p in [f'{slug}/'] + ([f'{slug}/en/'] if os.path.exists(f'{slug}/en/index.html') else []):
    if f'<loc>{B}{p}</loc>' not in m:
        m = m.replace('</urlset>', f'  <url><loc>{B}{p}</loc><lastmod>{today}</lastmod></url>\n</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write(m)

r = open('rss.xml', encoding='utf-8').read()
if f'<link>{B}{slug}/</link>' not in r:
    p = open(f'{slug}/index.html', encoding='utf-8').read()
    t = html.unescape(re.search(r'<title>(.*?)</title>', p).group(1))
    d = html.unescape(re.search(r'<meta name="description" content="(.*?)"', p).group(1))
    item = (f'  <item>\n    <title>{html.escape(t)}</title>\n    <link>{B}{slug}/</link>\n'
            f'    <guid isPermaLink="true">{B}{slug}/</guid>\n    <description>{html.escape(d)}</description>\n'
            f'    <pubDate>{now}</pubDate>\n  </item>\n')
    r = r.replace('</channel>', item + '</channel>')
    r = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{now}</lastBuildDate>', r)
    open('rss.xml', 'w', encoding='utf-8').write(r)
print('registered', slug)
