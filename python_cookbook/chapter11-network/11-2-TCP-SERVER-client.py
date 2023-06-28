#!/usr/bin/python
# -*- encoding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Hello')
print(s.recv(8192))