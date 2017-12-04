# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/16 0016

# print('''\
# Usage:thingy[OPTHONS]
#     -h                  Display this usage message
#     -H hostname         Hostname to connnect to
# ''')
#
# word='Python'
# print(word[0:4])
# print(word[4: ])
# print(word[-2:])
# words=['wwwwwwwwwwwww','cat','window','defenestrate']
# for w in words[:]:
#     if len(w)>6:
#         words.insert(2,w)
# print(words)

# a = ['Mary','had','a','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])
# print(list(range(2,10)))

# import re
# a='<span id="stock_quoteinfo_zde" class="green" >-0.29</span>&nbsp;&nbsp;<span id="stock_quoteinfo_zdf" class="green">(-1.45%)</span>'
#
# ret=re.findall('[-]?[\d]+[.]?[\d]+[%]?',a)
# print(ret)

# def fib(n):
#     result=[]
#     a,b=0,1
#     while a<n:
#         result.append(a)
#         a,b=b,a+b
#     return result
#
# fib(100)

# mart=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# a=[[row[i] for row in mart] for i in range(4)]
# print(a)

# print(list(zip(*mart)))

# def fib(n):
#     a,b=0,1
#     while b<n:
#         print(b,end=' ')
#         a,b=b,a+b
#     # print()
# fib(100)

# def fib2(n):
#     result=[]
#     a,b=0,1
#     while b<n:
#         result.append(b)
#         a,b=b,a+b
#     return result
# print(fib2(100))
#
# import builtins
# a=dir(builtins)
# for i in a:
#     print(i)

# import sys
# for i in sys.argv:
#     print(i)
# a=sys.path
# print(a)
# print(dir(a))



# import random
# rint(random.choice(['吃鸡吃鸡！','吃个锤子！']))

class Person:
    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""

        self.fight = self.fight - 200

    def practice(self):
        """注释：自我修炼，增长100战斗力"""

        self.fight = self.fight + 200

    def incest(self):
        """注释：多人游戏，消耗500战斗力"""

        self.fight = self.fight - 500

    def detail(self):
        """注释：当前对象的详细情况"""

        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight)
        print(temp)

# #####################  开始游戏  #####################

cang = Person('苍井井', '女', 18, 1000)  # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)  # 创建波多多角色

cang.incest()  # 苍井空参加一次多人游戏
# dong.practice()  # 东尼木木自我修炼了一次
# bo.grassland()  # 波多多参加一次草丛战斗
#
# # 输出当前所有人的详细情况
cang.detail()
# dong.detail()
# bo.detail()
#
# cang.incest()  # 苍井空又参加一次多人游戏
# dong.incest()  # 东尼木木也参加了一个多人游戏
# bo.practice()  # 波多多自我修炼了一次
#
# # 输出当前所有人的详细情况
# cang.detail()
# dong.detail()
# bo.detail()