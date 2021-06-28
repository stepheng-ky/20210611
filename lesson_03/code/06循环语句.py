#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 22:29
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 06循环语句.py
# 功能描述  ：
print('hello')
# while True:
#     print('写个死循环')
i = 0;
while i < 10:
    print(f'i={i}')
    i += 1

# 100以内奇数之和
i = 1
sum = 0
while i <= 100 :
    if i % 2 != 0 :
        sum += i
    i += 1
print(f'100以内奇数求和={sum}')

# 100以内7的倍数之和 以及个数
i = 7
count = 0 # 个数
sum = 0 # 之和
while i <= 100:
    count += 1
    sum += i
    i += 7
print(f'100以内7的倍数之和{sum}')
print(f'100以内7的倍数有{count}个')




