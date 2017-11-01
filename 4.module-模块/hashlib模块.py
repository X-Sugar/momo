# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/30 0030

#加密，从明文转换成密文
import hashlib
# m=hashlib.md5()
# # print(m)
#
# m.update('hello world'.encode('utf8'))
# print(m.hexdigest())    #16进制明文
# # print(m.digest())
#
# m.update('susu'.encode('utf8'))
# print(m.hexdigest())
#
# #跟m更新过后的md5值相同
# m2=hashlib.md5()
# m2.update('hello worldsusu'.encode('utf8'))
# print(m2.hexdigest())
#
# s=hashlib.sha256()      #sha.256最常用的
# s.update('hello world'.encode('utf8'))
# print(s.hexdigest())