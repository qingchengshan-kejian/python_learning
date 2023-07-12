x=  [1, 2, 3, 4]
y = [5, 6, 7, 8]
# 列表拼接两次 也就是x + x
print(x * 2)
# 列表拼接
print(x + y)

# numpy 是一个可以独立学习的模块。
# 数组与矩阵运算


import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print(ax * 2)
print(ax + ay)
print(ax * ay)