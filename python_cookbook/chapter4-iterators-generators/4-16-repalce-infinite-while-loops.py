#!/usr/bin/python
# -*- encoding: utf-8 -*-

CHUNKSIZE = 8192

# def reader(s):
#     while True:
#         data = s.recv(CHUNKSIZE)
#         if data == b'':
#             break
#         process_data(data)
# other way
# def reader(s):
#     for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
#         process_data(data)
# demo
import  sys
f = open('passwd.txt')
# l = f.read(10)
for chunk in iter(lambda :f.read(10), ''):
    n = sys.stdout.write(chunk)