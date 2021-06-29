#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 22:50
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 13break和continue.py
# 功能描述  ：
# break 立即退出循环
# continue

print('########## 测试break ##########')
i = 1
n = 10
while i <= n :
    print(i)
    i += 1
    if i == 5 :
        print('跳出循环')
        break
else :
    print('循环结束')

print('########## 测试continue ##########')
i = 1
n = 10
while i <= n :
    print(i)
    i += 1
    if i == 5 :
        print('continue')
        continue
else:
    print('循环结束')