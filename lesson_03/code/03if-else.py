#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 17:10
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 03if-else.py
# 功能描述  ：

# 输入年龄
age = int(input('请输入年龄：'))
if age > 18 :
    print('您已经成年了，可以喝酒了！')
else :
    print('你还小，不能喝酒哦！')

# 输入用户
username = input('请输入账号：')
if username == 'admin' :
    print(f'欢迎管理员{username}登录')
else :
    print(f'欢迎用户{username}登录')