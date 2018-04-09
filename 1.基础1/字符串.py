# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/21 0021

# String的内置方法

st = 'hello kitty {name} is {age}'

# print(st.count('l'))       #  统计元素个数
# print(st.capitalize())     #  首字母大写
# print(st.center(50,'#'))   #  居中
# print(st.endswith('tty3')) #  判断是否以某个内容结尾
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.expandtabs(tabsize=20))  # 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
# print(st.find('t'))        #  查找到第一个元素，并将索引值返回
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print(st.format_map({'name':'alex','age':22}))
# print(st.index('t'))
# print('asd'.isalnum())    # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# print('addf'.isalpha())   # 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
# print('12632178'.isdecimal())  # 如果 string 只包含十进制数字则返回 True 否则返回 False.
# print('1269999.uuuu'.isnumeric())  # 如果 string 中只包含数字字符，则返回 True，否则返回 False
# print('abc'.isidentifier())
# print('abc'.islower())  # 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# print('ABC'.isupper())  # 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# print('  e'.isspace())  # 如果 string 中只包含空格，则返回 True，否则返回 False.
# print('My title'.istitle())  # 如果 string 是标题化的(见 title())则返回 True，否则返回 False
# print('My tLtle'.lower())  # 转换 string 中所有大写字符为小写.
# print('My tLtle'.upper())  # 转换 string 中所有大写字符为大写.
# print('My tLtle'.swapcase())  # 翻转 string 中的大小写
# print('My tLtle'.ljust(50,'*'))  # 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# print('My tLtle'.rjust(50,'*'))  # 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# print('\tMy tLtle\n'.strip())  # 在 string 上执行 lstrip()和 rstrip()
# print('\tMy tLtle\n'.lstrip())  # 截掉 string 左边的空格
# print('\tMy tLtle\n'.rstrip())  # 截掉 string 右边的空格
# print('My title title'.replace('itle','lesson',1))  # 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
# print('My title title'.rfind('t'))  # 类似于 find()函数，不过是从右边开始查找.
# print('My title title'.split('i',1))  # 以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
# print('My title title'.title())  # 返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# print('ssssdfdf'.rpartition('d'))  # ('ssssdf', 'd', 'f'),已d为分隔，包含d

# ----------------摘一些重要的字符串方法------------------------
# print(st.count('l'))
# print(st.center(50,'#'))   #  居中
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.find('t'))
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print('My tLtle'.lower())
# print('My tLtle'.upper())
# print('\tMy tLtle\n'.strip())
# print('My title title'.replace('itle','lesson',1))
# print('My title title'.split('i',1))
# print('sdfsdfsd\nsdfsdfsd\neiojiouj'.splitlines())
# print('sdfsdfsdf'.startswith('s'))  # 判断是否以什么为开头
# print('sdfsdfdfsdf'.endswith('f'))  # 判断是否以什么为结尾


# ----------------------操作小例子---------------------------

# 将字符串中的每一个元素按照指定分隔符进行拼接
# test = '你是风儿我是沙'
# v = "_".join(test)
# print(v)
