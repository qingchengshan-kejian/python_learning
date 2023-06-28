#!/usr/bin/python
# -*- encoding: utf-8 -*-

from urllib import request, parse

# 使用urllib库，包含request及parse模块
# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = u.read()
print(resp)
