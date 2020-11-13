#!/usr/bin/python
# -*- coding: utf-8 -*- 

from __future__ import division # 确保/不会截断

import string

text_characters = "".join(map(char, range(32, 127))) + "\n\r\t\b"
_null_trans = string.maketrans("", "")

def istext(s, text_characters = text_characters, threshold = 0.30):
	# 若s包含了空值， 它不是文本
	if "\0" in s:
		return False

    # 一个空字符串是文本
	if not s:
		return True
	# 获得s的由非文本字符构成的子串
	t = s.translate(_null_trans, text_characters)
	# 非文本字符占比30%以内，则是文本
	return len(t) / len(s) <= threshold
