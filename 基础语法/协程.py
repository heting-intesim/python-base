# 通过 第三方包 greenlet 方便实现协程【pip install greenlet】
# from greenlet import greenlet
# from time import sleep
# def funcA():
#     for i in range(5):
#         print('A'+str(i))
#         g2.switch()  # 定义切换目标
#         sleep(0.1)
# def funcB():
#     for i in range(5):
#         print('B'+str(i))
#         g3.switch() # 定义切换目标
#         sleep(0.1)
# def funcC():
#     for i in range(5):
#         print('C'+str(i))
#         g1.switch() # 定义切换目标
#         sleep(0.1)

# if __name__ == "__main__":
#     g1 = greenlet(funcA)
#     g2 = greenlet(funcB)
#     g3 = greenlet(funcC)
#     g1.switch()
#     g2.switch()
#     g3.switch()

import gevent
from gevent import monkey
from time import sleep
monkey.patch_all()   # 打上猴子补丁  保证底层协程自动切换。
def funcA():
    for i in range(5):
        print('A'+str(i))
        sleep(0.1)
def funcB():
    for i in range(5):
        print('B'+str(i))
        sleep(0.1)
def funcC():
    for i in range(5):
        print('C'+str(i))
        sleep(0.1)

if __name__ == "__main__":
    g1 = greenlet(funcA)
    g2 = greenlet(funcB)
    g3 = greenlet(funcC)
    g1.join()
    g2.join()
    g3.join()
    print('--------END-------')