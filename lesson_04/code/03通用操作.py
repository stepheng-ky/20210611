#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 22:18
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 03通用操作.py
# 功能描述  ：
# 创建一个列表
status = ['孙','猪','孙','沙','唐','白','佛','菩']
# + 和 *
my_list = [1,2,3] + [4,5,6] # + 拼接
print(my_list)
my_list = [1,2,3]*4 # 重复次数
print(my_list)

# in 和 not in
# in用来检查指定元素是否存在于列表中
print('孙' in status)    # True
print('郭'  in status)   # False
print('孙' not in status)    # False
print('郭' not in status)    # True

# len()获取列表的元素个数
my_list = [1,2,6,3,4]
print(f'列表元素个数：{len(my_list)}')
# min()获取列表中最小值
my_list = ['d','1']
print(min(my_list))
# max()获取列表中最大值
print(max(my_list))
# print(status.index('郭')) # ValueError: '郭' is not in list
print(status.index('孙')) # 返回元素所在index
print(status.count('孙')) # 统计元素个数
print(status.count('郭')) # 统计元素个数
