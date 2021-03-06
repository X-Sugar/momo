# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/27 0027

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test")
root = tree.getroot()
# print(root.tag) #最外层标签


# 遍历xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)

# 只遍历指定节点
# for node in root.iter('year'):
#     print(node.tag,node.text)

# 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated", "yes")
#
# tree.write("xmltest.xml")

# 删除node
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')
