#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :merge_sort.py
# @Time      :2023/7/22 0022 15:23
# @Author    :Kexia


# 实现一次归并
def merge(li, low, mid, high):
    # low是要归并的列表的首
    # high是要对并的列表的尾
    # mid是要归并的列表的两部分分界的地方，这里是规定为第一部分的尾
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:# 两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完，肯定至少有一部分没有数了
    # 左边还有数
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    # 右边还有数
    while j <= high:
        ltmp.append(li[j])
        j += 1
    # ltmp写回原列表
    li[low:high+1] = ltmp

# 假设li初始是一次归并可实现排序
li = [6, 7, 8, 9,1, 2, 3, 4, 5]
merge(li, 0, 3, 8)
print(li)


def merge_sort(li, low, high):
    mid = (low + high) // 2
    if low < high: #至少两个元素
        # 递归，归并排序左边，一直到low >= hig结束递归，层层返回
        merge_sort(li, low, mid)
        # 递归，归并排序右边，一直到low >= hig结束递归，层层返回
        merge_sort(li, mid + 1, high)
        # 对左右进行merge
        merge(li, low, mid, high)