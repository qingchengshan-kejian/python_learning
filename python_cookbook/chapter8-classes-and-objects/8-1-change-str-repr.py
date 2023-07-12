class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # 0表示self
        # !r %r repr格式
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        #!s %s string格式
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print('p is {0!r}'.format(p))
print('p is {0}'.format(p))

