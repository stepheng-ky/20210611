#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 23:50
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 13关系运算符.py
# 功能描述  ：
# 比较两个值之间的关系，返回bool值；如果成立返回True，否则返回False
# > < == >= <= !=
result = 10 > 20
print(result)
result = 10 < 20
print(result)
result = 10 == 20
print(result)
result = 10 == 10
print(result)
result = 10 >= 20
print(result)
result = 10 <= 20
print(result)
result = 10 != 20
print(result)
# 在Python中可以对两个字符串进行大于或小于运算
# 实际上是比较的是字符串的unicode编码
# 我们比较两个字符串时，是逐位比较的
# 此特性可以用于对字符串进行排序
result = '2' > '11'
print(result)
result = int('2') > int('11')
print(result)
result = 'a' > 'b'
print(result)
result = 'ab' > 'b'
print(result)
result = '测试' > '哈哈' # 中文意义不大
print(result)
# is  is not 比较的是id
result = 'a' is 'a'
print(result)
result = 1 is True
print(result)
print(id(1),id(True))
result = 1 == True
print(result)









