lax_coordinates = (33, -118)
latitude, longitude = lax_coordinates

print(latitude)
print(longitude)

print(divmod(20, 8))
# 用*运算符把一个可迭代对象拆开作为函数的参数
t = (20, 8)
s = divmod(*t)
print(s)

quotient, remainder = divmod(*t)
print(quotient)
print(remainder)

# import os
# _, filename = os.path.split('/home/luciao/.ssh/idrsa.pub')
# print(filename)

a, b, *rest = range(5)
print(a)
print(b)
print(rest)