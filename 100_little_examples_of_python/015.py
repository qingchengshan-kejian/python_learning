#!/usr/bin/python
# -*- coding:UTF-8-*-

score=int(raw_input('input the score:\n'))
if score >=90:
	grade='A'
elif score >=60:
	grade='B'
else:
	grade='C'

print '%d is grade %s' %(score,grade)