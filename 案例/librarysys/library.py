# 图书管理系统 示意
import os

# 注册用户
def register():
    # 读入users文件
    p = os.path.dirname(__file__)
    with open(os.path.join(p,'users.txt')) as file:
        us = file.readlines()

    while True:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        rpassword = input('请确认密码：')

        if not username:
            print('用户名不能为空，请重新输入！')
            continue
        elif not password and not rpassword:
            print('密码不能为空！')
            continue
        elif password != rpassword:
            print('两次输入的密码必须一致！')
            continue
        # 判断是否已存在用户名
        for u in us:
            if username == u.split(' ')[0]:
                print('该用户名已存在，请重新输入')
                break
        else:
            #附加入users.txt 文件
            with open(os.path.join(p,'users.txt'),'a') as file:
                file.write(f'{username} {password}\n')
            break

# 用户登录
def login():
    # 读入users文件
    p = os.path.dirname(__file__)
    with open(os.path.join(p,'users.txt')) as file:
        us = file.readlines()
    
    for i in range(3):
        username = input('请输入用户名：')
        password = input('请输入密码：')
        user = f'{username} {password}\n'
        for u in us:
            if u == user:
                print(f'欢迎 {username} 进入系统')
                break
        else:
            print('用户名或密码错误！')
            continue
        break
    else:
        print('错误 3 次，自动退出系统！')

def readbook():
    # 读入books文件
    p = os.path.dirname(__file__)
    with open(os.path.join(p,'books.txt'),encoding='utf-8') as file:
        books = file.readlines()
    for b in books:
        print(b,end='')

# register()
# login()
# readbook()

