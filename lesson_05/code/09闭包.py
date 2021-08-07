#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 22:31
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 09闭包.py
# 功能描述  ：

# 将函数作为返回值返回，也是高阶函数
# 这种高阶函数 也叫闭包；通过闭包可以创建一些只有当前函数可以访问的变量；
#   可以将私有的数据藏在闭包中

def fn():
    # 函数内部定义一个函数
    a = 10
    def inner():
        print('我是inner',a)
    # 返回内部函数inner
    return inner

# r是一个函数，是调用fn()后返回的函数
# 这个函数是在fn()内部定义的 不是全局函数
# 所以它可以访问fn()的所有变量
r = fn()
r()


# 求多个数的平均值
nums = [50,20,30,10,77]

# sum求和先,然后除以len
print(sum(nums)/len(nums))
def make_avgeage():
    # 创建一个列表 保存数据
    nums = []
    # 创建一个函数计算平均值
    def average(n):
        nums.append(n)

        # 求平均值
        return sum(nums)/len(nums)
    return average
average = make_avgeage()
print(average(10))
print(average(20))
print(average(30))
print(average(40))