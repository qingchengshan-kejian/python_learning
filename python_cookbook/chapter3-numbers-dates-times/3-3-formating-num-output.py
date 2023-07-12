x = 1234.56789
print(format(x, '0.2f'))

# > 右对齐
# 10 宽度
# 1 精度
print(format(x, '>10.1f'))

print(format(x, '<10.1f'))

print(format(x, '^10.1f'))

print(format(x, 'e'))

print(format(x, '0.2E'))

print('The value is {:0,.2f}'.format(x))