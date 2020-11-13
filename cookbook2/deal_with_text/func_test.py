#!/usr/bin/python
# -*- coding: utf-8 -*-  


def fun_test(m, r = 'hello'):
	print('%s %s' % (m, r))


fun_instance = fun_test('hello',r='world')

# another demo 闭包

def fun_test2(r= 'hello'):
	def fun_test3(m):
		return '%s %s' % (m, r)
	return fun_test3

# 函数实例
fun_instance2 = fun_test2(r = 'world')

# 传参、调用函数
print(fun_instance2('hello'))

# another demo

def fun_test4(r='hello'):
	print('%s %s' % (m, r))

# not right
# fun_test4('hello','ss')


