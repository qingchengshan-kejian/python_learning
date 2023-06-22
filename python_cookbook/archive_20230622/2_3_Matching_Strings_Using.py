#!/usr/bin/pyhton
# -*- encoding: utf-8 -*-
'''
Matching Strings Using Shell Wildcard Patterns.
'''
from fnmatch import fnmatch, fnmatchcase


print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
name_match = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(name_match)

address = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

addr_list = [addr for addr in address if fnmatchcase(addr, '* ST')]
print(addr_list)

addr_list2 = [addr for addr in address if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(addr_list2)


# Discussion
