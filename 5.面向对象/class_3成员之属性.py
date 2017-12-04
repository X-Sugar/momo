# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/4 0004
"""
class Foo:
    def __init__(self):
        self.name = 'a'

    def bar(self):
        # self是对象
        print('bar')

    # 用户执行 obj.per
    @property   # 属性
    def per(self):
        print('per')

    #obj.per=123
    @per.setter
    def per(self,var):
        print(var)

    @per.deleter
    def per(self):
        print('666')

obj = Foo()
obj.per     # 实际是方法，访问是模仿字段

obj.per=123

del obj.per
"""
# ---------------------------------------------------------------
"""
class Pergination:
    def __init__(self,current_page):
        try:
            p = int(current_page)
        except Exception as e:
            p=1

        self.page = p

    @property
    def start(self):
        val = (self.page - 1) * 10
        return val

    @property
    def end(self):
        val= self.page * 10
        return val

li = []
for i in range(1000):
    li.append(i)

while True:
    p = input('请输入要查看的页码：')
    nums = Pergination(p)
    print(li[nums.start:nums.end])
 """
# ---------------------------------------------------------------

class Foo:

    def f1(self):
        return 1
    per = property(fget=f1)     #方法跟下面一样

    # @property
    # def per(self):
    #     return 12