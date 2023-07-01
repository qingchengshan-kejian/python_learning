# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# b = list(dedupe(a))
# print(b)

def dedupe(items, key=None):
    # 这个是用来存储，判断是否重复的，并不是函数的返回
    # 存储字典里一个元素的value
    # 这个函数是一个生成器
    seen = set()
    for item in items:
        # print(item)
        # key是一个函数
        # 函数的入参是字典元素，返回是元组，元组里是字典元素的值
        val = item if key is None else key(item)
        # print(val)
        if val not in seen:
            yield item
            seen.add(val)


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# 按一对值是否重复
b = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
print(b)

# 按第一个值是否重复
b = list(dedupe(a, key=lambda d: (d['x'])))
print(b)

