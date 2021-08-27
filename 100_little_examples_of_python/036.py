#!/usr/bin/python
# -*- coding: UTF-8 -*-
# print all the sushu between lower number and upper number 

lower=int(input("please input the lower number:"))
upper=int(input("please input the upper number:"))

for num in range(lower,upper+1):
	if num >1:
		for i in range(2,num):
			if (num%i==0):
				break
		else:
			print(num)
			