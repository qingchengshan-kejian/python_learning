#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Matching Text at the Start or End of a String.
'''

import os
from urllib.request import urlopen
import re

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

filenames = os.listdir('..')
print(filenames)

list = [name for name in filenames if name.endswith(('.c', '.h'))]
print(list)
print(any(name.endswith('.py') for name in filenames))

def read_data(name):
    if name.startswith(('http', 'https', 'ftp')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices))
print(url.startswith(tuple(choices)))

# Discussion
filename = 'spam.txt'
print(filename[-4:] == '.txt')

url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp')

url = 'http://www.python.org'
re_result = re.match('http:|https:|ftp:', url)
print(re_result)
