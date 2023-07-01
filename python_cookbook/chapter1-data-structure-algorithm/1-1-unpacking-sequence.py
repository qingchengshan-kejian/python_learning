#!/usr/bin/python
# -*- encoding: utf-8 -*-

p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print(name)
print(shares)
print(price)
print(date)

name, shares, price, (year, mon, day) = data
print(year)
print(mon)
print(day)
