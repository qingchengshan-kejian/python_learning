import json


data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}

# json_str = json.dumps(data)
# print(json_str)
#
# data_r = json.loads(json_str)
# print(data_r)

# writing json data
with open('data.json', 'w') as f:
    json.dump(data, f)

# reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

# 字典到json字符串 dumps, 相反loads
# 文件的读写，是dump和load