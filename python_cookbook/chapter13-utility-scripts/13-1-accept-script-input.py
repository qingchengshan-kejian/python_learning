#!/usr/bin/python
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

'''
usage:
ls | ./filein.py
./filein.py < /etc/passwd
./filein.py /etc/passwd
'''