# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/16 0016

# print('''\
# Usage:thingy[OPTHONS]
#     -h                  Display this usage message
#     -H hostname         Hostname to connnect to
# ''')
#
# word='Python'
# print(word[0:4])
# print(word[4: ])
# print(word[-2:])
# words=['wwwwwwwwwwwww','cat','window','defenestrate']
# for w in words[:]:
#     if len(w)>6:
#         words.insert(2,w)
# print(words)

# a = ['Mary','had','a','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])
# print(list(range(2,10)))

# import re
# a='<span id="stock_quoteinfo_zde" class="green" >-0.29</span>&nbsp;&nbsp;<span id="stock_quoteinfo_zdf" class="green">(-1.45%)</span>'
#
# ret=re.findall('[-]?[\d]+[.]?[\d]+[%]?',a)
# print(ret)

# def fib(n):
#     result=[]
#     a,b=0,1
#     while a<n:
#         result.append(a)
#         a,b=b,a+b
#     return result
#
# fib(100)

# mart=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# a=[[row[i] for row in mart] for i in range(4)]
# print(a)

# print(list(zip(*mart)))

# def fib(n):
#     a,b=0,1
#     while b<n:
#         print(b,end=' ')
#         a,b=b,a+b
#     # print()
# fib(100)

# def fib2(n):
#     result=[]
#     a,b=0,1
#     while b<n:
#         result.append(b)
#         a,b=b,a+b
#     return result
# print(fib2(100))
#
# import builtins
# a=dir(builtins)
# for i in a:
#     print(i)

# import sys
# for i in sys.argv:
#     print(i)
# a=sys.path
# print(a)
# print(dir(a))



# import random
# rint(random.choice(['吃鸡吃鸡！','吃个锤子！']))


# for i in range(10):
#     # print(i)
#     for a in range(i):
#         print('*',end='')
#     print('')

# class Foo:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#     def __str__(self):
#         return '%s：%s' % (self.name,self.age)
#
# obj = Foo('susu',18)
# print(obj)  # print(str(obj.name),str(obj.age))

# class NetworkError(RuntimeError):
#     def __init__(self,arg):
#         self.aargs=arg
#
# try:
#     raise NetworkError("Bad hostname")
# except NetworkError as e:
#     print(e.args)


# class Foo:
#
#     __v = None
#
#     @classmethod
#     def get_instance(cls):
#         if cls.__v:
#             return cls.__v
#         else:
#             cls.__v = Foo()
#             return cls.__v
#
#     def show(self,name):
#         self.name=name
# # 不要在使用 类()
# obj1 = Foo.get_instance()
# print(obj1)
# obj2 = Foo.get_instance()
# print(obj2)
# Foo.show(val='ssss')
# obj3 = Foo.get_instance()
# print(obj3)

# from datetime import date
#
# now = date.today()
# print(now)
#
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# import threading
#
# class mythreading(threading.Thread):
#     def run(self):
#         for i in range(1,5):
#             print(i)
#
# ma = mythreading()
# mb = mythreading()
# ma.start()
# mb.start()


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
#     ta = mythread()
#     ta.start()
#     ta.join()
#     print('main thread over')

# import threading,time
#
# def music(func):
#     for i in range(2):
#         print(time.ctime())
#         time.sleep(5)
#         print(func,time.ctime())
#
# def move(func):
#     for i in range(2):
#         print(time.ctime())
#         time.sleep(2)
#         print(func,time.ctime())
#
#
# threads = []
# t1 = threading.Thread(target=music,args=('七里香',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=('闻花未名',))
# threads.append(t2)
#
# print(threads)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()

# FTP服务器 pip3 install pyftpdlib

# from pyftpdlib.authorizers import DummyAuthorizer
# from pyftpdlib.handlers import FTPHandler
# from pyftpdlib.servers import FTPServer
#
# authorizer = DummyAuthorizer()
# authorizer.add_user('root','root','.',perm="elradfmw")
# handler = FTPHandler
# handler.authorizer = authorizer
# server = FTPServer(("192.168.1.2",21),handler)
# server.serve_forever()

# import pickle
#
# class School:
#     def __init__(self,name):
#         self.name = name
#
#     def save(self):
#         f=open('xxxx','wb')
#         pickle.dump(self,f)
#         f.close()
#
# s1 = School('shanghai')
# s1.save()
#
# s2 = School('beijing')
# s2.save()
# import uuid
# print(uuid.uuid1())
# print(uuid.uuid1())

# import time
#
# print(time.ctime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# p = Point(32,11)
# print(p.x)
# print(p.y)
#
# a = ['a','b','c']
# from collections import deque
# q = deque(a)
# q.append('x')
# q.appendleft('y')
# print(q)

a = "cmd|ifconfig"
print(a.split('|')[1])
print(a.split('|',1))