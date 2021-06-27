#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 0:23
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 09类型检查.py
# 功能描述  ：yyyy
# 数据类型 ： 数值 （整型 布尔值 浮点型 复数）、字符串、空值
# 类型检查
a = 123     # 整型
b = '123'   # 字符串
print(f'a = {a}')
print(f'b = {b}')
# 打印结果一样， 区分不出来。如何判断？
# 通过类型检查 可以检查指定值或变量的值的类型,并返回
# type()用来检查值的类型
print(type(a))
print(f'a = {a} , a的类型是{type(a)}')
print(f'b = {b} , b的类型是{type(b)}')
# 打印几种类型
print('常见的几种类型打印type返回结果：')
print('##################################')
print(type(1))
print(type(1.5))
print(type(True))
print(type(False))
print(type('hello'))
print(type(None))
print('##################################')
