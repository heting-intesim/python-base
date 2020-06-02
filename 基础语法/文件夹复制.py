import os
# 复制文件夹
# path1 = os.path.dirname(__file__)  # 返回当前文件所在的文件夹 全路径
# folderName = path1[path1.rfind('\\')+1:]   # 获取当前文件夹的名字  切片方式
# dirNew = 'd:\\tttt\\'+folderName   # 定义要粘贴文件夹的位置，并加上被复制文件夹的名称，方便下一步创建新文件夹
# os.makedirs(dirNew) # 创建多层目录必须要用makedirs   单级目录用 mkdir()
# for f in os.listdir(path1):
#     with open(os.path.join(path1,f),'rb') as f0:   # os.path.join() 专门用于连接路径与文件名
#         content = f0.read()
#         with open(os.path.join(dirNew,f), 'wb') as f1:
#             f1.write(content)


# 删除文件夹  【首先删除文件夹下所有文件，才能删除文件夹】
path = r'd:\temple\files'  # 指定要删除的文件夹
files = os.listdir(path)  # 列出文件夹下所有的文件
print(files)
for f in files:
    os.remove(os.path.join(path,f))
else:
    os.rmdir(path)
    print('删除完毕！')