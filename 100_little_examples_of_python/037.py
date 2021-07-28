#!/usr/bin/python
# -*- coding:UTF-8 -*-

if __name__=="__main__":
	N=10
	# input data
	print('please input 10 number .\n')
	l=[]
	for i in range(N):
		l.append (int (input('input a number :\n')))
	print()

	for i in range(N):
		print(l[i])
	print()

	#sort the 10 number
	for i in range(N-1):
		min=i
		for j in range(i+1,N):
			if l[min]>l[j]:min=j
		l[i],l[min]=l[min],l[i]
	print('after sorting:')
	for i in range(N):
		print(l[i])