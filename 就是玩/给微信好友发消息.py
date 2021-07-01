#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 12:43
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 给微信好友发消息.py
# 功能描述  ：
# 使用微信接口给微信好友发送消息，
from wxpy import *

bot = Bot()

my_friends = bot.friends().search('那个姓郭的、', sex=MALE, city='上海')
#friend = ensure_one(my_friends)

friend = bot.friends().search('游戏小狗狗', sex=MALE, city='深圳')[0]

friend.send('这是通过Python发送给你的消息')