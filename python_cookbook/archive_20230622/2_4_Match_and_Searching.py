#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Matching and Searching for Text Patterns.
'''
import re


text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

# Simple matching; \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat2.match('11/27/2012')
print(m)
# Extract the contents of each group
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, yead = m.groups()

# Find all matched (notice splitting into tuples)
print(datepat2.findall(text))

for month, day, year in datepat2.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# Discussion
m = datepat2.match('11/27/2012abcdef')
print(m)
print(m.group())

datepat3 = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat3.match('11/27/2012abcdef'))
print(datepat3.match('11/27/2012'))
