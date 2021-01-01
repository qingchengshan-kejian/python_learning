#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Transforming and Reducing Data at the Same Time.
'''
import os

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Determine if any .py files exists in a directory.

files = os.listdir('.') # dirname
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

'''
Discussion.
'''
s = sum((x * x for x in nums)) # Pass generator-expr as argument
s = sum(x * x for x in nums) #More elegant syntax

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
print(s)

# Original: Return 20
min_shares = min(s['shares'] for s in portfolio)

#Alternative: Return {'name':'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s:s['shares'])
print(min_shares)
