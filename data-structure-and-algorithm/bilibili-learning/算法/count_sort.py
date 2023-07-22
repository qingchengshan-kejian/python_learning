#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :count_sort.py
# @Time      :2023/7/22 0022 16:14
# @Author    :Kexia

def count_sort(li, max_count=100):
    # count存的是0 - 100，每个数的出现次数
    count = [0 for _ in range(max_count + 1)]
    # count的下标，正好就是对应的数字
    for val in li:
        count[val] += 1
    li.clear()
    print(count)
    for ind, val in enumerate(count):
        for i in range(val): # 出现0次，就不会append这个下标，这个下标就是范围内的数字
            li.append(ind)

import random
# li = [random.randint(0, 100) for _ in range(1000)]
li = [9,9,9,8,4,5,5,4,3]
print(li)
count_sort(li)
print(li)