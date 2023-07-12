x = 10
a = lambda y: x + y # x是全局变量
print(a(10))

x = 20 # x的值更新
b = lambda y: x + y # x是全局变量
print(a(10))
print(b(10))


x = 10
a = lambda y, x=x: x + y # x是全局变量赋值给x局部变量10，函数a有个局部变量x,值为10
print(a(10))

x = 20 # x的值更新
b = lambda y, x=x: x + y # x是全局变量赋值给x局部变量20，函数b有个局部变量x,值为20
print(a(10))
print(b(10))