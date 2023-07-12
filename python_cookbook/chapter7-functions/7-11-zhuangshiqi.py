# def now():
#     print('2023-7-11')
#
# print('1. 简单函数调用')
# now()
import functools

def log(func):
    # 经过装饰后，其实返回的是新的函数，赋值给原来的函数名
    # __name__属性等都变化了
    # @functools.wraps() 保持函数原有属性不变化
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s(): ' % func.__name__)
        return func(*args, **kwargs)
    return wrapper
    # 装饰器是增强函数，返回的wrapper是func的增强版本，wrapper的入参，必须给到func
    # 装饰器这里是wrapper，其实使用装饰器时，返回的函数赋值给原函数
    # 如果装饰器要带参数，参数不能直接放到函数的装饰器上，因为直接装饰函数的装饰器函数参数只能是被装饰的函数

# 这里相当于直接调用log(func) 返回wrapper(增强的func
@log
def now(x):
    print(x)
    print('2023-7-11')

now(99)

# 带上装饰器等于函数重新赋值，获得增强。
# now = log(now) # 返回的是wrapper函数
# now(4) # 调用时，传入参数，其实时wrapper函数的参数。


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 相当于 log('execute')(func)
# log('execute') 返回的是decorator函数
# 也就是decorator(func)
# 返回wrapper，加了其他功能+func(*args, **kwargs)
# 装饰函数，就是传入函数为参数，返回一个增强的函数
@log('execute')
def now2():
    print('2015-3-25')

now2()