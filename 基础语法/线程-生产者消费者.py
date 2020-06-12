import queue,threading,time
def productor(q):
    for n in range(10):
        q.put(n)
        print(f'生产产品号：{n}')
        time.sleep(0.5)
    q.task_done()
def consumer(q):
    for n in range(15):
        try:
            p = q.get(timeout=2)
        except:
            break
        print(f'消费产品号：{p}')
        time.sleep(0.5)
    q.task_done()  # 结束队列任务获取， 此处可以用try 方式捕获 get(timeout=3)的错误，从而判断无数据可获取

if __name__ == "__main__":
    q = queue.Queue(5)  # 创建一个队列，将其作为参数传入生产者和消费者函数
    t1 = threading.Thread(target=productor,args=(q,))
    t2 = threading.Thread(target=consumer,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('----------end----------')