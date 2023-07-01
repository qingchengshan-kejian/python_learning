#!/usr/bin/python
# -*- encoding: utf-8 -*-

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)


for idy, val in enumerate(my_list, 1):
    print(idy, val)