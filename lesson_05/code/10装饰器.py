#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 18:45
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 10装饰器.py
# 功能描述  ：

def add(a,b):
    '''
    求任意两个数的和
    :param a:
    :param b:
    :return:
    '''
    r = a + b
    return r


def mul(a,b):
    '''
    求任意两个数的乘积
    :param a:
    :param b:
    :return:
    '''
    r = a * b
    return r

# 希望函数可以在计算前，打印开始计算；计算结束后打印计算完毕
#   我们可以通过直接修改函数中的代码完成此需求，但是会产生以下几个问题：
#       1 如果要修改的函数过多，修改起来比较麻烦
#       2 并且不方便后期维护
#       3 并且这样做会违反开闭原则（OCP ）
#           程序的设计 要求开放对程序的扩展，关闭对程序的修改。

# r = add(12,34)
# print(r)

# 我们希望在不修改原来函数的情况下，来对函数进行扩展
def fn():
    print('我是fn函数...')

# 只需要根据现有的函数，创建一个新的函数
def fn2():
    print('函数开始执行...')
    fn()
    print('函数执行结束...')

# fn2()

def new_add(a,b):
    print('计算开始...')
    r = add(a,b)
    print('计算结束...')
    return r

# r = new_add(12,23)
# print(r)

# 上边的方式已经可以在不修改源代码的情况下，对函数进行扩展；
#   但是，这种方式要求每扩展一个函数就要手动创建一个新的函数，实在是太麻烦。
#   为了解决这个问题，可以创建一个函数，让这个函数可以自动帮助我们生成函数

def begin_end(fun):
    '''
    作用：对其他函数进行扩展，使其他函数可以执行前打印“开始执行”，执行完成后打印“执行结束”。
    参数：
        要扩展的函数
    :return:
    '''
    # 创建一个新函数
    def new_function(*args,**kwargs):
        print('开始执行~~~')
        # 调用被扩展的函数
        result = fun(*args,**kwargs)
        print('执行结束~~~')
        return result

    # 返回新函数
    return new_function

# f = begin_end(add)
# r = f(1,24)
# print(r)
#
#
# f = begin_end(fn)
# f()

# 像begin_end这种函数，我们称它为装饰器
#   通过装饰器，可以在不修改原来函数的情况下对函数进行扩展
#   在开发中，都是通过装饰器来扩展函数的功能
# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，来装饰当前函数
#   可以使用多个装饰器，这样函数会按照由内到外的顺序被装饰

@begin_end
def say_hello():
    print('大家好！')

say_hello()

@begin_end
def sum(a,b):
    return a + b

r = sum(1,44)
print(r)