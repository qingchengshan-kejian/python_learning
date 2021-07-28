#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    nmax = 50
    n = int(raw_input('intput the number of people:'))
    num = []
    for i in range(n):
        num.append(i + 1)
 
    i = 0
    k = 0
    m = 0
 
    while m < n - 1:
        if num[i] != 0 : k += 1 #k是辅助计数器
        if k == 3: #k为3 则标记为喊到数字3的人
            num[i] = 0 #数到3的 序号标记为0
            k = 0 #辅助计数器清零
            m += 1 #喊到3的人的个数（计数器）
        i += 1 #n 个人序号的循环
        if i == n : i = 0 #满一圈后重置为0
 
    i = 0
    while num[i] == 0: i += 1 #最后只剩下一个人的序号没有标记为0，并打印出来
    print num[i]