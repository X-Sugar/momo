# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/25 0025

# s=(x for x in range(1,11))

# print(next(s)) #print(s.__next__()) #特殊方式，不建议使用。
# print(next(s))
# print(next(s))

#生成器就是一个可迭代对象（）iterable

# for i in s:
#     print(i,end=" ")

# def foo():
#     print('OK')
#     yield 1
#
# g=foo()
# print(foo())
#
# next(g)

# 0 1 1 2 3 5 8 13 21 34
# def fib(max):
#     n,before,after=0,0,1
#     while n < max:
#         print(after)
#         before,after=after,before+after
#         n = n + 1
#
# fib(8)

# 0 1 1 2 3 5 8 13 21 34
# def fib(max):
#     n,before,after=0,0,1
#     while n < max:
#         yield before
#         before,after=after,before+after
#         n = n + 1
#
# b=[ x for x in fib(8)]
# print(b)

# def old():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
# b=old()
# b.send(None)
# b.send('sd')