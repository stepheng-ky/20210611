#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 23:32
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 07递归.py
# 功能描述  ：

# 求阶乘
def jiecheng(n):
    if n == 1:
        result = 1
    else:
        result = n*jiecheng(n-1)
    return result
a = 10
print(f'{a}的阶乘 1 ={jiecheng(a)}')

def jiecheng2(n):
    if n == 1 :
        return 1
    return n*jiecheng2(n-1)
print(f'{a}的阶乘 2 ={jiecheng2(a)}')
