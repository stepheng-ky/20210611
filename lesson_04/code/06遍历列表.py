#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 23:19
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 06遍历列表.py
# 功能描述  ：
# 遍历列表就是将列表中的所有元素取出来
status = ['孙','猪','孙','沙','唐','白','佛','菩']

# 1.
# while循环
print(f'========= while循环遍历列表（不常用） =========')
i = 0
while i < len(status) :
    print(f'status第{i+1}个元素是{status[i]}')
    i += 1

# for循环
# 语法：
# for 变量 in 序列:
#    代码块
# 每执行一次，就会将下一个元素赋值给变量
print(f'========= for循环遍历列表（常用） =========')
for s in status :
    print(f'status第{status.index(s)+1}个元素是{s}')