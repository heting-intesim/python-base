# input('输入提示：')
# print(f'{}')  最简便格式化输出方式{}内部链接变量名:.2f  【右对齐占10格】x:>10  【占10格居中对齐】x:^10
persons = []
for i in range(5):
    i = {'name':input('姓名:'),'age':input('年龄:')}
    persons.append(i)
for i in persons:
    print(f"姓名：{i['name']}\t  年龄：{i['age']}")
print(persons)

# name = input("请输入姓名：")
# age = input("请输入年龄：")
# print(f'姓名：{name}\t年龄：{age:.2f}')