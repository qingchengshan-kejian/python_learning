#!/usr/bin/python
# -*- encoding: utf-8 -*-

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


record = ('Dave', 'dave@163.dom', '773-555-1212', '444-666-7789')

name, email, *phone_numbers = record

print(phone_numbers)