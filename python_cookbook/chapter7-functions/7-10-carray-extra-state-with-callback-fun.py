def apply_sync(func, args, *, callback):
    # compute the result
    result = func(*args)

    # invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got: ', result)


def add(x, y):
    return x + y


apply_sync(add, (2, 3), callback=print_result)
apply_sync(add, ('hello', 'word'), callback=print_result)