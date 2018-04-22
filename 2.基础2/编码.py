# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/21 0021

s = 'Hell,默默'
print(type(s))      # <class 'str'>



# str >>> bytes: 编码 bytes 16进制

b = bytes(s,'utf8')
print(b)        # b'Hell,\xe9\xbb\x98\xe9\xbb\x98'

b2 = s.encode('utf8')
print(b2)       # b'Hell,\xe9\xbb\x98\xe9\xbb\x98'

# bytes >>> str:解码

c1 = str(b2,'utf8')
print(c1)       # Hell,默默

c11 = b2.decode('utf8')
print(c11)

c2 = str(b2,'gbk')
print(c2)       # Hell,榛橀粯（乱码）
