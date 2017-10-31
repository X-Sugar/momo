# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/20 0020

#装饰器
import time

def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend %s' % (start - end))
    return  inner

@show_time  #foo=show_time(foo)
def foo():
    print('foo.......')
    time.sleep(2)
foo()

@show_time
def bar():
    print('bar......')
    time.sleep(3)


bar()

