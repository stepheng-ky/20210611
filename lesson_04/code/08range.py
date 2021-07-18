#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 0:11
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 08range.py
# 功能描述  ：
# range是一个函数 可以生成一个自然数的序列
# 该函数需要三个参数：1.起始位置（默认0） 2.结束位置 3.步长（默认1）
# 通过range(),可以创建一个执行指定次数的for循环
r = range(5)
print(r)
my_list = list(r)
print(my_list)
for i in r:
    print(i)
r = range(0,10,2)
print(list(r))
r = range(10,0,-2)
print(list(r))
