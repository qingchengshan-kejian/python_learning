class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
    # deleter function
    @name.deleter
    def name(self):
        raise AttributeError("can't delete attribute")
    # 对象原来就具有getter setter，可以调用
    # 这里做了扩展，例如setter,增加value类型的校验
    # deleter 关闭

class SubPerson(Person):
    @property
    def name(self):
        print('Getting name') # 扩展
        return super().name
    @name.setter
    def name(self, value):
        print('Setting name to', value) # 扩展
        super(SubPerson, SubPerson).name.__set__(self, value) # 这里super为什么这样调用？？

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('kexia')
print(s.name)