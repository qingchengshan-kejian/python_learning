#!/usr/bin/python
"""Doc string here."""
# -*- encoding: utf-8 -*-
import queue
import blog_spider
import time
import random
import threading

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

def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    """Doc string here."""
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        print(threading.current_thread().name, f"craw {url}", "url_queue.size=", url_queue.qsize())
        html_queue.put(html)
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    """Doc string here."""
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        print(threading.current_thread().name, f"parse {url}", "url_queue.size=", html_queue.qsize())
        for result in results:
            fout.write(str(result) + "\n")
        time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)

    for idx in range(10):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}")
        t.start()

    fout = open("02_data.txt", "w")
    for idx in range(10):
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f"parse{idx}")
        t.start()