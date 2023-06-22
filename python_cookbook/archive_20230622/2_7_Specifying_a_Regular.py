#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

str_pat2 = re.compile(r'\"(.*?)\"')
print(str_pat2.findall(text2))
