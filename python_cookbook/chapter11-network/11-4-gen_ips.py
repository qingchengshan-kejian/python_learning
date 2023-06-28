#!/usr/bin/python
# -*- encoding: utf-8 -*-

import ipaddress
net = ipaddress.ip_network('123.45.67.64/26')
print(net)

for a in net:
    print(a)