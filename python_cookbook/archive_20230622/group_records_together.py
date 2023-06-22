#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Grouping Records Together Based on a Field
'''
# a list of dictionaries
from operator import itemgetter
from itertools import groupby


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'}, 
    {'address': '5148 N CLARK', 'date': '07/04/2012'}, 
    {'address': '5800 E 58TH', 'date': '07/02/2012'}, 
    {'address': '2122 N CLARK', 'date': '07/03/2012'}, 
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, 
    {'address': '1060 W ADDISON', 'date': '07/02/2012'}, 
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, 
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, 
    ]

# Sort by the desired field first
# rows.sort(key=itemgetter('date'))

# print(rows)
# Iterate in groups
# print(groupby(rows, key=itemgetter('date')))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('     ', i)

# 前提要是排序过的字典列表
