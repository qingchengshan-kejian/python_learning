class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name # 这里的属性名是_开头的

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value # 这里的属性名是_开头的

    # deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute.")

# 使用不同的装饰器，实现getter setter deleter

a = Person('Guido')
print(a.first_name)
# obj.attrname 调用getter
a.first_name = 42
# print(a.first_name)
# obj.attrname = value 调用setter

del a.first_name
# del obj.attrname 调用deleter

# 对于类中的方法，我们有时候希望它可以像属性一样被调用，这时候我们通常给类的方法添加@property修饰符:
