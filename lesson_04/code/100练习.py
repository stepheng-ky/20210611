#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 17:38
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 100练习.py
# 功能描述  ：
a = 'xydz'
print(a)
def solve_it():
    c = a[::-1]
    return c
print(solve_it())

a = {'1':1,'2':2,'3':3}
print(','.join(a.keys()))

a = 'hello'
b = '-'
print(b.join(a))