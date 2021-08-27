#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    zi = int(input('输入一个数字:\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    print(sum)
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print ('%d  %d  %d' % (c9,zi,sum))
    r = sum //zi
    print ('%d / %d = %d' % (sum,zi,r))