#!/usr/bin/python
# -*- coding:utf-8 -*-  

d = {
	'a' : [1, 2, 3],
	'b' : [4, 5]
}

e = {
	'a' : {1, 2, 3},
	'b' : {4, 5}
}

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)

print(e)

f = {}
f.setdefault('a', []).append(1)
f.setdefault('a', []).append(2)
f.setdefault('b', []).append(4)

print(f)