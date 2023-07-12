def apply_sync(func, args, *, callback):
    result = func(*args)

    callback(result)


from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def inlined_async(func):
        @wraps(func)
        def wrapper(*args):
            f = func(*args)
            result_queue = Queue()
            result_queue.put(None)
            while True:
                result = result_queue.get()
                try:
                    a = f.send(result)
                    apply_sync(a.func, a.args, callback=result_queue.put)
                except StopIteration:
                    break
        return wrapper

## 装饰器，还是没有记住！！！
