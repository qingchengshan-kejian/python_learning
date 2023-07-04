s = 'Elements are written as "<tag>text</tag>".'

import html
print(s)
print(html.escape(s))

# disable escaping of quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'

# from html.parser import HTMLParser
# p = HTMLParser()
# python3.4 以后，弃用此方法。
# print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))