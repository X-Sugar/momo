# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/6 0006

#用于生成和修改常见配置文档
#配置文件模块

import configparser


#生成配置文件, 字典的形式添加数据
config = configparser.ConfigParser()

# config['DEFAULT'] = {'minSdkVersion': '15',
#                      'targetSdkVersion': '24',
#                      'versionName': '1.0.0',
#                      'server action': 'yes'}
#
# config['luzhuo.me'] = {}
# config['luzhuo.me']['user'] = 'luzhuo'
#
# config['mysql'] = {}
# topsecret = config['mysql']
# topsecret['ip'] = '127.0.0.1'
# topsecret['port'] = '3306'
#
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)

#删除
# config.read('config.ini')
# config.remove_section('luzhuo.me')  #删除
# config.write(open('config.ini','w'))    #写入
#添加
# config.add_section('server.com')    #添加
# config.write(open('config.ini','a+'))   #添加
#修改/添加
config.read('config.ini')
config.set('mysql','port','1111')
config.write(open('config.ini','w'))
