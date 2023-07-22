#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :radix_sort.py
# @Time      :2023/7/22 0022 16:47
# @Author    :Kexia

def redix_sort(li):
    max_num = max(li) # 看最大值，决定了循环的次数，例如两位数，循环2次
    it = 0 # 循环次数
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)] # 分成10个桶
        # 分桶存放
        for var in li:
            digit = (var // (10 ** it)) % 10
            buckets[digit].append(var)
        li.clear()
        # 把数重新写回
        for buc in buckets:
            li.extend(buc)
        it += 1
