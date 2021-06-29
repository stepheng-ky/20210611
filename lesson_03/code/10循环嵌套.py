#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 22:16
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 10循环嵌套.py
# 功能描述  ：

# 循环嵌套
# 打印
# *****
# *****
# *****
# *****
# *****
# column = int(input('输入列：'))
# row = int(input('输入行：'))
# i = 1
# while i <= row :
#     print('*'*column)
#     i += 1
print('############## 打印多行多列** ##############')
column = 10
row = 10
i = 1
while i <= row :
    j = 1
    while j <= column :
        print('*',end='')
        j += 1
    print()
    i += 1

# 打印
# *
# **
# ***
# ****
# *****
print('############## 三角形* ##############')
i = 1
n = 5
while i <= n :
    j = 1
    while j <= i:
        print('*',end='')
        j += 1
    print()
    i += 1

# 打印九九乘法表
print('############## 打印九九乘法表 ##############')
i = 1
while i <= 9 :
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j}',end=' ')
        j += 1
    print()
    i += 1

# 打印100以内质数
print('############## 打印100以内质数 ##############')
i = 2
count = 0
while i <= 100:
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
print(f'\n100以内有{count}个质数')