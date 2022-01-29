#!/usr/bin/python
# -*- encoding: utf-8 -*-

def quicksort(list,start, r ):
    if start<r:
        q=partion(list,start,r)
        quicksort(list,start,q)
        quicksort(list,q+1,r)
def partion(list,start,r):
    i=start-1
    for j in range(start,r):
        if list[j]<=list[r]:
            i+=1
            list[i],list[j]=list[j],list[i]
    list[i+1],list[r]=list[r],list[i+1]
    return i

list=[3,2,4,1]
quicksort(list,0,3)
print(list)