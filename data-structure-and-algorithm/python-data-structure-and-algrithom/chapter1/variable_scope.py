a = 10; b = 20


def my_function():
    global a # 显式声明成全局变量
    a = 11; b = 21


my_function()
print(a)
print(b)