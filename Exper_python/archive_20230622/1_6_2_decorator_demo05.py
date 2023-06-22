#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
装饰器示例：输出格式化。
"""

import functools
import json

def json_output(decorated):
    """Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    """
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        result = decorated(*args, **kwargs)
        return json.dumps(result)
    return inner


@json_output
def do_nothing():
    return{'status': 'done'}

print(do_nothing())

class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return self._message



def json_output2(decorated):
    """Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    """
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        try:
            result = decorated(*args, **kwargs)
        except JSONOutputError as ex:
            result = {
            'status': 'error',
            'message': str(ex),
            }

        return json.dumps(result)
    return inner

@json_output2
def error():
    raise JSONOutputError('This function is erratic.')

print(error())