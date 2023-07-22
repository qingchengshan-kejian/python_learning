#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :topk.py
# @Time      :2023/7/22 0022 15:00
# @Author    :Kexia

# n个数，设计算法得到前k大的数
# 排序后切片 O(nlogn)
# 冒泡，k趟冒泡。或者插入排序、选择排序等。 O(kn)
# 堆排序思路 O(nlogk)
# 建小根堆
# 先取k个元素做小根堆，对剩下列表的元素循环，更新这个小根堆，最后这个小根堆就是前k大的元素
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j+1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    # 建堆
    n = len(li)
    for i in range((n - 1 -1) // 2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n - 1)
    # 取数
    for i in range(n-1, -1, -1):
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1) # i - 1是新的high
