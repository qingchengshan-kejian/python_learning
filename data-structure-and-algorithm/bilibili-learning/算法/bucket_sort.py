#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :bucket_sort.py
# @Time      :2023/7/22 0022 16:27
# @Author    :Kexia
import random


def bucket_sort(li, n=100, max_num=10000):
    # 100 buckets
    # every buket is a empty bucket
    buckets = [[] for _ in range(n)]
    for var in li:
        # which bucket?
        i = min(var // (max_num // n), n-1)
        # put into bucket
        buckets[i].append(var)
        # put into bucket and sort
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []
    for bucket in buckets:
        sorted_li.extend(bucket)
    return sorted_li

import random
li = [random.randint(0, 10) for i in range(10)]
print(li)
li = bucket_sort(li)
print(li)


