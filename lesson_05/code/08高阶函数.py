#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 21:32
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 08高阶函数.py
# 功能描述  ：
# 创建一个列表
l = [1,2,3,4,5,6,7,8,9,10]

# 定义一个函数 将指定的列表中所有的偶数保存到一个新的列表并返回
def fn(list):
    result = []
    for l in list:
        if l % 2 == 0:
            result.append(l)
    return result
print(fn(l))

def fn_main(func,list):
    result = []
    for i in list:
        if func(i):
            result.append(i)
    return result
def fn1(n):
    if n % 2 == 0 :
        return True
    return False
def fn2(n):
    if n >= 5 :
        return True
    return False
print(fn_main(fn1,l))
print(fn_main(fn2,l))

# filter()
# 可以从序列中过滤出符合条件的元素，保存到新的序列中
# 参数： 1.函数 2.序列 （可迭代）
# 返回值：符合条件的新序列结构
print(list(filter(fn1,l)))
print(list(filter(fn2,l)))

# 匿名函数 lambda 语法糖，舒服 ，语法比较简单
def fn5(a,b):
    return a + b
lambda a,b:a+b
print(fn5(10,20))
print((lambda a,b:a+b)(10,20))
# 也可以将匿名函数赋值给一个变量
fn6 = lambda a , b : a + b # 一般不会这么做 这样还不如直接命名一个函数
print(fn6)

# 改造lambda 偶数
lambda i:i%2==0
# filter()函数第一个参数是函数，匿名函数，第二个参数是list
print(list(filter(lambda i:i%2==0,l)))

# map()函数可以对可迭代的对象中的所有元素做指定操作，添加到新的对象中
l = [1,2,3,4,5,6,7,8,9,10]
r = map(lambda i:i**2,l )
print(list(r))

# sort() 对列表进行排序
#  默认比较大小
#  可以传key参数，传的是函数，它会先遍历所有元素调用此函数，将此函数返回值来进行比较 排序
l = ['123','2','ccca','dd','accc22222','bb']
l.sort()
print(l)
l.sort(key=len)
print(l)