# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/8 0008

# ret=re.search('\([^()]+\)',s).group()
source='1-2*((60 -30+(-40/5)*(9--2*5/3+7/3*99/4*2998+10*568/13))-(-4*3)/(16-3*2)'

import re

#判断计算格式是否正常
# def check(s):
#     flag=True
#     if re.findall('[a-zA-Z]',source):
#         print('Invalid')
#         flag=False
#     return flag
#
# def format(s):
#     s.replace(' ','')
#     s.replace('++','+')
#     return s

# ret=re.search('\([^()]+\)','(1+(2+5)*2').group()
# s1=print(ret)

# ret=re.match(r'^\d{3}\-\d{3,8}$','010-123456789')
# ret=re.search(r'^\d{3}\-\d{3,8}','010-123456789').group()
# print(ret)

# ret=re.split('\s+','a               b c')
# ret=re.split(r'[\s\,]+','a   t,u,,,,            b c')
# print(ret)

# t = '9:21:59'
# m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$',t)
# print(m)

# ret=re.match('^([\w\s\.]+)\@([\w]+)\.([\w]{2,3}$)','xiaobao123@cddssss.cn')
# print(ret.group())

