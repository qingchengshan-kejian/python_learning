import time
from functools import wraps


def timethis(func):
    '''
    decorator that reports the execution time.
    '''

    # 这条装饰器，就是实现原有函数属性的保留。
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    '''
    counts down
    '''
    while n > 0:
        n -= 1

countdown(1000000)