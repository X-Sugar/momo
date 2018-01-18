#coding:utf8
# _author: Administrator
# Date: 2018/1/17 0017

# window系统下，需要注意的是要想启动一个子进程，
# 必须加上那句if __name__ == "main"，进程相关的要写在这句下面。

# from multiprocessing import Process
#
# import time
#
# def f(name):
#     time.sleep(1)
#     print('Hello!',name,time.ctime())
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = Process(target=f,args=('susu',))
#         p_list.append(p)
#         p.start()
#
#     for p in p_list:
#         p.join()
#     print('End!')

# ---------------------------------------------------------
# 类式调用

# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self):
#         # super(MyProcess,self).__init__()
#         Process.__init__(self)
#
#     def run(self):
#         time.sleep(1)
#         print('Hello!',self.name,time.ctime())
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = MyProcess()
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()
#
#     print('End')

# ----------------------------------------------------------------

# from multiprocessing import Process
# import os,time
#
# def info(title):
#     print(title)
#     print('module name:',__name__)
#     print('parent process:',os.getppid())   # ppid父进程号
#     print('process id:',os.getpid())    # pid子进程号
#
#
# def f(name):
#     info('\033[31;1mfunction f\033[0m')
#     print('hello',name)
#
# if __name__ == '__main__':
#     info('\033[32;1m main process line \033[0m')
#     time.sleep(3)
#     p = Process(target=info,args=('bob',))
#     p.start()
#     p.join()

# -------------------------------------------------------

