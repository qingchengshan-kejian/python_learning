x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # True x y值相等，实际是2个list
print(x is y) # False

x = y
print(x is y) # y赋值给x,x y 指向同一个list
