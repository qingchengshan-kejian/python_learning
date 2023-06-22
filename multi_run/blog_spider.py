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
    # print(url, len(r.text))
    return r.text

# craw(urls[0])

def parse(html):
    # class="post-item-title"
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_ = "post-item-title")
    return [(link["href"], link.get_text()) for link in links]

if __name__ == "__main__":
    for result in parse(craw(urls[2])):
        print(result)
