# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/6 0006
#http://www.cnblogs.com/yuanchenqi/articles/5732581.html

#引入正则：模糊匹配

#元字符： . ^   $   *   +   ?   { }     [ ]     |   ( )     \
import re

#   .   通配符：匹配一个字符
# ret=re.findall('w.l','hello world')
# print(ret)

#   ^   尖角符:匹配开头
# ret=re.findall('^h...o','hello world')
# print(ret)

#   $   结尾
# ret=re.findall('w...d$','hello world')
# print(ret)

#   * 重复匹配 [0,无穷次]
# ret=re.findall('ba*','sdfdbfsdfbaaaaaaaaaaaaa')
# print(ret)

#   +   重复匹配 [0,无穷次]
# ret=re.findall('ba+','sdfdbfsdfbaaaaaaaaaaaaa')
# print(ret)

#   ?   [0,1]
# ret=re.findall('a?b','aaaaaaaaabgefsdfggacb')
# print(ret)

#   { }
# ret=re.findall('a{5}b','aaaaaaaaabsdfdf')
# print(ret)

# ret=re.findall('a{1,3}b','absdfdf') #贪婪匹配
# print(ret)


# 结论： *等于｛0，正无穷｝  +等价于｛1，正无穷｝ ？等价于{0,1}

#   [ ] 字符集 或的关系 只能选其1
# ret=re.findall('a[c,d]x','acx')
# ret=re.findall('[a-z]','acx')
# print(ret)

# [ ] 取消元字符功能,例外：(\ ^ -)
# ret=re.findall('[w,*]','awdx*')
# print(ret)

# ret=re.findall('[1-9,a-z,A-Z]','12tySK')
# print(ret)

# ret=re.findall('^t','sdfdt4e123tsdf')
# ret=re.findall('[^t]','sdfdt4e123tsdf') #除了t，取反
# ret=re.findall('[^4,5]','ser4sdf5') #排除4，5
# print(ret)


#   \
#反斜杠后边跟元字符去除特殊功能
#反斜杠好偶跟普通字符实现特殊功能

# \d  匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b  匹配一个特殊字符边界，比如空格 ，&，＃等


# ret=re.findall('\d{11}','fsdfsfs1231234124535456345')
# print(ret)

# ret=re.findall('\sadf','sdf adf')
# print(ret)

# ret=re.findall('\w11','sdff11fcc')
# print(ret)

# ret=re.findall(r'I\b','I am a boy')
# print(ret)

################################################################

#匹配出第一个满足条件的结果
# ret=re.search('sb','sdfsgsdgssbfdfe')
# # ret=re.search('sb','sdfsgsdgssbfdfe').group()
# print(ret)
# print(ret.group())

# ret=re.search('a\.','a.sdfd').group()
# print(ret)

# ret=re.search('a\+','a+gj').group()
# print(ret)

# ret=re.findall('\\\\c','sdfsdf\c')
# ret=re.findall(r'\\c','sdfsdf\c')
# print(ret)

#   ( )
# ret=re.search('(as)+','sdsdfsdasas').group()
# ret=re.search('(as)|3','3as').group()
# print(ret)


# ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','wwwweeee34ttt123/ooo')
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))

########################################################################################
#正则表达式的方法
# 1   findall()：所有结果都返回到一个列表里
# 2   search()：返回匹配到的第一个对象（object），对象可以调用group() 返回结果
# 3   match()：只在字符串开始（字符串开头）匹配，也返回对象，对象可以调用group() 返回结果

ret=re.match('asd','asdsdfsdasd')
print(ret.group())

# 4   split()
# ret=re.split('s','jojusoijl')
# ret=re.split('[k,s]','aewrsloikuj')
# print(ret)

# 4   sub()     #替换
# ret=re.sub('a..x','s..b','sdfsdfaffxxfg')
# ret=re.sub('\d','xxx','sdf3sdf4',1)   #替换次数
# print(ret)

# 5   compile()
# ret=re.compile('\.com')
# rets=ret.findall('dfsdf.comserefsd')
# print(rets)


##################################################################################

# ret=re.finditer('\d','sdff3sfdf4s') #迭代器
# print(next(ret).group())
