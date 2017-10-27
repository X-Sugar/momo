# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/11 0011

# dic = {'name1':1,'name2':2,'name3':3,'name4':{'name':'susu','age':28}}
#
# dic['name1']='susu'
# print(dic)
#
# dic2 = dict((('name','susu'),))
# print(dic2)
#
# dic1={'name':'susu'}
# dic1['age']=18
# print(dic1)

# ret = dic1.setdefault('age',34)
# print(ret)
#
# body = {'age':10,'name':'susu','hobby':'girl'}
# print(body.keys())
# print(body.values())
# print(body.items())
# print(list(body.keys()))
#
# dic6=dict.fromkeys(['host1','host2','host3'],'test')
# print(dic6)

name = {
    "china":{
        "1024":["free","fast","good"]
    }
}

name["china"]["1024"][1]='sususususu'
print(name)

for i in name:
    print(i,name[i])
