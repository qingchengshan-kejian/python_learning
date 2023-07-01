#!/usr/bin/python
# -*- encoding: utf-8 -*-

from itertools import permutations
from itertools import combinations

items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)

for c in combinations(items):
    print(c)

# 排列组合，一个是忽略顺序的，一个是有顺序的。
