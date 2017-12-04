# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/4 0004

class Person:

    def __init__(self,na,gen,age,fig):
        self.name=na
        self.gender=gen
        self.age=age
        self.fight=fig
    def grassland(self):
        """注释：草丛作战，消耗200战斗力"""

        self.fight = self.fight - 200
        print("进行了一次草丛作战！消耗200战斗力！")
    def practice(self):
        """注释：自我修炼，增长100战斗力"""

        self.fight = self.fight + 100
        print("进行了一次自我修炼！增加100战斗力！")
    def incest(self):
        """注释：多人游戏，消耗500战斗力"""

        self.fight = self.fight - 500
        print("进行了一次多人游戏！消耗500战斗力！")
    def detail(self):
        """注释：当前对象的详细情况"""
        temp1="当前状态："
        temp2= "姓名：%s 性别：%s 年龄：%s 战斗力：%s" % (self.name,self.gender,self.age,self.fight)
        print(temp1)
        print(temp2)
# ################开始游戏########################
cang = Person('苍井空','女',30,1000) #创建角色

cang.grassland()   #参加一次多人游戏
cang.practice() #参加一次个人修炼
cang.detail()   #当前个人详细情况
