colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

# 列表推到的作用只有一个：生成列表。如果想生成其他类型的序列，可以用生成器表达式。