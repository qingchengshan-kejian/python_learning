def spam(a, b, c, d):
    print(a, b, c, d)

from functools import partial

s1 = partial(spam, 1) # a = 1
s1(2, 3, 4)

s2 = partial(spam, d = 2) # d = 2

s3 = partial(spam, 1, 2, d = 42) # a = 1 b = 2 d = 42
