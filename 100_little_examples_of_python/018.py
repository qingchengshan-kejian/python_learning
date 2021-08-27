#!/usr/bin/python
# -*- coding:UTF-8 -*-
import functools

Tn=0
Sn=[]
n=int (input('n='))
a=int (input('a='))
for count in range(n):
	Tn=Tn+a
	a=a*10
	Sn.append(Tn)
	print (Tn)
Sn=functools.reduce(lambda x,y:x+y,Sn)
print ("the sum is:%d"  % Sn)