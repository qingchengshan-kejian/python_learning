#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
装饰器示例：函数注册表
"""

registry = []
def register(decorated):
    registry.append(decorated)
    return decorated

@register
def foo():
    return 3

@register
def bar():
    return 5

answers = []
for func in registry:
    answers.append(func())
print(answers)

class Registry(object):
    """docstring for Registry"""
    def __init__(self):
        self._functions = []

    # 在一个类中可以使用这个函数注册表装饰器收集类的方法或者就是注册一个方法
    def register(self, decorated):
        self._functions.append(decorated)
        return decorated

    def run_all(self, *args, **kwargs):
        return_values = []
        for func in self._functions:
            return_values.append(func(*args, **kwargs))
        return return_values

a = Registry()
b = Registry()

@a.register
def foo(x=3):
    return x

@b.register
def bar(x=5):
    return x

@a.register
@b.register
def baz(x=8):
    return x

print(a.run_all())
print(b.run_all())

print(a.run_all(x=6))
