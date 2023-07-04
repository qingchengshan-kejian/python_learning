s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}

a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(cmb_chrs)

b = unicodedata.normalize('NFD', a)
print(b)
d = b.translate(cmb_chrs)
print(d)

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(digitmap)
x = '\u0661\u0662\u0663'

print(x.translate(digitmap))

# 按照dict映射关系对字符进行转换。

