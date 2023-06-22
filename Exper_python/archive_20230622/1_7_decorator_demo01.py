#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
装饰类
"""

import functools
import time

def sortable_by_creation_time(cls):
    """Given a class, augment the class to have its instances be sortable
    by the timestamp at which they were instantiated.
    """
    # Augment the class original `__init__` method to also store a 
    # `_created` attribute on the instance, which corresponds to when it
    # was instantiated.
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self._created = time.time()
    cls.__init__ = new_init

    # Add `__lt__` and `__gt__` methods that return True or False based on
    # the created values in question.
    cls.__lt__ = lambda self, other: self._created < other._created
    cls.__gt__ = lambda self, other: self._created > other._created

    # Done; return the class object
    return cls

@sortable_by_creation_time
class Sortable(object):
    """docstring for Sortable"""
    def __init__(self, identifier):
        self.identifier = identifier
    def __repr__(self):
        return self.identifier


first = Sortable('1')
second = Sortable('2')
third = Sortable('3')
print(first._created)
print(second._created)
print(third._created)



sortables = [third, second, first]
print(sorted(sortables))

# 运行结果和预期不符

