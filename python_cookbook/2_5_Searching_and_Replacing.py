#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Searching and Replacing Text.
'''
import re

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text2 = 'Today is 11/26/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2))