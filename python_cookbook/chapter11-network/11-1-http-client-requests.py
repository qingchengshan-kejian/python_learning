#!/usr/bin/python
# -*- encoding: utf-8 -*-

import requests

# Base URL being accessed
# url = 'http://httpbin.org/post'
#
# # Dictionary of query parameters (if any)
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
#
# # Extra Headers
# headers = {
#     'User-agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }

# resp = requests.post(url, data = parms, headers = headers)

# Decoded text returned by the request
# text = resp.text
# print(text)

# resp1 = requests.head('http://httpbin.org/')
# status = resp1.status_code
# # last_modified = resp1.headers['last-modified']
# content_type = resp1.headers['content-type']
# content_length = resp1.headers['content-length']
#
# print(status, content_length, content_type)

# resp2 = requests.get('http://pypi.python.org/pypi?:action=login', auth=('user', 'password'))
# print(resp2.json)

# # cookies demo
# url = 'http://httpbin.org/get'
# resp1 = requests.get(url)
# resp2 = requests.get(url, cookies=resp1.cookies)
# print(resp2)

# upload content
url = 'http://httpbin.org/post'
files = {'file': ('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files = files)
print(r)
