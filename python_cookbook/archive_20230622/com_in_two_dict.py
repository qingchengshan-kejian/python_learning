#!/usr/bin/python
# -*- coding: utf-8 -*-

a = {
	'x' : 1,
	'y' : 2,
	'z' : 3
}

b = {
	'w' : 10,
	'x' : 11,
	'y' : 2
}


"""
works in python3 not in python2
"""

# find keys in common
print(a.keys() & b.keys())

# find keys in a that are not in b
print(a.keys() - b.keys())

# find (key, value) pairs in common
print(a.items() & b.items())

# make a new dictionay with certain keys removed 
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)