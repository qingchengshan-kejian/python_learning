#!/usr/bin/python
# -*- encoding: utf-8 -*-

def selectSort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[j]<list[min]:
                min = j
        list[min],list[i] = list[i], list[min]
    return list

print(selectSort([3,4,6,2,1]))