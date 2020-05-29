# 以产品质量检查为例，一批产品中一旦出现一个不合格品，则判定此批产品报废； 全部通过检查则判定此批产品合格
p = [1, 1, 0, 1, 1]
for i in p:
    if i == 0:
        print('发现不合格品，判定 此批产品报废！')
        break
    else:
        print('这件产品合格')
else: # 只有当for顺利执行完毕，而没有break时，才会执行else 之后的语句！  
    print('---此批产品合格！---') # 一旦break，本句就不执行
print('End')

#登录验证
for i in range(3):
    name = input('请输入用户名：')
    password = input('请输入密码：')
    if name!='zhao' or password!='123':
        print('输入错误！')
        continue
    print('欢迎 zhao')
    break
else:     #此句之后的语句只有当for结构不在循环中break，才会执行；  一旦break此句不执行！！
    print('输入错次数已达上限，强制退出')