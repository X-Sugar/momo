# -*- coding=utf-8 -*-

# 闭包函数

# def outer():
#     x=10
#     def inner():    #条件1：内部函数
#         print(x)    #条件2：引用外部变量
#     return inner
#
# f=outer()
# f()

# 装饰器
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

# 装饰带参数

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

# 多个参数

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

# 装饰器加参数

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

# a=[lambda :x for x in range(10)]
# print(a[0]())

# a = 3
# b = [a + i for i in range(10)]
# print(b)


# -----------------------不定长参数------------------------
# *args:接收N个位置参数，转换成元组形式

# def test(*args):
#     print(args)
#
# test(1,2,3,4,5)
# test(*[1,2,3,4,5])
# 执行时args = tuple([1,2,3,4,5])

# def test1(x,*args):
#     print(x)
#     print(args)
#
# test1(1,2,3,4,5,6,7)

# **kwargs:接收N个关键字参数，转换成字典方式

# def test2(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#     print(kwargs['sex'])
#
# test2(name='alex', age=8, sex='male')
# test2(**{'name':'alex', 'age':'22', 'sex':'male'})

# def test3(name, **kwargs):
#     print(name)
#     print(kwargs)
#
# test3('alex',age=8, sex='male')

def test4(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger('TEST4')

def logger(source):
    print('from %s' % source)

test4('alex', age=34, sex='male',hobby='tesla')