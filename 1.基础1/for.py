# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/21 0021

# a = ['susu','momo','lili','lucy','Cici']

#当遍历一个序列时，使用enumerate()函数可以同时得到位置索引和对应的值。
# for i,v in enumerate(a):
#     print(i,v)


#同时遍历两个或更多的序列，使用zip()函数可以成对读取元素。
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
#
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))

#要反向遍历一个序列，首先正向生成这个序列，然后调用reversed()函数。
# for i in reversed(range(1, 10, 2)):
#     print(i,end=' ')

#要按顺序循环一个序列，请使用sorted()函数，返回一个新的排序的列表，同时保留源不变。
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']   #os:set集合去重复
# for i in sorted(set(basket)):
#     print(i)

#如果在遍历列表的时候同时想改变它，创建一个新的列表会更简单更安全。
import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)

#打印三角形

# for i in range(10):
#     for a in range(i):
#         print('*',end=" ")
#
#     for b in range(i,10):
#         print('#',end=' ')
#     print('')


for i in range(10):
    for j in range(0,10-i):
        print(end=' ')
    for k in range(10-i,10):
        print('*',end=' ')
    print('')


for i in range(10):
    for j in range(0,i):
        print(end=" ")

    for j in range(i,10):
        print("$", end=" ")

    print("")