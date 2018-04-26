# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/15 0015
# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;
# key必须为字符串，而值可以是python所支持的数据类型
import shelve

f = shelve.open(r'shelve_test')
f.close()

# 添加内容
# f['info']={'name':'susu','age':'18'}

# 读取内容
# print(f.get('info'))
# print(f.get('info')['name'])