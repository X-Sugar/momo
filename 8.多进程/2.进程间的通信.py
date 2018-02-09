#coding:utf8
# _author: Administrator
# Date: 2018/1/18 0018

# 不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法：

# Queues

# 使用方法跟threading里的queue类似：

# from multiprocessing import Process, Queue
#
# def f(q,n):
#     q.put([42, n, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p_list=[]
#     for i in range(3):
#         p = Process(target=f, args=(q,i))
#         p_list.append(p)
#         p.start()
#
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     for i in p_list:
#             i.join()

# Pipes
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()