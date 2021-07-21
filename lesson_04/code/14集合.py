#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 0:07
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 14集合.py
# 功能描述  ：

# {} 、set() 创建集合
a = {1,20,3}
print(a,type(a))
s = set()
print(s,type(s))
# set可以将列表或字典转换为集合
a = [1,22,3,5,3,1]
print(a,type(a),set(a),type(set(a)))
a = {'a':1,'b':2}
print(a,type(a),set(a),type(set(a))) # set转换字典时，只保留了key


s = {'a','b',3,1}
print(s,type(s))

# 使用in和not in
print('a' in s)
print('ae' in s)

# len() 元素个数
print(len(s))

# add() 添加元素
s.add('haha')
print(s)

# update() 将某集合元素添加到这个集合
#   参数也可以是序列或字典
s2 = {'新的'}
s.update(s2)
print(s)

# pop() 删除 随机删除并返回一个元素
s.pop()
print(s)

# remove() 删除指定元素
s.remove('haha')
print(s)
# s.remove(233)

# clear 清空集合
s.clear()
print(s)

# copy() 浅复制
b = s.copy()
print(b,id(b),s,id(s))
