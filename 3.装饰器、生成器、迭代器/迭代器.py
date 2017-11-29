# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/27 0027

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。

# 字符串，列表或元组对象都可用于创建迭代器：

# list=[1,2,3,4]
# it=iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# 迭代器对象可以使用常规for语句进行遍历：

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# 也可以使用 next() 函数：
import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()