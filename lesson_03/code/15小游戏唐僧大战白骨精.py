#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 23:37
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 15小游戏唐僧大战白骨精.py
# 功能描述  ：

# 唐僧大战白骨精
# 1.身份选择
#   1.1 显示提示信息
#           欢迎光临游戏
#           请选择身份 1.** 2.**
#           请选择
#   1.2 根据用户的选择提示不同的信息
#           1. --
#           2. --
#           3. --
# 2.进行游戏
#   2.1 显示玩家的基本信息（攻击力 生命值）
#   2.2 显示玩家可以进行的操作：
#       1、练级
#           提升攻击力、生命值
#       2、打boss
#           - 玩家攻击boss，boss反击
#           - 计算谁死 玩家or boss
#           - 游戏结束
#       3、逃跑
#           - 退出游戏，提升游戏结束

# 显示提示信息
game_name = '《唐僧大战白骨精》'
print(f'============= 欢迎光临游戏{game_name} =============')
print('''请选择您的身份：
    1、唐僧
    2、白骨精''')
id = input('请选择[1/2]：')
print('='*70)
if id == '1' :
    print('您已经选择唐僧，恭喜你将以唐僧的身份进行游戏！')
elif id == '2' :
    print('您已经选择白骨精~然鹅，系统不同意。系统将自动为您分配唐僧的身份进行游戏！')
else :
    print('您的选择无效~系统将自动为您分配唐僧的身份进行游戏！')
attack_player = 2
life_player  = 2
attack_boss = 10
life_boss = 15
print('=' * 70)
print(f'您的身份是->唐僧<-，您的攻击力是：{attack_player},您的生命值是：{life_player}。')
# 由于游戏选项是需要反复选择的，因此得写循环；写死循环 给用户决定是否结束
while True:
    print('=' * 70)
    print(f'提示：BOSS的攻击力是：{attack_boss},BOSS的生命值是：{life_boss}。')
    print('='*70)
    print('''请选择您要做的操作：
        1、练级
        2、打boss
        3、逃跑''')
    choose_player = input('请选择[1/2/3]：')
    # 处理用户的选择
    if choose_player == '1':
        # 增加玩家攻击力和生命值
        life_player += 2
        attack_player += 2
        print('=' * 70)
        print(f'恭喜升级成功！您现在的攻击力是：{attack_player},生命值是：{life_player}。')
    elif choose_player == '2':
        # 玩家攻击BOSS
        life_boss -= attack_player
        print('=' * 70)
        print('您攻击了BOSS。')
        if life_boss <= 0:
            print(f'BOSS受到{attack_player}点伤害，已死亡。玩家胜利！')
            break
        # BOSS攻击玩家
        print(f'BOSS受到{attack_player}点伤害，剩余生命值{life_boss}。')
        print('=' * 70)
        print(f'BOSS攻击了您。')
        life_player -= attack_boss
        if life_player <= 0 :
            print(f'玩家受到{attack_boss}点伤害，已死亡。BOSS胜利！')
            break
        print(f'玩家受到{attack_boss}点伤害，剩余生命值{life_player}。')
        print('=' * 70)
        print(f'您的身份是->唐僧<-，您的攻击力是：{attack_player},您的生命值是：{life_player}。')
    elif choose_player == '3' :
        # 逃跑  退出游戏
        print(f'您无耻的逃跑了。游戏失败。BOSS胜利！')
        break