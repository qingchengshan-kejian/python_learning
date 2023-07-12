class A:
    def __init__(self):
        self._internal = 0 # an internal attribute
        self.public = 1

    def public_method(self):
        print('a public method')

    def _internal_method(self):
        print('a internal method')


class B:
    def __init__(self):
        self._private = 0

    def _private_method(self):
        print('B private method')

    def public_method(self):
        print('B public method')

class C(B):
    def __init__(self):
        super().__init__()
        self._private = 1 # does not override B._private
    # does not override B._private_method()
    def _private_method(self):
        print('C private method')