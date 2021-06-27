#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 15:02
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 15条件运算符.py
# 功能描述  ：
# 语法： 语句1 if 条件表达式 else 语句2
#           先对条件表达式进行求值判断
#           如果True，执行语句1；否则执行语句2
print('成功') if True else print('失败')
print('成功') if False else print('失败')
a = 10
b = 20
print('a大') if a > b else print('b大')
a = 30
b = 20
print('a大') if a > b else print('b大')
print(a if a > b else b)
a = 10
b = 200
c = 60
# a b c 通过条件运算符获取最大值
print((a if a > b else b) if (a if a > b else b) > c else c  )
print(max(a,b,c))
max_num = a if a > b else b
max_num = max_num if max_num > c else c
print(max_num)