add = lambda x, y: x + y
# 左边参数，右边返回

names =  ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']

sorted(names, key=lambda name: name.split()[-1].lower())
# 这是一个函数
# 函数接收names的元素作为参数
# 返回的是排序依据的结果