#!/usr/bin/python 
# -*- coding: UTF-8 -*-

from sys import stdout
for j in range(2,1001):
	k = []
	n = -1
	s = j
	for i in range(1,j):
		    if j % i == 0:
			    n += 1
			    s -= i
			    k.append(i)

	if s == 0:
		print (j)
		print (k)
		for i in range(n):
			stdout.write(str(k[i]))  #输出前n-1个数
			stdout.write(' ')
		#print (k)
		print (k[n]) #输出最后一个数
		#print(k)
				