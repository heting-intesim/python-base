import threading,time,random
lock = threading.Lock()
ticktes = 100
def task(name):
    global ticktes
    while True:
        lock.acquire()
        if ticktes <= 0:
            break
        else:
            print(f'{name}窗口出票成功，票号：{ticktes}')
            ticktes -= 1
            lock.release()
            time.sleep(random.random())
    lock.release()

if __name__ == "__main__":
    ts = []
    for i in range(1,6):
        ts.append(threading.Thread(target=task,args=(str(i),)))
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print('--------end-------')