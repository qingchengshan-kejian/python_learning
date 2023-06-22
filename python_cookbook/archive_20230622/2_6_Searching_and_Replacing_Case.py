#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))

print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


def matchcase(word):
    # print(m.group())
    def replace(m):
        # print(m)
        # print(m.group())
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    # print(replace)
    return replace
# print(matchcase('snake'))
# 运行sub函数的时候，逐一把匹配结果传递给matchcase的内层函数,这是什么原理？
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))