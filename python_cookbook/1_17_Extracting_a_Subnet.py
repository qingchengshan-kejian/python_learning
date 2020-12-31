#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Extracting a Subnet of a Dictionary.
'''

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key:value for key, value in prices.items() if value > 200}
print(p1)

# Make a dictionary of tech stocks
tech_name = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key,value in prices.items() if key in tech_name}
print(p2)

# Disscussion
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)
# 上面那种方式更清楚，也更快。

p4 = {key:prices[key] for key in prices.keys() & tech_name}
print(p4)