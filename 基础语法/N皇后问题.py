# 二皇后问题，pan[1][1] 
# 递归方式
# 每组个位、十位上的数不重复，abs(各位-各位) == abs(十位-十位)
import time
def queen(m,n,b):
    if m == 1:
        for i in range(n):
            for k,v in enumerate(b):
                if i == v or abs(k-len(b)) == abs(v-i):
                    break
            else:
                b.append(i)
                res.append(b)
    else:
        for j in range(n):
            if len(b) == 0:
                c = b + [j]
                queen(m-1,n,c)
            else:
                for k,v in enumerate(b):
                    if j == v or abs(k-len(b)) == abs(v-j):
                        break
                else:
                    c = b + [j]
                    queen(m-1,n,c)
def queen2(m,n,b):
    if m == 1:
        num = (set(range(n))-set(b)).pop()
        for k,v in enumerate(b):
            if num == v or abs(k-len(b)) == abs(v-num):
                break
        else:
            c = b.append(num)
            res.append(c)
    else:
        set_surplus = set(range(n))-set(b)
        for j in set_surplus:
            if len(b) == 0:
                c = b + [j]
                queen2(m-1,n,c)
            else:
                for k,v in enumerate(b):
                    if j == v or abs(k-len(b)) == abs(v-j):
                        break
                else:
                    c = b + [j]
                    queen2(m-1,n,c)
# 网络标准解决方案
def queen0(A, cur=0):
    if cur == len(A):
        # print(A)
        res.append(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen0(A, cur+1)

res = []
t1 = time.time()
queen(10,10,[])
t2 = time.time()
print('原queen TIME:',t2-t1)
print(len(res))

res = []
t1 = time.time()
queen0([None]*10)
t2 = time.time()
print('标准queen0 TIME:',t2-t1)
print(len(res))

res = []
t1 = time.time()
queen2(10,10,[])
t2 = time.time()
print('优化queen2 TIME:',t2-t1)
print(len(res))
