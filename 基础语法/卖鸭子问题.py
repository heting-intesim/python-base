'''
一个人赶着鸭子去每个村庄卖，每经过一个村子卖去所赶鸭子的一半又一只。
这样他经过了七个村子后还剩两只鸭子，
问他出发时共赶多少只鸭子？经过每个村子卖出多少只鸭子？
'''
# 递归体为：  rest(n) = (rest(n+1)+1)*2
def rest(n):
    if n == 7:
        print('经过第7个村庄后时剩余2只')
        return 2
    else:
        rn1 = rest(n+1)
        r = (rn1+1)*2
        if n==0:
            print(f'原有{r}只鸭子')
            print(f'经过第1个村转后，卖掉')
        else:
            print(f'经过第{n}个村庄后，卖掉{r-rn1}只，剩余{r}只鸭子！')
        return r

rest(0)