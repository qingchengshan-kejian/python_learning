#!/usr/bin/python
# -*- encoding: utf-8 -*-
import re

# Whitespace stripping
s = '    hello world   \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello======'
print(t.lstrip('-'))
print(t.strip('-='))

# Discussion here.
s1 = '    hello        world    \n'
print(s1.strip())

print(s1.replace(' ', ''))
print(re.sub('\s+', ' ', s1))
