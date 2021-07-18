#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 22:46
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 05列表的方法.py
# 功能描述  ：

# 列表的方法
status = ['孙','猪','孙','沙','唐','白','佛','菩']
print(f'打印列表status：{status}')
status.append('append追加的元素')    # append追加到最后位置
print(f'append添加后：{status}')
status.insert(2,'insert插入元素') # 在指定位置插入新的元素；类似 status[2:2] = '插入的'
print(f'insert插入后：{status}')
status[2:2] = ['索引插入的元素']   # 索引插入
print(f'索引插入元素后：{status}')
status.extend(['extend扩展1','extend扩展2'])    # 将其他列表添加到此列表
print(f'extend扩展后：{status}')
status.clear()  # 清空所有元素
print(f'clear清空后：{status}')
status = ['孙','猪','孙','沙','唐','白','佛','菩']
print(f'新的列表：{status}')
a = status.pop(3)   # 删除索引=2的元素,并返回这个元素;默认删除最后一个
print(f'pop删除后：{status},删除的元素是：{a}')
status.remove('孙')  # 指定元素删除，如果有多个此相同元素，只删除第一个此元素；如果没有此元素，error
print(f'remove删除后：{status}')
status.reverse()    # 反转,类似[::-1]
print(f'reverse反转之后：{status}')
status = status[::-1]
print(f'用索引::-1反转：{status}')
# sort() 排序,默认升序排列 降序用sort(reverse=True)
status.sort()
print(f'sort排序后：{status}')


L = [2,1,10,3]
print(L.sort())
print(L)
print(L.sort(reverse=True))
print(L)