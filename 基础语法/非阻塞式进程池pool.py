# 非阻塞式进程池
from multiprocessing import Pool
from time import sleep,time
from random import random
import os

# def task(name):
#     print('开始做任务---', name,'进程ID为',os.getpid())
#     start = time()
#     sleep(random()*2)
#     end = time()
#     # print(f'任务 {name} 完成---用时 {end-start} 秒','进程id为',os.getpid())
#     return f'任务--{name}完成,用时{end-start}秒,进程id为{os.getpid()}'

# container = []
# def callback_func(str_return):  # 定义回调函数，负责对每次任务返回的信息进行处理。 此处将放回的字符串逐一存到到container中。
#     container.append(str_return)

# if __name__ == "__main__":
#     pool = Pool(3)

#     tasks = ['数学','语文','英语','物理','化学','生物','计算机']
#     for t in tasks:
#         pool.apply_async(task,args=(t,),callback=callback_func) # args接受任务的参数，用元组形式； callback接收回调函数名
    
#     pool.close() # 进程池关闭，不再接受新进程进入
#     pool.join()  # 手动阻塞主进程，否则主进程一结束，pool中的子进程马上结束！
#     for i in container:
#         print(i)
#     print('--------end--------')


# -----------------------------------------------------------------------------------------
# 阻塞式进程池
def task(name):
    print('开始做任务---', name,'进程ID为',os.getpid())
    start = time()
    sleep(random()*2)
    end = time()
    print(f'任务 {name} 完成---用时 {end-start} 秒','进程id为',os.getpid())

if __name__ == "__main__":
    pool = Pool(3)  # 创建进程池，指定最大进程数
    tasks = ['数学','语文','英语','物理','化学','生物','计算机']
    for t in tasks:
        pool.apply(task,args=(t,)) # args接受任务的参数，用元组形式； 无callback回调函数

    print('--------end--------')