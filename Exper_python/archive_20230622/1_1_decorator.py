#!/usr/bin/python
# -*- encoding: utf-8 -*-

'''
装饰器
'''
# 示例如下
def decorated_by(func):
    func.__doc__ += '\nDecorated by decorated_by.'
    return func

def add(x, y):
    """Return the sum of x and y."""
    return x + y
help(add)

# 直接调用装饰函数来使用
add = decorated_by(add)
help(add)
# 简单来说，装饰器就是使原来的函数多了一些额外的功能


# 也可以使用装饰器语法
@decorated_by
def add_2(x, y):
    """Return the sum of x and y."""
    return x + y

help(add_2)

"""
@also_decorated_by
@decorated_by
def add(x, y):
    '''Return the sum of x and y.'''
    return x + y
"""
"""
由内到外装饰。
"""