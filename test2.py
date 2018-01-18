#coding:utf8
# _author: Administrator
# Date: 2018/1/15 0015

from multiprocessing import Process,Queue

def f(q,n):
    q.put([42,n,'hello'])
    print('subprocess id:',id(q))


if __name__ == '__main__':
    q = Queue()
    p_list=[]
    print('main q id:',id(q))
    for i in range(3):
        p = Process(target=f,args=(q,i))
        p_list.append(p)
        p.start()

    print(q.get())
    print(q.get())
    print(q.get())
    for i in p_list:
        i.join()