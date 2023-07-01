#!/usr/bin/python
# -*- encoding: utf-8 -*-

# a = [1, 2, 3, 4]
# for x in reversed(a):
#     print(x)

# Print a file backwards
f = open('passwd.txt')
# for line in reversed(list(f)):
#     print(line)


for lineno, line in enumerate(f):
    print(lineno, line)