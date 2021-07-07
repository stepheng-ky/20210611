#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 22:28
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 04修改元素.py
# 功能描述  ：

# 创建一个列表
status = ['孙','猪','孙','沙','唐','白','佛','菩']
print(f'修改前：{status}')

# 直接通过索引修改元素
status[0] = '郭'
print(f'1.通过索引修改后：{status}')

# 通过del删除元素
del status[0]
print(f'2.del删除元素：{status}')

# 通过切片修改
# 在给切片赋值时，必须传递一个序列
status[0:2] = ['小郭','大佬'] # 替换多个元素
status[0:2] = ['小郭','大佬','牛批'] # 替换多个元素
status[0:2] = ['小郭']
status[0:0] = ['嘿嘿'] # 在最前边插入一个元素
# status[::2] = ['第一个'] # 当设置了步长时，元素个数必须等于切片的元素个数
print(f'3.切片修改元素：{status}')
del status[0:2] # 删除0，1的元素 类似 status[0:2] = []
print(f'4.del删除切片：{status}')

# 以上操作只适用于可变序列 列表
s = 'hello'
print(s)
# s[1] = 'a'  # str不可变，报错
# 可以通过list() 函数将其他的序列转换为list
s = list(s)
print(f's转换为list：{s}')
s[1] = 'a'
print(f'list a改元素后：{s}')