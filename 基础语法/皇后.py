import time
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

# res = []
# # t1 = time.time()
# huang(4,4,[])
# t2 = time.time()
# print(res,'总数：',len(res))
# print('runnint TIME:',t2-t1)


def huang2(m,n,b):
    global sum
    if m == 1:
        for i in range(n):
            for k,v in enumerate(b):
                if i == v or abs(k-len(b)) == abs(v-i):
                    break
            else:
                # b.append(i)
                # print(b)
                # res.append(b)
                sum += 1
    else:
        for j in range(n):
            if len(b) == 0:
                c = b + [j]
                huang2(m-1,n,c)
            else:
                for k,v in enumerate(b):
                    if j == v or abs(k-len(b)) == abs(v-j):
                        break
                else:
                    c = b + [j]
                    huang2(m-1,n,c)
# res = []
# sum = 0
# n = 15
# huang2(n,n,[]) 
# print(sum)
# print(f'{n}皇后问题存在{len(res)}种布局方案')
# # 用迭代器逐个显示棋盘
# i_res = iter(res)
# while True:
#     if input('显示下一个布局？[按回车继续][按Ctrl+c结束]') == '':
#         try:
#             r = next(i_res)
#             print(r)
#             show(r)
#         except:
#             print(f'已全部显示完毕，共 {len(res)} 种布局方案！')
#             break

# 标准答案
def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur+1)
queen([None]*8)