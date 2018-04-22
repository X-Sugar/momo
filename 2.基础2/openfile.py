# -*- coding=utf-8 -*-

# f = open('江城子','rb') # rb 以二进制的方式打开文件，b方式不能指定编码
# data = f.read()
# print(data.decode('utf8'))

# --------------read()和readline()以及readlines()用法区别 --------------

# .read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中
# .readlines() 一次读取整个文件（类似于 .read()
# .readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理.
# .readline() 每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。

# --------------------------------------------------------------------------

# with open('江城子2','a',encoding='utf8') as g:
#     g.truncate(2)
##################################################################
# import sys,time
# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(0.1)
##################################################################

# with open('江城子','r',encoding='utf8') as  f,open('江城子2','w',encoding='utf8') as g:
#     num=0
#     for i in f:
#         num+=1
#         if num == 2:
#
#            i=''.join([i.strip(),'uuuuuuuuuuu\n'])
#         g.write(i)
##################################################################

# with open('江城子', 'r', encoding='utf8') as  f, open('江城子2', 'w', encoding='utf8') as g:
#     num = 0
#     for i in f:
#         num += 1
#         if num == 2:
#             i = 'sdfasdfasdfas\n'
#         g.write(i)
##################################################################

# with open('江城子', 'r', encoding='utf8') as  f:
#     print(f.read(6))
##################################################################

# with open('江城子', 'r', encoding='utf8') as  f:
#     num=0
#     for i in f:
#         num += 1
#         if num == 6:
#             i = ''.join([i.strip(),'11111111111'])
#             # print(i.strip())
#         print(i.strip())
##################################################################
# with open('江城子', 'r', encoding='utf8') as  f:
#     for i in f.readlines():
#         print(i.strip())
##################################################################
# with open('江城子', 'r', encoding='utf8') as  f:
#     num = 0
#     for i in f.readlines():
#         num += 1
#         if num == 8:
#             i = ''.join([i.strip(),'*********'])    #建议的字符串拼接，取代万恶的+
#         print(i.strip())
##################################################################
# with open('江城子', 'r', encoding='utf8') as  f:
#     for i in f:
#         print(i.strip())
#
#     print(f.tell())
#     print(f.read(4)) #中文占三个
#     print(f.tell())
#     print(f.seek(3))
#     print(f.read(4))
#     print(f.flush())
#     print(f.tell())
##################################################################

# import sys,time
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.1)

# import time
# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(0.1)

# f_read = open('江城子','r',encoding='utf8')
# f_write = open('江城子2','w',encoding='utf8')
#
# num = 0
# for i in f_read:
#     num += 1
#     if num == 5:
#         i = ''.join([i.strip(),'Sususususuuuu\n'])
#     f_write.write(i)

# with open('江城子','r',encoding='utf8') as f_read,open('江城子2','w',encoding='utf8') as f_write:
#     for line in f_read:
#         f_write.write(line)
# # f = open()

# seek
# with open('江城子','r',encoding='utf8') as f:
#     f.seek(9)
#     print(f.readline())
