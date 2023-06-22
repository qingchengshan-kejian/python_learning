#!/usr/bin/python

#first demo
p = (4,5)
x,y = p

print(x)
print(y)

#second demo
data = ['ACME', 50, 91.1, (2012,12,21)]
name,shares,price,date = data

print(name)
print(shares)
print(price)
print(date)

name,shares,price,(year, mon, day) = data

print(year)
print(mon)
print(day)

#error demon
p = (4, 5)
#x, y, z = p 

#other demo
s = 'Hello'
a, b, c, d, e = s
print(a,b,c,d,e)

#other demo 1
data = ['ACME', 50, 91.1, (2012,12,21)]
_, shares, price, _ = data
print(shares, price)


