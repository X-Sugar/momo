# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/15 0015

import shelve

f=shelve.open(r'shelve_test')

# f['info']={'name':'susu','age':'18'}


# data=f.get('info')
data=f['info']
print(data)