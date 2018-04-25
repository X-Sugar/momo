# __author:  Administrator
# date:  2016/8/23


dic={1:'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
# dic={'name':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}

# print(dic)

# # 字典两大特点：无序，键唯一


# # 字典的创建
# a=list()
# print(a)

# dic={'name':'alex'}

# dic1={}
# dic2=dict((('name','alex'),))
# print(dic2)

# dic3=dict([['name','alex'],])
# print(dic3)
#
#
#
#
# dic1={'name':'alex'}
# dic1['age']=18
# print(dic1)
#
# # 键存在，不改动，返回字典中相应的键对应的值
# ret=dic1.setdefault('age',34)
# print(ret)
#
# #键不存在，在字典中中增加新的键值对，并返回相应的值
# ret2=dic1.setdefault('hobby','girl')
# print(dic1)
# print(ret2)
#
# # 查  通过键去查找
# dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
#
# print(dic3['name'])
# print(list(dic3.keys()))
# print(list(dic3.values()))
# print(list(dic3.items()))

# li=[1,2,34,4]
# li[2]=5
# dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
# dic3['age']=55
# print(dic3)
#
dic4={'age': 18, 'name': 'alex', 'hobby': 'girl'}
# dic5={'1':'111','2':'222'}
dic5={'1':'111','name':'222'}

dic4.update(dic5)
print(dic4)
print(dic5)



# dic5 = {'name': 'alex', 'age': 18, 'class': 1}
#
# dic5.clear() # 清空字典
# print(dic5)
# del dic5['name'] #删除字典中指定键值对
# print(dic5)
#
#
# print(dic5.pop('age')) #删除字典中指定键值对，并返回该键值对的值
# ret=dic5.pop('age')
# print(ret)
# print(dic5)
#
# a = dic5.popitem() #随机删除某组键值对，并以元组方式返回值
# print(a, dic5)
#
# del dic5        #删除整个字典
# print(dic5)
#
#
# 5 其他操作以及涉及到的方法
#
#
# dic6=dict.fromkeys(['host1','host2','host3'],'test')
# print(dic6)                         # {'host3': 'test', 'host1': 'test', 'host2': 'test'}
#
# dic6['host2']='abc'
# print(dic6)
#
# dic6=dict.fromkeys(['host1','host2','host3'],['test1','tets2'])
# print(dic6)#{'host2': ['test1', 'tets2'], 'host3': ['test1', 'tets2'], 'host1': ['test1', 'tets2']}
#
# dic6['host2'][1]='test3'
# print(dic6)#{'host3': ['test1', 'test3'], 'host2': ['test1', 'test3'], 'host1': ['test1', 'test3']}
#
#
#
#
# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }

# av_catalog['欧美']["www.youporn.com"][1]='高清午马'



# dic={5:'555',2:'666',4:'444'}
# print(5 in dic)
# print(sorted(dic.items()))


# dic5={'name': 'alex', 'age': 18}
# for i in dic5:
#     print(i,dic5[i])
#
# for i,v in dic5.items():
#     print(i,v)



# String 操作

# a="Let's go "
# print(a)
# 1   * 重复输出字符串
# print('hello'*20)

# 2 [] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
# print('helloworld'[2:])

# 3关键字 in
# print(数据连接 in [23,45,数据连接])
# print('e2l' in 'hello')

# 4 %   格式字符串
# print('alex is a good teacher')
# print('%s is a good teacher'%'alex')

# 5
# a='123'
# b='abc'
# d='44'
# c=a+b
# print(c)
#
# c= ''.join([a,b,d])
# print(c)

#list中取字典值
# a=[{u'escapely_1':u'5505052'}]
# b=a[0].get('escapely_1')
# print(b)

#不用get
# dic={5:'555',2:'666',4:'444'}
# print(dic[5])



# 字典
# dict
# dict
# dic = {
#     "k1": 'v1',
#     "k2": 'v2'
# }
# 1 根据序列，创建字典，并指定统一的值
# v = dict.fromkeys(["k1",123,"learn"],123)
# print(v)

# 2 根据Key获取值，key不存在时，可以指定默认值（None）
# v = dic['k11111']
# print(v)
# v = dic.get('k1',111111)
# print(v)

# 3 删除并获取值
# dic = {
#     "k1": 'v1',
#     "k2": 'v2'
# }
# v = dic.pop('k1',90)
# print(dic,v)
# k,v = dic.popitem()
# print(dic,k,v)

# 4 设置值，
# 已存在，不设置，获取当前key对应的值
# 不存在，设置，获取当前key对应的值
# dic = {
#     "k1": 'v1',
#     "k2": 'v2'
# }
# v = dic.setdefault('k1111','123')
# print(dic,v)

# 5 更新
# dic = {
#     "k1": 'v1',
#     "k2": 'v2'
# }
# dic.update({'k1': '111111','k3': 123})
# print(dic)
# dic.update(k1=123,k3=345,k5="asdf")
# print(dic)

# 6 keys()  7 values()   8 items()   get   update
##########



# 1、基本机构
# info = {
#     "k1": "v1", # 键值对
#     "k2": "v2"
# }
#### 2 字典的value可以是任何值
# info = {
#     "k1": 18,
#     "k2": True,
#     "k3": [
#         11,
#         [],
#         (),
#         22,
#         33,
#         {
#             'kk1': 'vv1',
#             'kk2': 'vv2',
#             'kk3': (11,22),
#         }
#     ],
#     "k4": (11,22,33,44)
# }
# print(info)

####  3 布尔值(1,0)、列表、字典不能作为字典的key
# info ={
#     1: 'asdf',
#     "k1": 'asdf',
#     True: "123",
#     # [11,22]: 123
#     (11,22): 123,
#     # {'k1':'v1'}: 123
#
# }
# print(info)

# 4 字典无序

# info = {
#     "k1": 18,
#     "k2": True,
#     "k3": [
#         11,
#         [],
#         (),
#         22,
#         33,
#         {
#             'kk1': 'vv1',
#             'kk2': 'vv2',
#             'kk3': (11,22),
#         }
#     ],
#     "k4": (11,22,33,44)
# }
# print(info)

# 5、索引方式找到指定元素
# info = {
#     "k1": 18,
#     2: True,
#     "k3": [
#         11,
#         [],
#         (),
#         22,
#         33,
#         {
#             'kk1': 'vv1',
#             'kk2': 'vv2',
#             'kk3': (11,22),
#         }
#     ],
#     "k4": (11,22,33,44)
# }
# # v = info['k1']
# # print(v)
# # v = info[2]
# # print(v)
# v = info['k3'][5]['kk3'][0]
# print(v)

# 6 字典支持 del 删除
# info = {
#     "k1": 18,
#     2: True,
#     "k3": [
#         11,
#         [],
#         (),
#         22,
#         33,
#         {
#             'kk1': 'vv1',
#             'kk2': 'vv2',
#             'kk3': (11,22),
#         }
#     ],
#     "k4": (11,22,33,44)
# }
# del info['k1']
#
# del info['k3'][5]['kk1']
# print(info)

# 7 for循环
# dict
# info = {
#     "k1": 18,
#     2: True,
#     "k3": [
#         11,
#         [],
#         (),
#         22,
#         33,
#         {
#             'kk1': 'vv1',
#             'kk2': 'vv2',
#             'kk3': (11,22),
#         }
#     ],
#     "k4": (11,22,33,44)
# }
# for item in info:
#     print(item)
#
# for item in info.keys():
#     print(item)

# for item in info.values():
#     print(item)

# for item in info.keys():
#     print(item,info[item])

# for k,v in info.items():
#     print(k,v)

# True 1  False 0
# info ={
#     "k1": 'asdf',
#     True: "123",
#     # [11,22]: 123
#     (11,22): 123,
#     # {'k1':' v1'}: 123
#
# }
# print(info)

#######################　整理 #################

# 一、数字
# int(..)
# 二、字符串
# replace/find/join/strip/startswith/split/upper/lower/format
# tempalte = "i am {name}, age : {age}"
# # v = tempalte.format(name='alex',age=19)
# v = tempalte.format(**{"name": 'alex','age': 19})
# print(v)
# 三、列表
# append、extend、insert
# 索引、切片、循环
# 四、元组
# 忽略
# 索引、切片、循环         以及元素不能被修改
# 五、字典
# get/update/keys/values/items
# for,索引

# dic = {
#     "k1": 'v1'
# }

# v = "k1" in dic
# print(v)

# v = "v1" in dic.values()
# print(v)
# 六、布尔值
# 0 1
# bool(...)
# None ""  () []  {} 0 ==> False