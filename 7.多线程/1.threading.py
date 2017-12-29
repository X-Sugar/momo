# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/26 0026

# 线程是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。
# 一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不通的任务

import time,threading

def foo(n):
    print('foo')
    time.sleep(1)
    print('%s' % n)

def bar(n):
    print('bar')
    time.sleep(2)
    print('%s' % n)

if __name__ == '__main__':

    start=time.time()
    # foo()
    # bar()
    t1 = threading.Thread(target=foo,args=(1,))     # 创建一个线程，执行foo()
    t2 = threading.Thread(target=bar,args=(2,))     # 创建一个线程，执行bar()

    t1.start()      # 调用start()，运行线程
    t2.start()      # 调用start()，运行线程

    end = time.time()

    print(end-start)