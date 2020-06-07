import os
class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []
    # 借书
    def borrow_book(self,book,bookbase):
        if book in self.books:
            print('此书你已经借过了')
        else:
            bookbase.jie(book,self)
            self.books.append(book.name)
            print(f'借书{book.name} 成功')
    # 还书
    def return_book(self, book, bookbase):
        if book.name not in self.books:
            print('此书你没有借过')
        else:
            bookbase.huan(book,self)
            self.books.remove(book.name)
            print(f'借书{book.name} 成功')

class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
    def __eq__(self, other): # 自定义 book对象相等的条件
        return self.__dict__ == other.__dict__
    def __str__(self):
        return self.name

class BookBase:
    def __init__(self):
        self.book_list = []
    def init_from_file(self, file):
        try:
            with open(file, 'r',encoding='utf-8') as file:
                lines = file.readlines()
        except Exception as err:
                print(err)
        for ln in lines:
            line = ln.strip().split(' ')
            sss = tuple(line[0][1:-1].split(','))
            b = Book(*sss)
            names = line[3][1:-2].split(',') if line[3][1:-2] else [] # 如果为[] ,则返回空数组
            dict0 = {'book_info':b, 'total_num':int(line[1]), 'surplus_num':int(line[2]), 'reader_names':names}
            self.book_list.append(dict0)
    def __str__(self):
        string0 = ''
        for b in self.book_list:
            string0 += f'书名：{str(b["book_info"])}， 总数：{b["total_num"]}本， 剩余：{b["surplus_num"]}本， 借阅者：{str(b["reader_names"])}\n'
        return string0
    # 新书上架
    def add_newbook(self, book, total_num):
        for b in self.book_list:
            if book.name == b['book_info'].name:
                print('此书已经在架上！')
                break
        else:
            dict0 = {'book_info':book, 'total_num':total_num, 'surplus_num':total_num, 'reader_names':[]}
            self.book_list.append(dict0)
            # 写入books2.txt文件
            p = os.path.dirname(__file__)
            with open(os.path.join(p,'books2.txt'),'w',encoding='utf-8') as file:
                for bk in self.book_list:
                    file.write(f'[{bk["book_info"].name},{bk["book_info"].author}] {bk["total_num"]} {bk["total_num"]} []\n')
            print(f'新书《{book.name}》上架成功!')
    # 旧书下架 
    def del_book(self, book):
        for b in self.book_list:
            if book.name == b['book_info'].name:
                self.book_list.remove(b)
                # 更新books2.txt文件
                p = os.path.dirname(__file__)
                with open(os.path.join(p,'books2.txt'),'w',encoding='utf-8') as file:
                    for bk in self.book_list:
                        file.write(f'[{bk["book_info"].name},{bk["book_info"].author}] {bk["total_num"]} {bk["total_num"]} []\n')
                print(f'旧书《{book.name}》下架成功！')
                break
        else:
            print('此书不在架上！')
    # 借书
    def jie(self, book, reader):
        # {'book_info':b, 'total_num':line[1], 'surplus_num':line[2], 'reader_names':names}
        for b in self.book_list:
            # if book in reader.books:
            #     print('此书你已经借过了！')
            #     break
            if b['surplus_num'] == 0:
                print('此书已被借完，请稍后再来！')
                break
            elif b['book_info'] == book:
                b['surplus_num'] -= 1
                b['reader_names'].append(reader.name)
                break
        else:
            print('没有此书！')
    # 还书
    def huan(self, book, reader):
        for b in self.book_list:
            if book.name not in reader.books:
                print('此书你没有借过了！')  # 商榷？？？？？
                break
            elif b['total_num'] == b['surplus_num']:
                print('此书不是从我馆借出的！')
                break
            elif b['book_info'] == book:
                b['surplus_num'] += 1
                b['reader_names'].remove(reader.name)
                break
        else:
            print('没有此书！')


bs = BookBase()
bs.init_from_file(r'E:\Learn\python-base\案例\librarysys\books2.txt')
print(bs)
# r0 = Reader('jack')
# b0 = Book('三国','罗贯中')
# r0.borrow_book(b0,bs)
# # b1 = Book('红楼梦','曹雪芹')
# print(bs)
# r0.return_book(b0, bs)
b2 = Book('三国','罗贯中')
bs.add_newbook(b2,5)
print(bs)


# 主函数
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

# if __name__ == "__main__":
#     main()
