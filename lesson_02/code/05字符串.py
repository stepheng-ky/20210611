#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 0:22
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 05字符串.py
# 功能描述  ：

# 字符串 单引号或双引号都可；不可混合使用；相同的引号不能嵌套，不同的可以嵌套
s = 'hello world'
print(s)
s = 'hello "world"'
print(s)
# 长字符串 单引号和双引号不能跨行使用，可以加 \ 表示跨行
s = '鹅鹅鹅，' \
    '曲项向天歌，' \
    '白毛浮绿水，' \
    '红掌拨清波。'
print(s)
# 使用三重引号 表示长字符串 ''' 或者 """
# 三重引号可以换行 且保留字符串的格式
s = '''鹅鹅鹅，
曲项向天歌，
白毛浮绿水，
红掌拨清波'''
print(s)

# 转义字符 \  \' \"  \t \n \\ \uxxxx表示Unicode编码
s = "子曰：\"学而时习之，不亦说乎。\""
print(s)
s = '\u0064'
print(s)
s = '\u1cc0'
print(s)




