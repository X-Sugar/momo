# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/16 0016

# print('''\
# Usage:thingy[OPTHONS]
#     -h                  Display this usage message
#     -H hostname         Hostname to connnect to
# ''')
#
# word='Python'
# print(word[0:4])
# print(word[4: ])
# print(word[-2:])
# words=['wwwwwwwwwwwww','cat','window','defenestrate']
# for w in words[:]:
#     if len(w)>6:
#         words.insert(2,w)
# print(words)

# a = ['Mary','had','a','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])
# print(list(range(2,10)))

# import re
# a='<span id="stock_quoteinfo_zde" class="green" >-0.29</span>&nbsp;&nbsp;<span id="stock_quoteinfo_zdf" class="green">(-1.45%)</span>'
#
# ret=re.findall('[-]?[\d]+[.]?[\d]+[%]?',a)
# print(ret)

# def fib(n):
#     result=[]
#     a,b=0,1
#     while a<n:
#         result.append(a)
#         a,b=b,a+b
#     return result
#
# fib(100)

mart=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# a=[[row[i] for row in mart] for i in range(4)]
# print(a)

print(list(zip(*mart)))