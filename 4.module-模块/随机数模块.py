# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/27 0027

import random

#五位随机验证码
def cod_num():
    nums=''
    for i in range(5):
        add=random.choice([random.randrange(10),chr(random.randrange(65,91))])
        nums+=str(add)
    print(nums)

cod_num()
