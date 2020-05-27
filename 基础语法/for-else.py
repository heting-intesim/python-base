for i in range(5):
    if i == 2:
        print('出问题了~~')
        break
    else:
        print('不错不错')
else: # 只有当for顺利执行完毕，而没有break时，才会执行else 之后的语句！  
    print('很好！') # 一旦break，本句就不执行
print('End')