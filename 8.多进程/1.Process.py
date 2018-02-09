# -*- coding:utf-8 -*-
# _author: Administrator
# Date: 2018/1/15 0015

# 只适合Unix
# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# -----------------------------------------------------------

# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# -----------------------------------------------------------

# import os
#
# from multiprocessing import Process
#
# class Proc(Process):
#     def __init__(self,name):
#         Process.__init__(self)
#         self.name=name
#     def run(self):
#         print('Run child process %s (%s)...' % (self.name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Proc('test')
#     print('Child process will start.')
#     p.start()
#     p.join()    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     print('Child process end.')

# -----------------------------------------------------------
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

# from multiprocessing import Pool
# import os,time,random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name,(end-start)))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')
# -----------------------------------------------------------

# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

# -----------------------------------------------------------

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()