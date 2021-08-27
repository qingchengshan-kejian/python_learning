#!/usr/bin/python
# -*- coding:UTF-8 -*-

x=int (input("please input a number:\n"))


a=x//10000
b=x%10000//1000
c=x%1000//100
d=x%100//10
e=x%10

if a!=0:
	print ("5 bit numer:",e,d,c,b,a)
elif b!=0:
	print ("4 bit number",e,d,c,b)
elif c!=0:
	print ("3 bit number",e,d,c)
elif d!=0:
	print ("2 bit number",e,d)
else:
	print ("1 bit number",e)