#!/usr/bin/python
# -*- coding:UTF-8 -*-
if __name__=='__main__':
	n=int(raw_input('the integer number n is :\n'))
	m=int(raw_input('the moved number m is :\n'))
	def move(array,n,m):
		array_end=array[n-1]
		for i in range(n-1,0,-1):
			array[i]=array[i-1]

		array[0]=array_end
		m -= 1
		if m>0:move(array,n,m)

	number=[]
	for i in range(n):
		number.append(int(raw_input('input a number:\n')))

	print 'the original list is:\n',number
	move(number,n,m)

	print 'after moving:\n',number