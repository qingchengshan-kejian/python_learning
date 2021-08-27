#!/usr/bin/python
# -*- coding:UTF-8 -*-

TRUE=1
FALSE=0

def SQ(x):
	return x*x

print('if the num is less than 50,than quit')
again=1

while again:
	num=int(input('input a number:'))
	print('the result is : %d ' % SQ(num))
	if SQ(num)>=50:
		again=TRUE
	else:
		again=FALSE

	
