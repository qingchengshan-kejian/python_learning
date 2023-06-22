#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
装饰器参数。
同时考虑装饰器本身是个函数，当确实是装饰函数时，返回被装饰的函数。
当不作为装饰器使用，仅是一个函数时，返回普通函数。
考虑3种方式：
@json_output  #运行且装饰，函数直接传给json_output,内层装饰器的func参数接收不到
@json_output() #运行使用内层装饰，函数会传给内层装饰器的func
@json_output(indent=4) #同上，添加了额外参数
"""

import functools
import json

class JSONOutputError(Exception):
    """docstring for JSONOutputError"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def json_output(decorated_=None, indent=None, sort_keys=False):
    """Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    """
    # Did we get both a decorated method and keyword arguments?
    # That should not happen.
    if decorated_ and (indent or sort_keys):
        raise RuntimeError('Unexpected arguments')

    # Define the actual decorator function.    
    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                'status': 'erros',
                'message': str(ex),
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner

    # Return either the actual decorator, or the result of applying
    # the actual decorator, depending on what arguments we got.
    if decorated_:
        print("decorated_", decorated_)
        return actual_decorator(decorated_)
    else:
        print("not decorated_")
        return actual_decorator

# 正常装饰使用，返回的是actual_decorator
@json_output(indent=4)
def do_nothing():
    return {'status': 'done'}

print(do_nothing())


# 调用函数json_output(do_nothing函数，)
@json_output
def do_nothing2():
    return {'status': 'done'}

print(do_nothing2())