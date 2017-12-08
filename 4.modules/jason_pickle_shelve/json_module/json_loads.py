# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/15 0015

# import json
#
# f=open('json_test','r',encoding='utf8')
#
# data=f.read()
# data=json.loads(data)
#
# print(data['name'])

#---------------------------------------------

import json

# f=open('json_test2','r',encoding='utf8')
# data=json.load(f)
# print(data['name'])
# f.close()

with open('json_test2','r',encoding='utf8') as f:
    data=json.load(f)
    print(data['name'])