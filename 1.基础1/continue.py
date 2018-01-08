# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/5 0005

for i in range(10):
    if i > 5 :
        continue
    print(i,end=' ')
################################################################
# i = 1
# while i < 10:
#     i += 1
#     if i%2>0:
#         continue
#     print(i)
################################################################


# exit_flag = False
# for i in range(10):
#     if i < 5:
#         continue
#     print(i)
#     for j in range(10):
#         print("第二层",j)
#         if j == 6:
#             exit_flag = True
#             break
#     if exit_flag:
#         break