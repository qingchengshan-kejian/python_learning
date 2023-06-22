#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
装饰器示例：用户验证。
"""

import functools

class User(object):
    """A representation of a use in our application"""
    def __init__(self, username, email):
        self.username = username
        self.email = email


class AnonymousUser(object):
    """An anonymous user; a stand-in for an actual user that nonetheless 
    is not an actual user.
    """
    def __init__(self):
        self.username = None
        self.email = None

    def __nonezero__(self):
        return False

        
def requires_user(func):
    @functools.wraps(func)
    def inner(user, *args, **kwargs):
        """Verify that the user is truthy; if so, run the decorated method,
        and if not, raise ValueError.
        """
        # Ensure that user is tryth, and of the correct type.
        # The "truthy" check will fail on anonymous users, since the
        # AnonymousUser subclass has a `__nonezero__`method that
        # returns False
        if user and isinstance(user, User):
            return func(user, *args, **kwargs)
        else:
            raise ValueError('A valid user is required to run this.')

    return inner
