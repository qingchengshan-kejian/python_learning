#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Searching and Replacing Text.
'''
import re
from calendar import month_abbr


text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text2 = 'Today is 11/26/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text2))

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

# 正则匹配的结果传入函数
print(datepat.sub(change_date, text2))

newtext, n = datepat.subn(r'\3-\1-\2', text2)
print(newtext)
print(n)

# Discussion