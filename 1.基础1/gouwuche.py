# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/6 0006

#打印菜单
menu = '''
-------------菜单------------
1. iPhone 6s     ￥5800
2. macbook       ￥9000
3. coffee        ￥32
4. python book   ￥80
5. bicyle        ￥1500
-----------------------------
退出请输入：exit
-----------------------------
'''
print(menu)

#输入余额
salary = int(input("请输入的你余额："))

#定义列表
name = ["pass","iPhone 6s","macbook","coffee","python book","bicyle"]
price = [0,5800,9000,32,80,1500]

while True:
    nums = input("请输入你要购买物品的序号：")
    if nums == "exit":
        print("您的余额为：%d" % salary)
        print("欢迎下次光临！")
        break
    num = int(nums)
    if salary - price[num] > 0:
        print("已加入：%s到你的购物车，当前余额为：%d!" % (name[num],salary - price[num]))
        salary = salary - price[num]
    else:
        print("余额不足，%d，请重新输入！" % (salary - price[num]))