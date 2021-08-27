#!/usr/bin/python
# -*- coding:UTF-8 -*-

def inp(numbers):
	for i in range(6):
		numbers.append(int(raw_input('input a number: \n')))

p=0

def arr_max(array):
	max=0
	for i in range(1,len(array)-1):
		max=0
		p=i
		if array[p]>array[max]:max=p
	k=max
	array[0],array[k]=array[k],array[0]

def arr_min(array):
	min=0
	for i in range(1,len(array)-1):
		min=0
		p=i
		if array[p]<array[min]:min=p
	k=min
	array[5],array[k]=array[k],array[5]

def outp(numbers):
	for i in range(len(numbers)):
		print numbers[i]

if __name__=='__main__':
	array=[]
	inp(array)
	arr_max(array)
	arr_min(array)
	print 'the result is:\n'
	outp(array)

	
