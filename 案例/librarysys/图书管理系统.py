'''
图书管理系统
    1.查询图书
    2.增加图书
    3.借阅图书
    4.归还图书
    5.退出系统
'''
# 书：书名，作者，状态，位置
# 管理系统：
class Book(object):

    def __init__(self, name, author, status, bookindex):
        self.name = name
        self.author = author
        self.status = status
        self.bookindex = bookindex

    def __str__(self):
        if self.status == 1:
            stats = '未借出'
        elif self.status == 0:
            stats = '已借出'
        else:
            stats = '状态异常'
        return '书名: 《%s》 作者: %s 状态: <%s> 位置: %s' \
               % (self.name, self.author, stats, self.bookindex)


class BookManage(object):
    books = []

    def start(self):
        self.books.append(Book('python', 'guido', 1, 'ISO9001'))
        self.books.append(Book('c', '谭浩强', 1, 'NFS8102'))
        self.books.append(Book('java', 'westos', 1, 'PKA7844'))
        # 0:借出 1：存在
        # python 1
        # c 1
        # java 1

    def Menu(self):
        self.start()
        while True:
            print("""
                        图书管理系统
        1.查询图书
        2.增加图书
        3.借阅图书
        4.归还图书
        5.退出系统
        """)

            choice = input('请选择：')

            if choice == '1':
                self.showAllBook()
            elif choice == '2':
                self.addBook()
            elif choice == '3':
                self.borrowBook()
            elif choice == '4':
                self.returnBook()
            elif choice == '5':
                print('欢迎下次使用...')
                exit()
            else:
                print('请输入正确选择')
                continue

    def showAllBook(self):
        for book in self.books:
            print(book)

    def addBook(self):
        name = input('图书名称:')
        self.books.append(Book(name, input('作者:'), 1, input('存储位置:')))
        print('图书《%s》增加成功' % name)

    def checkBook(self, name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None

    def borrowBook(self):
        name = input('借阅图书名称: ')
        ret = self.checkBook(name)
        print(ret)

        if ret != None:
            if ret.status == 0:
                print('书籍《%s》已经借出' % name)
            else:
                ret.status = 0
                print('书籍《%s》借阅成功' % name)
        else:
            print('书籍《%s》不存在' % name)

    def returnBook(self):
        name = input('归还图书名称:')
        ret = self.checkBook(name)

        if ret != None:
            if ret.status == 0:
                ret.status = 1
                print('书籍《%s》归还成功' % name)
                print(ret)
            else:
                print('书籍《%s》未借出' % name)
        else:
            print('书籍《%s》不存在' % name)

manager = BookManage()
manager.Menu()