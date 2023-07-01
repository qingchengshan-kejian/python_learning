symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    # 获取字符的Unicode码位
    codes.append(ord(symbol))
print(codes)

# other way to trans
codes = [ord(symbol) for symbol in symbols]
# codes = [lambda :ord(symbol) for symbol in symbols]
print((codes))

x = 'my precious'
dummy = [ x for x in 'ABC']
print(x)
print(dummy)

x = 'ABC'
dummy = [ord(x) for x in x]
print(dummy)