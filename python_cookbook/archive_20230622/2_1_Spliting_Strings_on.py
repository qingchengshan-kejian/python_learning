#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Spliting Strings on Any of Multiple Delimiters.
'''

import re
line = 'asdf fjdk; afed, fjek,asdf,    foo'
print(re.split(r'[;,\s]\s*', line))

# Discussion
# 分割后保留分割符号
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
print(values)
delimiters = fields[1::2] + ['']
print(delimiters)

joinResult = ''.join(v+d for v,d in zip(values, delimiters))
print(joinResult)

# 分割后不保留分割符号，使用?:表达式
fields_result = re.split(r'(?:,|;|\s)\s*', line)
print(fields_result)

