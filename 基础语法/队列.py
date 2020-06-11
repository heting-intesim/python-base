# from multiprocessing import Queue
# q1 = Queue(5)
# for i in 'abcde':
#     q1.put(i,block=False,timeout=2) # 一旦队列满，后续会等待timeout时间，还是满的则put会报Full的错误
#     print(i)
# for i in range(6):
#     print(q1.get(block=True,timeout=2)) # 一旦队列为空，后续会等待，还是为空则报Empty错误


# 进程间通信
from multiprocessing import Queue,Process
from time import sleep
def download(q):
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    for i in images:
        print(f'正在下载 {i}')
        sleep(0.5)
        q.put(i)

def storeFile(q):
    while True:
        try:
            print(f'已保存 {q.get(timeout=3)}')  # 等待3s后还取不到值则表明下载任务已经完成！，会报错，在被except捕获
        except:
            print('全部保存完毕')
            break

if __name__ == "__main__":
    q = Queue(3)
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=storeFile,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('-----end-----')