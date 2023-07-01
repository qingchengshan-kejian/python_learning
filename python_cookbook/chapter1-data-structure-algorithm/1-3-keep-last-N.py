#!/usr/bin/python
# -*- encoding: utf-8 -*-

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
    # 生成器，生成2个可迭代对象
    # 1个是line（匹配python的line）,每个元素是一行
    # 1个是previous_lines(匹配行之前的行），每个元素是1个deque,单个元素也是可迭代的



if __name__ == '__main__':
    with open('passwd.txt') as f:
        for line_this, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print("line-")
            print(line_this, end='')
            # print('-'*20)
            # print(prevlines)
