# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/15 0015

# 不能对函数进行序列化
# import json
#
# dic={'name':'susu','age':'18'}
#
# data=json.dumps(dic)
# f=open('json_test','w',encoding='utf8')
# f.write(data)
# f.close()



# ---------------------------------------------dump
# 写法更简单了
import json

dic = {
    'name': 'susu',
    'age': '18'
}

f = open('json_test2','w',encoding='utf8')
json.dump(dic, f)
f.close()