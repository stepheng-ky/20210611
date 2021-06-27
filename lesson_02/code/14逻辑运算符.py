#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 23:27
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 14逻辑运算符.py
# 功能描述  ：
# and  or  not
# not 逻辑非
#   对bool值进行取反操作 not True = False
#   对于非bool值，先将其转换为bool值，然后取反
# and 逻辑与
#   与运算找False
#   Python中的与运算是短路的与，如果第一个值是False，就不再看第二个值
# or 逻辑或
#   或运算找True
#   Python中的或运算也是短路的或，如果第一个是True，就不再看第二个值

a = True
print('a =',a)
a = not a
print('a =',a)
a = 1
print('a =',a)
a = not 1
print('a =',a)
a = not 0
print('a =',a)
a = True and True
print('a =',a)
a = True and False
print('a =',a)
a = False and False
print('a =',a)
#   Python中的与运算是短路的与，如果第一个值是False，就不再看第二个值
True and print('and True所以打印我')
False and print('and False所以不打印我')
a = True or False
print('a =',a)
a = False or False
print('a =',a)
#   Python中的或运算也是短路的或，如果第一个是True，就不再看第二个值
False or print('or False所以打印我')
True or print('or True所以不打印我')

# 非bool值的 与或运算
#   当对非bool值进行与或运算时，Python会将其当作bool值运算，最终返回原值
#   原值！ 原值！ 原值！
#   与 找False的，如果第一个是False就不看第二个，直接返回第一个，否则返回第二个
print(1 and 2 ) # 2 找False的，如果第一个是False就不看第二个，但是这个第一个是True看第二个，所以返回2
print(1 and 0)  # 0 第一个True，看第二个0，返回0
print(0 and 1)  # 0 第一个是False，不看第二个，返回第一个0
print(0 and None) # 0 第一个是False，返回第一个0
print(None and 0) # None 第一个是False，返回第一个None
#   或 找True的，第一个如果是True就不看 第二个，直接返回第一个，否则返回第二个
print(1 or 2) # 1 第一个1True，直接返回1
print(2 or 1) # 2 第一个2True，直接返回2
print(2 or 0) # 2 第一个2True，直接返回2
print(0 or 2) # 2 第一个0False，找第二个返回
print(0 or None) # None 第一个0False，找第二个返回
True and print('True所以打印我')
False and print('False所以不打印我')
