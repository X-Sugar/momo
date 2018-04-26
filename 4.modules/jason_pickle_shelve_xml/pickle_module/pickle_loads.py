# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/15 0015

import pickle

# f=open('pickle_test','rb')
#
# data=f.read()
# data=pickle.loads(data)
#
# print(data['name'])

# --------------------------------------------
with open('pickle_test','rb') as f:
    data = pickle.load(f)
    print(data)