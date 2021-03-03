#!/usr/bin/python
# -*- encoding: utf-8 -*-


import re


comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a \n
            multiline comment */
        '''
print(comment.findall(text1))
print(comment.findall(text2))

comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment2.findall(text2))

comment3 = re.compile(r'/\*(.*?)\*', re.DOTALL)
print(comment3.findall(text2))

