# 自定义进程
from multiprocessing import Process
from time import sleep

class MyProcess(Process):
    def __init__(self, name, s):  # 自定义要传递的参数！
        super(MyProcess, self).__init__()
        self.name = name
        self.s = s

    # 重写run方法
    def run(self):
        n = 1
        while True:
            print(f'进程：{self.name}---->n: {n}')
            sleep(self.s)  # 使用传进来的参数
            n += 1

if __name__ == "__main__":
    p1 = MyProcess('进程1',1) # 创建自定义进程，并传递参数
    p2 = MyProcess('进程2',2)
    p1.start()  # 开始执行进程
    p2.start()