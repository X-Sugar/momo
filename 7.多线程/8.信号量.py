# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2018/1/3 0003

import threading,time

class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()

if __name__ == '__main__':
    semaphore=threading.Semaphore(5)
    thrs=[]
    for i in range(23):
        thrs.append(MyThread())
    for t in thrs:
        t.start()