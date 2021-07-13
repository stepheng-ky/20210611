#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 23:51
# @Author  : Stepheng
# @Email   : 1142262478@qq.com
# @File    : 07EMS练习.py
# 功能描述  ：

# EMS员工管理系统

# 初始化 员工信息list
employee = [['郭科元',20,'男','河南']]
employee.append(['gky','1','1','1'])
employee.append(['gky2','2','2','2'])
employee.append(['gky','3','3','3'])
employee.append(['gky3','4','4','4'])
employee_username = ['郭科元']
employee_username.append('gky')
employee_username.append('gky2')
employee_username.append('gky')
employee_username.append('gky3')

# 显示系统
while True:
    print(f'='*20,f'欢迎使用员工管理系统',f'='*20)
# 显示用户选项
    print(f'''请选择要做的操作：
    1.查询员工
    2.添加员工
    3.删除员工
    4.退出系统''')
    user_choose = input('请选择[1-4]：')
    print(f'='*58)
    # 处理用户的选择
    if user_choose == '1':
        # 打印表头
        print(f'序号\t\t姓名\t\t年龄\t\t性别\t\t住址')
        for e in employee:
            print(f'{employee.index(e)+1}\t\t{e[0]}\t\t{e[1]}\t\t{e[2]}\t\t{e[3]}')
    elif user_choose == '2':
        user_name = input('请输入姓名：')
        age = input('请输入年龄：')
        sex = input('请输入性别：')
        address = input('请输入住址：')
        user_info = [user_name,age,sex,address]
        employee.append(user_info)
        employee_username.append(user_name)
        print(f'员工{user_name}添加完成。')
    elif user_choose == '3':
        user_name_delete = input('请输入要删除的员工姓名：')
        if user_name_delete in employee_username:
            if employee_username.count(user_name_delete) >1 :
                print(f'同名员工{user_name_delete}有{employee_username.count(user_name_delete)}个'
                      f'，他们分别是：')
                # 复制临时列表 打印同名的员工信息
                tmp = employee_username[:]
                i = 0
                index_tmp_list = []
                print(f'序号\t\t姓名\t\t年龄\t\t性别\t\t住址')
                while user_name_delete in tmp:
                    index_tmp = tmp.index(user_name_delete)+i
                    index_tmp_list.append(str(index_tmp + 1))
                    print(f'{index_tmp + 1}'
                          f'\t\t{employee[index_tmp][0]}\t\t{employee[index_tmp][1]}'
                          f'\t\t{employee[index_tmp][2]}\t\t{employee[index_tmp][3]}')
                    tmp.pop(tmp.index(user_name_delete))
                    i += 1
                user_name_delete_index = input(f'请选择要删除的序号：')
                if user_name_delete_index in index_tmp_list :
                    print(f'序号{user_name_delete_index}的员工{user_name_delete}删除中。。。')
                    employee.pop(int(user_name_delete_index)-1)
                    employee_username.pop(int(user_name_delete_index)-1)
                    print(f'序号为{user_name_delete_index}的员工{user_name_delete}已删除。')
                else:
                    print(f'没有序号为{user_name_delete_index}的员工{user_name_delete}。删除失败。')
            else:
                print(f'员工{user_name_delete}删除中。。。')
                employee.pop(employee_username.index(user_name_delete))
                employee_username.pop(employee_username.index(user_name_delete))
                print(f'员工{user_name_delete}已删除。')
        else:
            print(f'员工{user_name_delete}不存在。无需删除。')
    elif user_choose == '4':
        print(f'=' * 58)
        input('欢迎使用！点击回车退出系统！')
        break
    else:
        print(f'选择无效，请重新选择。')

    # 打印分割线
    print(f'='*58)
