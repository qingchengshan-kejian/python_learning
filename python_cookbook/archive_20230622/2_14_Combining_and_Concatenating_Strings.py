#!/usr/bin/python
# -*- encoding: utf-8 -*-

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))

print(','.join(parts))

print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)

print('{} {}'.format(a, b))

print('Hello' 'World')

# Discussion
s = ''
for p in parts:
    s += p
print(s)

data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

x = 'he'
y = 'she'
z = 'it'
print(x + ':' + y + ':' + z)
print(':'.join([x, y, z]))
print(x, y, z, sep=':')
