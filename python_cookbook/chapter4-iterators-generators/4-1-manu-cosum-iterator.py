#!/usr/bin/python
# -*- encoding: utf-8 -*-

# # version1
# with open('passwd.txt') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass

# # version2
# with open('passwd.txt') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')


items = [1, 2, 3]
it = iter(items)
while True:
    s = next(it, None)
    if s is None:
        break
    print(s, end='')
# 循环打印列表元素，默认是换行显示的，指定end参数为‘’,取消换行输出
