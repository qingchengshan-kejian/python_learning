l = list(range(10))
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)

l[3::2] = [11, 22]
print(l)

# 序列运算
l = [1, 2, 3]
print(l * 5)
# 重复5次