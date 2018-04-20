# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/20 0020

# 装饰器    增强函数功能，但又不希望改变函数的定义。
# 装饰器本身有参数
# 装饰有返回值的函数

import time

def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend %s' % (start - end))
    return inner

@show_time
# foo=show_time(foo)
def foo():
    print('foo.......')
    time.sleep(2)
foo()

# @show_time
# def bar():
#     print('bar......')
#     time.sleep(3)
# bar()


# # ######################################################
# def aa(cc):
#     def dd():
#         print('xxxxxxxxxx')
#         cc()
#     return dd
# @aa
# def bb():
#     print('--------------')
# bb()
# # #####################################################
# def printdebug(func):
#     def __decorator(user):  # add parameter receive the user information
#         print('enter the login')
#         func(user)  # pass user to login
#         print('exit the login')
#     return __decorator
#
# @printdebug
# def login(user):
#     print('in login:' + user)
# login('jatsz')