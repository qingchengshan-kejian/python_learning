# class A:
#     def spam(self):
#         print('A.spam')
#
#
# class B(A):
#     def spam(self):
#         print('B.spam')
#         super().spam() # call parent spam()
#
# b = B()
# b.spam()

# class A:
#     def __init__(self):
#         self.x = 0
#
# class B:
#     def __init__(self):
#         super().__init__() # parent init
#         self.y = 1

class Proxy:
    def __init__(self, obj):
        self.obj = obj

    # delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # call original __setattr__
        else:
            setattr(self._obj, name, value)

    # 继承
    # 重载