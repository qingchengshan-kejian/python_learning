#!/usr/bin/python
# -*- encoding: utf-8 -*-
from itertools import dropwhile
from itertools import islice

with open('passwd.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')


items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)



