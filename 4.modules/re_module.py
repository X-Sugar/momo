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

ret=re.findall('\\\\c','sdfsdf\c')
print(ret)