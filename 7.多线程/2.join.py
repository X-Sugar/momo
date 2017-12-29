# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/27 0027

# join()作用是 调用 join() 的线程 阻塞直到 某一线程结束才继续执行
# 我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，
# 即它调用了线程的 run() 方法：

# import threading,time
#
# class mythread(threading.Thread):
#     def run(self):
#         self.i = 1
#         print(self.i)
#         self.i = self.i + 1
#         time.sleep(1)
#         print(self.i)
#         time.sleep(1)
#
# if __name__=='__main__':
#     ta = mythread()     # 实例化线程
#     ta.start()      # 开启ta线程
#     ta.join()       # 主线程等待 ta线程结束才继续执行
#     print('main thread over')


import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")