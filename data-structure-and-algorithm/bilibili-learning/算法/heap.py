#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :heap.py
# @Time      :2023/7/22 0022 14:54
# @Author    :Kexia

# 堆的内置模块
import heapq
import random

# 堆的实现
# 列表到堆
li = list(range(100))
random.shuffle(li)
print(li)

heapq.heapify(li)
for i in range(len(li)):
    print(heapq.heappop(li), end=',')
