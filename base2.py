# -*- coding:utf-8 -*-

#python取json数据
#理解python对象、json之间的转换
#编码：把一个Python对象编码转换成Json字符串   json.dumps()
#解码：把Json格式字符串解码转换成Python对象   json.loads()

import json


data = {'b':789,'c':456,'a':123}

json_data = json.dumps(data)
#json_data = json.dumps(data,sort_keys=True,indent=4)
print type(json_data)
print json_data

data2 = json.loads(json_data)
print type(data2)
print data2
print data2['a']


data3 = {'姓名':'zhangman','年龄':30,'性别':'女'}
json_data = json.dumps(data3,sort_keys=True,indent=4,ensure_ascii=False)
print json_data

