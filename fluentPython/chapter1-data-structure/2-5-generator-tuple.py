symbols = '$¢£¥€¤'
s = tuple(ord(symbol) for symbol in symbols)
print(s)

import array
t = array.array('I', (ord(symbol) for symbol in symbols))
print(t)