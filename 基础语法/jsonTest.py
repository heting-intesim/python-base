import json
 
# Python 字典类型转换为 JSON 对象
# data = {
#     'no' : 1,
#     'name' : 'Yuan',
#     'url' : 'http://www.runoob.com'
# }
 
# json_str = json.dumps(data)
# print ("Python 原始数据：", repr(data))
# print ("JSON 对象：", json_str)
import os
path = os.path.dirname(__file__)
with open(os.path.join(path,'t.json'),encoding='utf-8') as file:
    data = json.load(file)
print(data)
for key,value in data.items():
    print(key,value)
print(data['books']['name'])