#!/usr/bin/python
# -*- coding: utf-8 -*-

record = '....................100 .......513.25 ..........'

SHARES = slice(20, 23)
PRICE = slice(31, 38)


cost = int(int(record[SHARES]) * float(record[PRICE]))

print(cost)