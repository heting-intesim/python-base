'''
闭包形成的条件：
1 存在内定义函数，并且内函数中调用外函数变量
2 外函数返回内函数的名称
3 执行一次外函数，并将返回值赋值到一个函数变量

4 装饰器是一种闭包的特殊应用！！！
'''
def fnAdd():
    count = 0
    def fn():
        nonlocal count
        count += 1
        return count
    return fn

add = fnAdd()
add()
add()