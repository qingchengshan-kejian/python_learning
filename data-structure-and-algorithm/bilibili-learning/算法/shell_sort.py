#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :shell_sort.py
# @Time      :2023/7/22 0022 16:06
# @Author    :Kexia

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2