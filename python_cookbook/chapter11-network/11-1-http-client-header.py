#!/usr/bin/python
# -*- encoding: utf-8 -*-

from urllib import request, parse

# 使用urllib库，包含request及parse模块
# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Extra headers
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
# Make a POST request and read the response
# querystring是个可选参数
# headers是可选参数
# 构造request
req = request.Request(url, querystring.encode('ascii'), headers = headers)
u = request.urlopen(req)
resp = u.read()
print(resp)
