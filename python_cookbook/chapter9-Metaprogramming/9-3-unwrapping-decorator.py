@somedecorator
def add(x, y):
    return x + y

orig_add = add.__wrapped__ # 还原被装饰的函数。
orig_add(3, 4)