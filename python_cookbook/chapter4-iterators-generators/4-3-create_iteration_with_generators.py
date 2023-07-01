#!/usr/bin/python
# -*- encoding: utf-8 -*-


def frange(start, stop, increment):
    '''
    这是一个简单的生成器的例子
    '''
    x = start
    while x < stop:
        yield x
        # yield 而不是 print, 就变成了x的生成器
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))