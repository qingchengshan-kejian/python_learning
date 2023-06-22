#!/usr/bin/python
"""Doc string here."""
# -*- encoding: utf-8 -*-

import requests
import threading
import time
from bs4 import BeautifulSoup

# 原先的print函数和主线程的锁
_print = print
mutex = threading.Lock()


# 定义新的print函数
def print(text, *args, **kw):
    '''
    使输出有序进行，不出现多线程同一时间输出导致错乱的问题。
    '''
    with mutex:
        _print(text, *args, **kw)


urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]

# 单功能函数
# 并行运行多个单功能函数
def craw(url):
    """Doc string here."""
    r = requests.get(url)
    print(url, len(r.text))

# craw(urls[0])


def single_thread():
    """Doc string here."""
    for url in urls:
        craw(url)


time1 = time.time()
single_thread()
time2 = time.time()
delta_time = time2 - time1
print("single thread cost time: %f\n" % delta_time)


def multi_thread():
    """Doc string here."""
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url, ))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

time1 = time.time()
multi_thread()
time2 = time.time()
delta_time = time2 - time1
print("multi thread cost time: %f\n" % delta_time)