# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/27 0027

# 列表生成式
# [x*2 for x in range(10)]

# 生成器 （generator object）

    # 创建生成器两种方式
    # 第一种
# (x*2 for x in range(10))
    # 第二种
# def f():
#     yield
# f()   #这个就是生成器

    # 生成器调用方法

# 第一种
# next(f()) #计算出一个值
        # 注意：生成器在创建的时候已经决定了能计算的个数，超出则报错StopIteration
        # 遍历所有元素可以for循环
# for i in [1,2,3]:
#     print(i)

#for 循环内部做了三件事
#   1.调用对象iter()方法，返回一个迭代器对象
#   2. while:
#           i=next(list_Iterator)
#   3.捕捉错误
# while:
#     try:
#         i=next(list_Iterator)
#
#     except StopIteration
#         break

#第二种
#   send():

# def x():
#     recv=yield 2
#     print('OK!')
# x().send(None)  #等同于next(f())

#send() 给recv传参数


#迭代器
# 满足迭代器协议：
#     1.内部有next方法
#     2.内部有iter()方法

# lit=[1,2,3]
# for i in iter(lit):
#     print(i)

# a = [1,2,3,4]
# b=iter(a)   #b就是一个迭代器对象