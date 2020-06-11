from multiprocessing import Process
import os
from time import sleep
def task1(s,arg1):
    while True:
        sleep(s)
        print('---任务1---',os.getpid(),'------',os.getppid(),arg1)
def task2(s,arg1):
    while True:
        sleep(s)
        print('---任务2---',os.getpid(),'------',os.getppid(),arg1)

if __name__ == "__main__":
    p1 = Process(target=task1,name ='任务1',args=(1,'任务1')) #可以给进程传参
    p1.start() # dhhh
    p2 = Process(target=task2,name='任务2',args=(2,'任务2'))
    p2.start()