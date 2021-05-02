import threading
from datetime import datetime


def thread_func():  # 线程函数
    print('我是一个线程函数', datetime.now())


def many_thread():
    threads = []
    for _ in range(10):  # 循环创建10个线程
        t = threading.Thread(target=thread_func)
        threads.append(t)
    for t in threads:  # 循环启动10个线程
        t.start()


if __name__ == '__main__':
    many_thread()
