# 图书管理系统 示意
import os

# 注册用户
def regist():  
    # 读入users文件
    p = os.path.dirname(__file__)
    with open(os.path.join(p,'users.txt'),encoding='utf-8') as file:
        us = file.readlines()

    while True:
        user_name = input('请输入用户名：')
        password = input('请输入密码：')
        re_password = input('请确认密码：')

        if not user_name:
            print('用户名不能为空，请重新输入！')
            continue
        elif not password and not re_password:
            print('密码不能为空！')
            continue
        elif password != re_password:
            print('两次输入的密码必须一致！')
            continue
        # 判断是否已存在用户名
        for u in us:
            if user_name == u.split(' ')[0]:
                print('该用户名已存在，请重新输入')
                break
        else:
            #附加入users.txt 文件
            with open(os.path.join(p,'users.txt'),'a',encoding='utf-8') as file:
                file.write(f'{user_name} {password} []\n')
            break

# 用户登录
def login():
    # 读入users文件
    print('---用户登陆---')
    user_r = ''
    p = os.path.dirname(__file__)
    with open(os.path.join(p,'users.txt'),encoding='utf-8') as file:
        us = file.readlines()
    
    for i in range(3):
        user_name = input('请输入用户名：')
        password = input('请输入密码：')
        user = f'{user_name} {password}'
        for u in us:
            if user in u:
                print(f'欢迎 {user_name} 进入系统')
                user_r = user_name
                break
        else:
            print('用户名或密码错误！')
            continue
        break
    else:
        print('错误 3 次，自动退出系统！')
    
    return user_r

def show_book():
    # 读入books文件
    # 返回现有图书列表['三国','水浒'] 或[]
    r_books = []
    p = os.path.dirname(__file__)
    with open(os.path.join(p,'books.txt'),encoding='utf-8') as file:
        books = file.readlines()
    if not books:
        print('存书已被全部借出，请稍后再试_^^_')
        return r_books
    for i,b in enumerate(books):
        r_books.append(b[:-1])
        print(i+1,b,end='')

    return r_books

# 借书
def borrow_book(user):
    '''
    传入用户名字
    '''
    # 判断books是否为空【图书被人借完后会空！！】
    books = show_book()
    if not books: # 如果存书为空，则退出
        return
    n_book = int(input('请选择要借出的书籍序号：'))
    book = books[n_book - 1]

    p = os.path.dirname(__file__)
    with open(os.path.join(p,'users.txt'),encoding='utf-8') as file:
        user_old = file.readlines()
    # user_name = user
    user_new = []
    for i in user_old:
        if user in i:
            line_new = i[:-2]+book+",]\n"
            user_new.append(line_new)
        else:
            user_new.append(i)
    with open(os.path.join(p,'users.txt'),'w',encoding='utf-8') as file:
        file.writelines(user_new)
    
    # 更新books.txt文件
    with open(os.path.join(p,'books.txt'),encoding='utf-8') as file:
        books_old = file.read()
    books_new = books_old.replace(book+'\n','')
    with open(os.path.join(p,'books.txt'),'w',encoding='utf-8') as file:
        file.writelines(books_new)



    print(f'借书 《{book}》 成功')


#还书
def return_book(user):
    '''
    传入用户名，自己持有的图书列表
    '''
    # 列出自己持有的书籍
    p = os.path.dirname(__file__)
    with open(os.path.join(p,'users.txt'),encoding='utf-8') as file:
        user_old = file.readlines()
    for i in user_old:
        if user in i:
            books_oldline = i
            books = i[i.index('[')+1:-3].split(',')
            break

    if books[0] != '': # 如果有借书，则执行，没有则退出
        print(f'用户：{user} 借出的书籍如下：')
        for i,b in enumerate(books):
            print(i+1,b)
        n_book = int(input('请选择要归还的书籍序号：'))
        book = books.pop(n_book - 1)

        books_newline = books_oldline.replace(book+',', '')

        user_new = []
        for i in user_old:
            if user in i:
                books_newline = books_oldline.replace(book+',', '')
                user_new.append(books_newline)
            else:
                user_new.append(i)
        with open(os.path.join(p,'users.txt'),'w',encoding='utf-8') as file:
            file.writelines(user_new)

        # 更新books.txt文件
        with open(os.path.join(p,'books.txt'),'a',encoding='utf-8') as file:
            file.writelines(book+'\n')
        
        print(f'还书 《{book}》 成功')
    else:
        print('没有借出书籍，请去借书')

def main():
    print('*'*30,'欢迎进入图书系统','*'*30)
    islogin = False
    user_name = ''
    while True:
        n_select = input('\n请选择进入的功能序号：1 查看图书列表  2 登录  3 注册用户  4 借书  5 还书  q退出\n')
        # 展示现存图书
        if n_select == '1':
            show_book()
            continue
        # 登陆
        elif n_select == '2':
            user_name = login()  # 接收返回的用户信息
            if user_name: # 如果登陆成功，则标记islogin
                islogin = True
            continue
        # 用户注册
        elif n_select == '3':
            regist()
            islogin = False
            continue
        # 借书
        elif n_select == '4':
            if not islogin: # 如果没登录则 提示登陆
                print('请登陆后再借书！')
                continue
            borrow_book(user_name)
            continue
        # 还书
        elif n_select == '5':
            if not islogin:
                print('请登陆后再还书！')
                continue
            return_book(user_name)
            continue
        elif n_select == 'q':
            break
        else:
            print('请选择正确的序号！')

if __name__ == "__main__":
    main()