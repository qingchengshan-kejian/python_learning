#!/usr/bin/python
# -*- coding:UTF-8 -*-

class Num:
	nNum=1
	def inc(self):
		self.nNum+=1
		print('nNum is %d' % self.nNum)

if __name__=='__main__':
	nNum=2
	inst=Num()
	for i in range(3):
		nNum+=1
		print('the num is %d' % nNum)
		inst.inc()

