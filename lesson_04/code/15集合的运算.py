#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 0:06
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 15集合的运算.py
# 功能描述  ：
# 创建两个集合
s = {1,2,3,4,5}
s2 = {3,4,5,6,7}
# & 交集
print(s,s2,s & s2)
# | 并集
print(s,s2,s | s2)
# - 差集
print(s,s2,s - s2)
print(s,s2,s - (s & s2))
# ^亦或集
print(s,s2,s ^ s2)
print(s,s2,(s - s2) | (s2 - s))
# <= 检查一个集合是否是另一个集合的子集
print(s,s2,s <= s2)
print(s,s2,s & s2,(s & s2) <= s)
# < 检查一个集合是否是另一个集合的真子集
print(s,s2,s < s2)
print(s,s2,s & s2,(s & s2) < s)
# >=  >  超集 真超集
print(s,s2,s > s2)
print(s,s2,s & s2,s > (s & s2) )

