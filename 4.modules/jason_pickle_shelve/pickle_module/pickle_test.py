# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/15 0015

import pickle

dic={'name':'susu','age':'18'}

data=pickle.dumps(dic)
f=open('pickle_test','wb')
f.write(data)
f.close()
#  ##############################################
