#!/usr/bin/python
# -*- coding: utf-8 -*-

prices = {
	'ACME' : 45.23,
	'AAPL' : 612.78,
	'IBM' : 205.55,
	'HPQ' : 37.20,
	'FB' : 10.75
}

# a list of a tuple
zipPrices = zip(prices.values(), prices.keys())
print(zipPrices)

min_price = min(zip(prices.values(), prices.keys()))
print('%s %s' % ('min_price', min_price))

max_price = max(zip(prices.values(), prices.keys()))
print('%s %s' % ('max_price', max_price))

priceSorted = sorted(zip(prices.values(), prices.keys()))
print(priceSorted)

"""
zip() creates an iterator that can only be consumed once.
"""

print(min(prices))
print(max(prices))

print(min(prices.values()))
print(max(prices.values()))


print(min(prices, key = lambda k: prices[k]))
print(max(prices, key = lambda k: prices[k]))

min_value = prices[min(prices, key = lambda k: prices[k])]
print(min_value)

