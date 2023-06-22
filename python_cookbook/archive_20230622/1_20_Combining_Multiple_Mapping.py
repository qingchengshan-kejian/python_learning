#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Combining Multiple Mappings into a Single Mapping.
'''
from collections import ChainMap
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])

'''
Discussion.
'''
print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
print(c)

# del c['y']
# key not found

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)

# Discard last mapping
values = values.parents
print(values)
# Discard last mapping
values = values.parents
print(values)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)

a['x'] = 13
print(merged['x'])

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])

a['x'] = 42
print(merged['x'])