#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 17:17
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 04if-elif-else.py
# 功能描述  ：

# if-elif-else

username = input('用户名：')
if username == 'admin':
    print(f'欢迎管理员{username}登录。')
elif username == 'superadmin' :
    print(f'欢迎超级管理员{username}登录')
elif username == 'ywadmin' :
    print(f'欢迎运维管理员{username}登录')
else:
    print(f'欢迎用户{username}登录')

num = int(input('请输入数字给你判断奇偶：'))
if num % 2 == 0 :
    print(f'{num}是偶数')
else :
    print(f'{num}是奇数')

year = int(input('输入年份我给你判断是否是闰年：'))
if year % 400 == 0 :
    print(f'{year}是闰年。')
elif year % 100 !=0 and year % 4 == 0 :
    print(f'{year}是闰年。')
else:
    print(f'{year}不是闰年。')

age = float(input('输入你家狗狗的年龄。我给你换算人的年龄：'))
if age < 0:
    print(f'你家狗狗{age}岁了。假的吧！')
elif age <= 2:
    age_p = age * 10.5
    print(f'你家狗狗{age}岁了。相当于人的{age_p}岁。')
else:
    age_p = 21 + 4 * (age - 2)
    print(f'你家狗狗{age}岁了。相当于人的{age_p}岁。')
