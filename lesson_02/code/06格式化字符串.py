#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 23:46
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 06格式化字符串.py
# 功能描述  ：想打印 a = hello

a = "hello"
# 字符串之间也可以进行加法运算
# 如果将两个字符串进行相加，则自动将两个字符串拼接为一个字符串
a = "hello" + " world"
print(a)
# 第一种
print("a = " + a) # 这种写法在Python中不常见
a = 123
# print("a = " + a) # 字符串不能和其他类型进行加法运算 否则异常
# 1. print(a,b,c)
# 第二种
print("a =",a) # 这种写法，任何类型都可以拼接
# 2. 在创建字符串时，可以在字符串中指定占位符
# %s 在Python中表示任意字符
a = 'hello %s'
a = 'hello %s'%'world'
a = 'hello %s , world %s'%('1','2')
# %3s表示填充的位数至少3个，如果不够，自动空格补位，够了就全部打印
a = 'hello%3s'%'wo'
a = 'hello%3s'%'world'
# %3.5s表示长度限制3个到5个，不够就补位，多了就截取
a = 'hello%3.5s'%'w'
a = 'hello%3.5s'%'worldhahaha'
# %s可以也占位数字，但是对于数字不好限制小数位数
a = 'hello%s'%1234
a = 'hello%.2s'%232.456
print(a)
# %d 整数占位符
# %f 浮点数占位符
a = 'hello%d'%10
print(a)
a = 'hello%d'%10.23
print(a)
a = 'hello%.3f'%10.23
print(a)
# 第三种
print('a = %s'%a)


# 格式化字符串，可以在字符串前添加一个f来创建一个格式化字符串
a = f'hello'
a = '变量a'
b = '变量b'
print(a)
c = f'hello {a} {b}'
print(c)
# 第四种
print(f'a = {a}')


# 练习
print('####################################')
print('练习：四种方式打印欢迎xxx光临')
customer = '郭科元'
print('第一种：拼接')
print('欢迎 ' + customer + ' 光临！')
print('第二种：多个参数')
print('欢迎',customer,'光临！')
print('第三种：占位符')
print('欢迎 %s 光临！'%customer)
print('第四种：格式化字符串')
print(f'欢迎 {customer} 光临！')
print('####################################')
