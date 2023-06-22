#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
1. 字符串类型
1-1. 字符串拼接，循环嵌套方式下，优先选择str.join()方法，而不是+拼接。
2. 集合类型
2-1. 列表 元组 字典 集合 （列表和字典目前是我所常用的）
"""
print("this class is about string type.")

# 列表推导
# type1 实际运行速度很慢
evens = []
for i in range(10):
	if i % 2 == 0:
		evens.append(i)
print(evens)

# type2 列表推导（表达式方式）
evens2 = [i for i in range(10) if i %2 == 0]
print(evens2)

# 枚举
# 方式1
i = 0
for element in ['one', 'two', 'three']:
	print(i, element)
	i += 1

# 方式2 
for i, element in enumerate(['one', 'two', 'three']):
	print(i, element)

# 方式3
for item in zip([1, 2, 3], [4, 5, 6]):
	print(item)

# zip再zip
for item in zip(*zip([1, 2, 3], [4, 5, 6])):
	print(item)

# 序列解包
first, second, third = 'foo', 'bar', 100
print(first)
print(second)
print(third)

# 序列解包，带星号可以进行范围匹配
first, *inner, last = 0, 1, 2, 3
print(first)
print(inner)
print(last)

# 嵌套解包
(a, b), (c, d) = (1, 2), (3, 4)
print((a, b, c, d))

