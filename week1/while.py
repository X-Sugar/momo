# -*- coding:utf-8 -*-
print('------------------------------------------------------------------------')
# for i in range(1,10):
#     for a in range(0,i):
#         print("#",end=" ")
#
#     for b in range(i,10):
#         print("*",end=" ")
#     print("")
for i in range(1,10):
     for j in range(1,i+1):
          print("%d*%d=%2d" % (j,i,i*j),end="\t")
     print (" ")

print('------------------------------------------------------------------------')
a = 1
while a <= 9:
    b = 1
    while b <= a:
        # print(b,'*',a,'=',a * b,end="\t")
        print("%d*%d=%d" % (a,b,a*b),end="\t")
        b += 1
    print()
    a += 1