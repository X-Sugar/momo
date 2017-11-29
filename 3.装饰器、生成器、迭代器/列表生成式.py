# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/25 0025

# a = [x for x in range(1,11)]
# print(a)

# a = [x*x for x in range(1,11)]
# print(a)

# def f(n):
#     return n**3
#
# a=[f(x) for x in range(10)]
# print(a)
# print(type(a))
#
#
# t=('susu',8,9)
# a,b,c=t
# print(a)
# print(b)
# print(c)

# b=[x*x for x in range(1,11) if x % 2 == 0]
# print(b)

# b=[m+n for m in 'ABC' for n in 'XYZ']
# print(b)

import os
b=[d for d in os.listdir('.')]
print(b)