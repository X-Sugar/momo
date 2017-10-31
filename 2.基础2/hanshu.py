# -*- coding=utf-8 -*-

#闭包函数

# def outer():
#     x=10
#     def inner():    #条件1：内部函数
#         print(x)    #条件2：引用外部变量
#     return inner
#
# f=outer()
# f()

#装饰器
# import time
# def show_time(f):
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print('spend %s' % (start - end))
#     return  inner
#
# @show_time
# def foo():
#     print('emmmmmm.........')
#     time.sleep(2)
# foo()

#装饰起带参数

# import time
# def show_time(f):
#     def inner(x,y):
#         start = time.time()
#         f(x,y)
#         end = time.time()
#         print('spend %s' % (start - end))
#     return  inner
# @show_time
# def foo(x,y):
#     print(x+y)
#     time.sleep(1)
# foo(2,3)

#多个参数

# import time
# def show_time(f):
#     def inner(*x,**y):
#         start = time.time()
#         f(*x,**y)
#         end = time.time()
#         print('spend %s' % (start - end))
#     return  inner
# @show_time
# def foo(*x,**y):
#     nums=0
#     for i in x:
#         nums+=i
#     print(nums)
#     time.sleep(1)
# foo(2,3,4)

#装饰器加参数

# import time
# def logger(flag):
#     def show_time(f):
#         def inner(*x,**y):
#             start = time.time()
#             f(*x,**y)
#             end = time.time()
#             print('spend %s' % (start - end))
#             if flag=='true':
#                 print('日志记录')
#         return  inner
#     return show_time
# @logger('true')
# def foo(*x,**y):
#     nums=0
#     for i in x:
#         nums+=i
#     print(nums)
#     time.sleep(1)
# foo(1,5,7,8)

# a = 12
# def outer():
#     a = 10
#     def inner():
#         nonlocal a
#         print(a)
#         # a = 2
#         # print(a)
#     inner()
#
# outer()


# name = "lzl"
#
# def f1():
#     print(name)
# def f2():
#     name = "eric"
#     return f1
#
# ret = f2()
# ret()


# for i in range(10):
#     print(i)
#
# print(i)

a=[lambda :x for x in range(10)]
print(a[0]())

# a = 3
# b = [a + i for i in range(10)]
# print(b)
