from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)
# 按格式解析字符串到datetime格式
z = datetime.now()
print(z)
diff = z - y
print(diff)