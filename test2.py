import re

sfz = ['360730199102013225','360730198902013225','360730199002013225']

for i in sfz:
    ret = re.findall('^\d{6}1990\d{8}$',i)
    if ret:
        print(ret[0])