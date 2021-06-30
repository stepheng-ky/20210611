#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 23:07
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 14练习优化.py
# 功能描述  ：
# 打印100以内质数
# 引入time模块记录程序运行时间
from time import *
start_time = time()
i = 2
n = 100000
print(f'############## 打印{n}以内质数 ##############')
count = 0
while i <= n:
    flag = True
    j = 2
    while j <= i ** 0.5:
        if i % j == 0 :
            flag = False
            break
        j += 1
    if flag :
        print(i,end=' ')
        count += 1
    i += 1
print(f'\n如上，{n}以内有{count}个质数')
end_time = time()
spend_time = end_time - start_time
print(f'程序运行花费了{spend_time}s')