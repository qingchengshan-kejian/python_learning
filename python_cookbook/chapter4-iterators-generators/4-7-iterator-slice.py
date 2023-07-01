#!/usr/bin/python
# -*- encoding: utf-8 -*-
import itertools


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# 对迭代器c进行切片
for x in itertools.islice(c, 10, 20):
    print(x)



