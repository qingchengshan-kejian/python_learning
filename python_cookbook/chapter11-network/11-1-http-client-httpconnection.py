#!/usr/bin/python
# -*- encoding: utf-8 -*-

# from http.client import HTTPConnection
# from urllib import parse
#
# c = HTTPConnection('www.python.org', 80)
# c.request('HEAD', '/index.html')
# resp = c.getresponse()
#
# print('Status', resp.status)
# for name, value in resp.getheaders():
#     print(name, value)

# import urllib.request
#
# auth = urllib.request.HTTPBasicAuthHandler()
# auth.add_password('pypi', 'http://pypi.python.org', 'username', 'password')
# opener = urllib.request.build_opener(auth)
#
# r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
# u = opener.open(r)
# resp = u.read()
# print(resp)
# # From here. You can access more pages using opener

import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37',
                 headers = {'User-agent': 'goaway/1.0'})
resp = r.json()
# print(resp)
print(resp['headers'])
print(resp['args'])
# httpbin.org是个很好的测试代码的网站
