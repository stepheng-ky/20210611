#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 21:51
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 02基本语法.py
# 功能描述  ：


# 1. 严格区分大小写
print('Hello')
#Print('Hello2')

# 2. 每一行都是一个语句 换行即结束  ,无需分号等

# 3. Python每一行长度不要过长，建议不要超过80个字符
print('HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello')

# 4. 一条语句可以多行编写，语句后以\结尾
print\
    ('HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHe\
    lloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello')

# 5. Python是缩进严格的语言，不要随便写缩进
    # print('测试缩进') # 此语句会报错

# 6. Python注释使用#，#后即是注释的内容，注释的内容会被解释器忽略
# 一般#后会跟一个空格
# 上边的是多行注释
print('单行注释示例：') # 这是一个单行注释

# 7. 字面量和变量
# 字面量就是一个值，1，3，3，4，6，'Hello'等
# 字面量表示的意思就是它字面的值，在程序中可以直接使用字面量
print(123,end=' ')
print('字面量测试')
# 变量（variable）可以用来保存字面量，并且变量中保存的字面量是不定的
# 变量本身没有任何意义，根据不同的字面量表示不同的含义
a=10
print(a,end=' ')
a='变量测试'
print(a)
# 都是用变量表示字面量
