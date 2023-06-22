#!/usr/bin/python
# -*- encoding: utf-8 -*-

def insertSort(list):
    for i in range(1,len(list)):
        j = i-1
        key = list[i]
        while j >= 0:
            if list[j] > key:
                list[j+1] = list[j]
                list[j] = key
            j -= 1
    return list
print(insertSort([1,3,2,5,9,4,11,7]))