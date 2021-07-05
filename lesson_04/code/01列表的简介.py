#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 23:38
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 01列表的简介.py
# 功能描述  ：
# 通过[]来创建列表
my_list = []
print(my_list)
print(type(my_list))
# 列表存储的数据，称之为元素
# 一个列表可以存储多个元素 创建时也可以指定元素
my_list = [10] # 创建一个有一个元素10的列表
# 向列表中添加多个元素，元素之间用逗号隔开
my_list = [10,20,30,40] # 创建多个元素的列表
print(my_list)
my_list = [10,'1',None,True,[1,'1'],print] # 列表中包含多个不同类型的元素
print(my_list)

# 列表中的对象都会按照插入的顺序存储到列表中。
# 我们可以通过索引 index 获取列表中的元素
# 索引是从0开始的整数 第一个位置索引是0，第二个位置索引是1，第三个位置索引是2...
my_list = [10,20,30,40,50]
# 语法 my_list[索引]
print(my_list[0])
print(my_list[3])
# print(my_list[5])

# 获取列表的长度 len()
print(len(my_list))
print('============== 打印列表 my_list 的元素 =============')
for i in range(0,len(my_list)):
    print(my_list[i])