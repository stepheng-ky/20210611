#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 22:00
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 02切片.py
# 功能描述  ：
# 切片 指从现有列表中，获取一个子列表
status = ['孙','猪','沙','唐','白','佛','菩']
print(status[2])
# 列表的索引也可以是负数 指倒数第几个 -1 倒数第一个。。。
print(status[-1])

# 通过切片获取指定的元素
# 语法：列表[起始索引:结束索引] 子列表包含起始，不包含结束
print(status[1:4]) # 索引1到索引3，不包含索引4的
print(status[0:5]) # 索引0到索引4，不包含索引5的
print(status[0:9]) # 结束位置超过长度 不报错
print(status)
print(status[1:])  # 起始或结束可以省略 省略结尾，一直到最后
print(status[:4])  # 省略开始位置，从第一个开始
print(status[:])   # 开始和结束都省略，相当于创建了副本，返回所有的元素
print(status[2:1]) # 起始位置在结束位置之后，返回空

# 语法：列表[起始:结束:步长]
# 步长不能是0，可以是负数
print(status[1:5:2]) # 1到5 2个步长 也就是打印索引 1、3
print(status[::3]) # 全部索引，每隔2个打印
# print(status[::0])
print(status[::-1]) # 如果是负数，从结束位置往前，倒序
