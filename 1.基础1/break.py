# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/5 0005

# for i in range(1,10):
#     print(i)
#     i += 1
#     if i > 5:
#         break
#######################################################

# _user = "Sugar"
# _passwd = "123"
# for i in range(3):
#     username = input("Username:")
#     password = input("Password:")
#     if username == _user and password == _passwd:
#         print("Welcom %s login..." % (_user))
#         break   #跳出、中断
#     else:
#         print("Invalid username or password!")
#
# else:       #只要上面for循环正常循环完毕，就会执行else
#     print("不要脸！")

#利用for、if打印奇数、偶数
'''
for i in range(1,101):
    if i % 2 == 0:
        print(i,end=" ")

print()

for i in range(1,101):
    if i % 2 == 1:
        print(i,end=" ")
'''

#快速打印奇数、偶数
'''
for i in range(1,101,2):
    print(i,end=" ")

print()

for i in range(2,101,2):
    print(i,end=" ")
'''

