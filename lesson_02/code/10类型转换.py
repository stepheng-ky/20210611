#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 22:48
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 10类型转换.py
# 功能描述  ：

a = 'hello'
b = 123
print(a + str(b) + '\n')

# 类型转换四个函数 int() float() str() bool()
# int() 转换为整型
#   bool值：True-->1，False-->0
#   float： 直接取整
#   字符串：合法的数字，直接转换；不合法，则报错ValueError
# float():转换为浮点型
# str():转换为字符串
# bool():转换为bool值
#   规则：对于所有表示空性(0、None、''等)的对象，转换为False，其他都是True
a = True
a = False
a = 12.7
a = '12'
print('int函数：')
print(a)
print(type(a))
print(int(a))
print(type(int(a)))

a = 10
print('float函数：')
print(a)
print(type(a))
print(float(a))
print(type(float(a)))

# str()
a = True
print('str函数：')
print(a)
print(type(a))
print(str(a))
print(type(str(a)))

a = 12
print('bool函数：')
print(bool(a))
print(bool(0))
print(bool('hello'))
print(bool(''))
print(bool(None))