#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
装饰器参数。
"""

import functools
import json

class JSONOutputError(Exception):
    """docstring for JSONOutputError"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def json_output(indent=None, sort_keys=False):
    """Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    """
    def actual_decorator(decorated):
        @functools.wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result = decorated(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                'status': 'erros',
                'message': str(ex),
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    return actual_decorator


@json_output(indent=4)
def do_nothing():
    return {'status': 'done'}

print(do_nothing())