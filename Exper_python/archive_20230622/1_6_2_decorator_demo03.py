#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
装饰器示例：保存帮助信息。
"""

import functools

def requires_ints(decorated):
    @functools.wraps(decorated)  #使用这个函数，使得函数即使是被装饰后，扔保留原本的信息。
    def inner(*args, **kwargs):
        # Get any values that may have been sent as keyword arguments.
        kwarg_values = [i for i in kwargs.values()]

        # Iterate over every value sent to the decorated method, and
        # ensure that each one is an integer; raise TypeError if not.
        for arg in args + kwarg_values:
            if not isinstance(i, int):
                raise TypeError('%s only accepts integers as arguments.' % decorated.__name__)
        # Run the decorated method, and return the result.
        return decorated(*args, **kwargs)
    return inner

@requires_ints
def foo(x, y):
    """Return the sum of x and y."""
    return x + y

help(foo)