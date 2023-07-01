#!/usr/bin/python
# -*- encoding: utf-8 -*-

from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('passwd.txt') as f:
    lines_outer = linehistory(f)
    # print(lines.lines)
    # print(lines.history)
    for line_outer in lines_outer:
        if 'python' in line_outer:
            for lineno_outer, hline in lines_outer.history:
                print('{}:{}'.format(lineno_outer, hline), end='')
