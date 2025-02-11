import time
from functools import wraps


def timethis(func):
    '''
    decorator that reports the execution time.
    '''
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

# 元编程
# 软件开发领域中最经典的口头禅就是“don’t repeat yourself”。
# 也就是说，任何时候当你的程序中存在高度重复(或者是通过剪切复制)的代码时，都应该想想是否有更好的解决方案。
# 在Python当中，通常都可以通过元编程来解决这类问题。
# 简而言之，元编程就是关于创建操作源代码(比如修改、生成或包装原来的代码)的函数和类。
# 主要技术是使用装饰器、类装饰器和元类。
# 不过还有一些其他技术， 包括签名对象、使用 exec() 执行代码以及对内部函数和类的反射技术等。
