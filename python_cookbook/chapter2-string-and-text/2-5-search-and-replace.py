text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re
# 捕获
# 分组
# 替换
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# 模式
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# 模式应用
print(datepat.sub(r'\3-\1-\2', text))

# 替换作用可以用函数来实现
from calendar import month_abbr
def change_date(m):
    # 函数的入参是捕获的分组
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
# n为匹配替换的次数



