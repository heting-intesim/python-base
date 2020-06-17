# 打印棋盘
def show(data):
    n = len(data)
    for i in data:
        for j in range(n):
            if j == i:
                print('+ ',end='')
            else:
                print('- ',end='')
        print('')
# 计算可能的棋盘布局
def huang(m,n,b):
    if m == 1:
        for i in range(n):
            if i not in b:
                b.append(i)
                res.append(b)
            else:
                continue
    else:
        for j in range(n):
            if j not in b:
                c = b + [j]
                huang(m-1,n,c)
            else:
                continue

res = []
huang(5,5,[])
i_res = iter(res)
while True:
    if input('显示下一个布局？[按回车继续][按Ctrl+c结束]') == '':
        try:
            r = next(i_res)
            print(r)
            show(r)
        except:
            print(f'已全部显示完毕，共 {len(res)} 种布局方案！')
            break