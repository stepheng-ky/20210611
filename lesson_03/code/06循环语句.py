#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 22:29
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 06循环语句.py
# 功能描述  ：
print('hello')
# while True:
#     print('写个死循环')
i = 0;
while i < 10:
    print(f'i={i}')
    i += 1

# 100以内奇数之和
i = 1
sum = 0
while i <= 100 :
    if i % 2 != 0 :
        sum += i
    i += 1
print(f'100以内奇数求和={sum}')

# 100以内7的倍数之和 以及个数
i = 7
count = 0 # 个数
sum = 0 # 之和
while i <= 100:
    count += 1
    sum += i
    i += 7
print(f'100以内7的倍数之和{sum}')
print(f'100以内7的倍数有{count}个')


# 水仙花
# 一个三位以上数字，每个位上的数字的n次幂之和等于自己
# （1**3 + 5**3 + 3**3 = 153）
# 打印1000以内的水仙花数字
i = 100
n = 1000
print(f'{i}到{n}之间的水仙花数字如下：')
while i < n :
    tihrd_num = i // 100
    second_num = (i % 100) // 10
    first_num = (i % 100) % 10
    if tihrd_num ** 3 + second_num ** 3 + first_num ** 3 == i :
        print(i)
    i += 1


# 输入一个数字 判断是否是质数
num = int(input('来个数字给你判断是否是质数：'))
i = 2
# 是否是质数
flag = True
if num == 1:
    print(f'{num}不是质数')
elif num == 2:
    print(f'{num}是质数')
else:
    while i <= num // 2 :
        if num % i == 0:
            flag = False
            break
        i += 1
    if flag :
        print(f'{num}是质数')
    else:
        print(f'{num}不是质数')
    print(f'循环了{i}次')