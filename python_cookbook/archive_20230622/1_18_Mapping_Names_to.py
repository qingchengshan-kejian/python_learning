#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Mapping Names to Sequence Elements.
'''

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10--19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

'''
Discussion.
'''
s = Stock('ACME', 100, 123.45)
print(s)
# s.shares = 75
# can not set attribute.
s = s._replace(shares=75)
print(s)

Stock2 = namedtuple('Stock2', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock2_prototype = Stock2('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock2(s):
    return stock2_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock2(a))
