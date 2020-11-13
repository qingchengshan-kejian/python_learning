#!/usr/bin/python
# -*- coding: utf-8 -*-  

import string
def translator(frm = '', to = '', delete= '', keep = None):
	if len(to) == 1:
		to = to * len(frm)
	trans = string.maketrans(frm, to)
	if keep is not None:
		all_chars = string.maketrans('', '')
		delete = all_chars.translate(all_chars, keep.translate(all_chars, delete))
	def translate(s):
		return s.translate(trans, delete)
	return translate


no_digits = translator(delete = string.digits)
print(no_digits('Chris Perkins : 224-7992'))

all_chars2 = string.maketrans('', '')
print(all_chars2)