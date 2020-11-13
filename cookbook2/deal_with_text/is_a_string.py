#!/usr/bin/python
'''
Summary.
Description
'''


def isAString(anobj):
	return isinstance(anobj, str)


stringobj = "hello world"
intobj = 8

print(isAString(stringobj))
print(isAString(intobj))