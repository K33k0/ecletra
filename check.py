from html.parser import HTMLParser
from pathlib import Path
import re
p = Path('dist')
t = (p / 'index.html').read_text(encoding='utf-8')
HTMLParser().feed(t)
ids = set(re.findall(r'id="([^"]+)"', t))
assert all(x in ids for x in re.findall(r'href="#([^"]+)"', t))
assert all((p / x).exists() for x in re.findall(r'(?:src|href)="((?:assets/|style)[^"]+)"', t))
print('HTML parsed; section anchors and local assets verified.')
