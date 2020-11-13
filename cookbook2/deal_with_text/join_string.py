#!/usr/bin/python

pieces = ['hello', 'world', '!']
small1 = 'hello'
small2 = 'world'
small3 = '!'

large_string = ' '.join(pieces)

# method 1
print(large_string)

# method 2
large_string2 = '%s %s %s' % (small1, small2, small3)
print(large_string2)

# method 3
large_string3 = ''
for small in pieces:
	large_string3 += small

print(large_string3)

# method 4
from functools import reduce 
import operator
large_string4 = reduce(operator.add, pieces, ' ')
print('large_string4 is %s' % (large_string4))

