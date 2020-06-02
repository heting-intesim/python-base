import os
# stream = open('E:\\gitPYTHON\\基础语法\\1.txt','rt',encoding='utf-8')
# print(type(stream))  # open 返回一个 数据流【管道】  _io.TextIOWrapper
# cont = stream.read()
# print(cont)

# with open('E:\\gitPYTHON\\基础语法\\1.txt','rt',encoding='utf-8') as file:
#     cont = file.readline()
#     print(cont)
#     conts = file.readlines()  # 将每一行数据放入列表，行末加上\n
#     print(conts)

# with open(r'E:\gitPYTHON\基础语法\1.txt','r',encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)

# s = 'hello world'
# with open(r'E:\gitPYTHON\基础语法\1.txt','a',encoding='utf-8') as file:
#     file.write(s)
#     file.write('\ntian cai\n')

# 复制文件
# with open(r'E:\gitPYTHON\基础语法\2.txt', 'wb') as file1:
#     with open(r'E:\gitPYTHON\基础语法\1.txt', 'rb') as file2:
#         while True:
#             line = file2.readline()
#             file1.write(line)
#             if not line:
#                 break
p = os.path.dirname(__file__)
print(p)
print(1)
print(os.getcwd())
print(2)
print(os.path.abspath(__file__))
print(3)
print(os.path.abspath('1.txt'))