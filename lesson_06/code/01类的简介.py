#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 20:38
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 01类的简介.py
# 功能描述  ：

class MyClass():
    pass

mc = MyClass()
mc2 = MyClass()
print(mc,id(mc),type(mc),isinstance(mc,MyClass))
print(mc2,id(mc2),type(mc2),isinstance(mc2,MyClass))