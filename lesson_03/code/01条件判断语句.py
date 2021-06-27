#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 16:07
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 01条件判断语句.py
# 功能描述  ：
# 条件判断 / if语句
# 语法： if ...:... else ...
print(1)
if True:print("True")
# 代码块 代码块保存一组代码，但是代码块不能放在:后，得换行
if True:
    print('True')
    print('haha')

number = 22
# 可以用逻辑运算符and or 连接多个条件
if number > 10 and number < 20 :
    print('number比10大！')
    print('number比20小！')

num = int(input('请输入数字：'))
if num > 10 and num < 20:
    print(num,'比10大，比20小')

username = input('请输入管理员账号：')
if username == 'admin':
    print('欢迎管理员~')
