#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    i = 0
    j = 1
    x = 0
    while (i < 5) :
        x = 4 * j #j是最后一个猴子分完拿走后剩下4份每份的个数 基本算法是 *5+1 后必须还能整除4
        for i in range(0,5) :
            if(x%4 != 0) : #连续5次循环，如果出现不能整除4的情况，则j是不正确的，最后答案是找到正确的j
                break
            else :
                i += 1 #此处i 是用来结束while循环的
            x = (x/4) * 5 +1
        j += 1 #不能完整经过for循环的j 要自加1
    print x

