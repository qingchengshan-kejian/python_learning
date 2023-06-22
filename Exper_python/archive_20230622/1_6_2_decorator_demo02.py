#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
执行时封装代码，检查函数接收参数类型都是整型。
"""

def requires_ints(decorated):
    def inner(*args, **kwargs):
        # Get any values that may have been sent as keyword arguments.
        kwargs_values = [i for i in kwargs.values()]
        # Iterate over every value sent to the decorated method, and
        # ensure that each one is an integer; raise TypeError if not.
        for arg in list(args) + kwargs_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' % decorated.__name__)
        # Run the decorated method, and return the result.
        return decorated(*args, **kwargs)
    return inner

@requires_ints
def foo(x, y):
    """Return the sum of x and y."""
    return x + y
help(foo)

print(foo(3, 5))
# 装饰后foo编程inner函数，运行时就会执行inner函数，inner函数先执行检查代码，然后再执行被装饰的函数本身

print(foo('bo', 5))