# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/27 0027

# 当一个进程拥有多个线程之后，如果他们各做各的任务互没有关系还行，但既然属于同一个进程，他们之间总是具有一定关系的。
# 比如多个线程都要对某个数据进行修改，则可能会出现不可预料的结果。为保证操作正确，就需要引入锁来进行线程间的同步。
# python3 中的 threading 模块提供了 RLock锁(可重入锁)。
# 对于某一时间只能让一个线程操作的语句放到 RLock的acquire 方法 和 release方法之间。
# 即 acquire()方法相当于给RLock 锁  上锁，而 release() 相当于解锁。

import threading,time

x = 0
lock = threading.RLock()

class mythread(threading.Thread):
    def run(self):
        global x    # 声明一个全局变量
        lock.acquire()  # 上锁，acquire()和release()之间的语句一次只能有一个线程进入，其余线程在acquire()处等待
        x += 10
        print(self.name,x)
        lock.release()  # 解锁

def main():
    l = []
    for i in range(5):
        l.append(mythread())    # 创建 5 个线程，并把他们放到一个列表中
    for i in l:
        i.start()   # 开启列表中的所有线程
if __name__ == '__main__':
    main()