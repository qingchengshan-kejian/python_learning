#!/usr/bin/python
# -*- coding:UTF-8 -*-

a= int (input ("please input a number:"))

x=str(a)
flag=True

for i in range (len(x)//2):
	if x[i] !=x[-i-1]:
		flag=False
		break
if flag:
	print("%d is a huiwen number." % a)
else:
	print("%d is not a huiwen number." % a)
