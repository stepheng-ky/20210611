#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 15:18
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 16运算符的优先级.py
# 功能描述  ：
# 和数学一样，Python运算符优先级 先乘除后加减
#
a = 1 + 2 * 3
print(a)
# and优先级高于or
# 运算符的优先级可以看官方文档的表格：https://docs.python.org/zh-cn/3/reference/expressions.html#operator-precedence
a = 1 or 2 and 3 # 1
print(a)
a = 1 and 3 or 2 # 3
print(a)

# 逻辑运算符 补充
# 逻辑运算符可以连着写
result = 1 < 2 < 3 # 1 < 2 and 2 < 3
print(result)