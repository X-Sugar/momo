# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/8 0008

# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def show(self):
#         return "%s---%s" % (self.name,self.age)
# obj = Foo('susu',18)

# print(obj.name)     # 方法一

# print(obj.__dict__['name'])     # 方法二


# 通过字符串的形式操作对象中的成员
# print(getattr(obj,'name'))      # 1.获取成员 直接从对象里取值

# print(hasattr(obj,'agee'))      # 2.检查成员 判断值在对象里是否存在

# setattr(obj,'k1','v1')          # 3.设置成员
# print(obj.k1)

# delattr(obj,'name')             # 4.删除成员
# obj.name

import su

r1 = getattr(su,'name')
print(r1)

r2 = getattr(su,'func')
result =r2()
print(result)

r3 = getattr(su,'Foo')
print(r3)
obj = r3()
print(obj.name)
