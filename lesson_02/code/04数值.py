#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 0:03
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 04数值.py
# 功能描述  ：
# 在Python中 数值分为三种：整数、浮点数、复数
# 在Python中所有整数都是int类型
# Python 中整数的大小没有上限 无限大
# 如果数字长度过大，可以用下划线作为分隔符
a = 1_2_3
print(a)
# 十进制的数字不能以0开头
# 二进制 0b开头
a = 0b10
# 八进制 0o开头
a = 0o10
# 十六进制 0x开头
a = 0x10

# 浮点（小数），在Python中所有浮点数都是float类型
a = 1.1
# 对浮点数进行运算，得到的是不精确的数
print(1.2+2.3)
a = 1.2
b = 2.3
c = 0.1 + 0.2 # 0.30000000004
print(c)