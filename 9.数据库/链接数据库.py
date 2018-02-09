# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/25 0025

# 链接数据库，安装：pip install pymysql
import pymysql

# 创建链接
db = pymysql.connect('localhost','root','xia0suba0','learn')

# 创建游标,括号内的参数：设置游标类型为字典，默认元组
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

# 传参使用方法,r是受影响的行数
# inp = input('请输入需要增加的名字：')
# r = cursor.execute('INSERT INTO learn.txt(name,AUTHOR,DATA,pid) VALUES(%s,"bbb","2015-11-22",33)',inp)
# db.commit()

# 多个传参使用方法,多个只能是列表或者是元组
# inp = input('请输入需要增加的名字：')
# r = cursor.execute('INSERT INTO learn.txt(name,AUTHOR,DATA,pid) VALUES(%s,%s,%s,%s)',('aa','bb','2014-01-03',33))
# db.commit()

# 传入多个参数
# lists=[
#     ('sdfd','sd','2014-07-03',44),
#     ('dfgdfg','jk','2014-12-03',36),
#     ('yuty','jhk','2014-11-03',78),
# ]
# r = cursor.executemany('INSERT INTO learn.txt(name,AUTHOR,DATA,pid) VALUES(%s,%s,%s,%s)',lists)
# db.commit()

cursor.execute('select * from learn.txt')
# 取出数据
values1 = cursor.fetchone()
values2 = cursor.fetchall()
print(values2)

# 提交数据，修改表的时候需要确认
# db.commit()

# 关闭游标
cursor.close()
# 关闭链接
db.close()