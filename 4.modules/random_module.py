# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/27 0027

import random

# 用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成随机数
print(random.uniform(10,20))
print(random.uniform(20,10))

# 用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，Python生成随机数
print(random.randint(12,20))
# print(random.randint(30,20))  #语句错误

# 在1到100随机一个数
print(random.choice(range(1,101)))
print(random.choice('sdfsdfsdf123#$%^&*&*'))
# 随机选取字符串：
print(random.choice(['susu','momo','cici','lulu']))

# 随机选取0到100间的偶数：
print(random.randrange(0,101,2))

# 随机浮点数：
print(random.random())

# 多个字符中选取特定数量的字符,返回一个列表：
print(random.sample('aaaabcdefgh',3))

# 洗牌：
iteams = [1,2,3,4,5,6]
random.shuffle(iteams)
print(iteams)
# 五位随机验证码
# (65, 91)所有大写字母(97, 123)所有小写字母(48, 58)所有数字
def cod_num():
    nums = ''
    lists = ['!','@','#','%','&','*','?']
    for i in range(8):
        add = random.choice([random.randrange(10),chr(random.randrange(65,91)),random.choice(lists)])
        nums += str(add)
    print(nums)
cod_num()
