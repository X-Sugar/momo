# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/4 0004

class Province:
    country = '中国'  # 1.静态字段，属于类,保存在类中，内存中只保存一份，执行是可通过对象访问，也可以通过类访问
    def __init__(self,name):
        self.name=name      # 2.普通字段，属于对象,保存在对象中，执行只能通过对象访问

# print(Province.country)
jiangxi = Province('江西')
#jiangxi.name = "江西西"    # 把对象的值修改了
print(jiangxi.name)
print(Province.country,jiangxi.name)
print(jiangxi.country)  # 通过对象访问静态字段