class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 在Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。这非常有用，因为它允许我们在运行时去设置任意的新属性。
# 每一个实例，都有一个字典保存实例属性，如果实例很多，这是消耗内存的
# 在Python中，你可以在class中设置__slots__，它是一个包含这些固定的属性名的list。这样Python就不会再使用dict，而且只分配这些属性的空间。

