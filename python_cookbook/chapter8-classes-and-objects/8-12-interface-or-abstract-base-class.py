from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

a = IStream() # TypeError: can't instantiate abstract class
              #IStream with abstract methods read, write

# 使用 @abstractmethod 抽象方法:
#
#     所在的 class 继承 abc.ABC
#     给需要抽象的实例方法添加装饰器 @abstractmethod
#
# 完成这两步后, 这个 class 就变成了抽象类, 不能被直接实例化, 要想使用抽象类, 必须继承该类并实现该类的所有抽象方法

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def info(self):
        print("Animal")


class Bird(Animal):
    # 实现抽象方法
    def info(self):
        # 调用基类方法(即便是抽象方法)
        super().info()
        print("Bird")


animal = Animal() # 直接实例化基类，会报错

bird = Bird()
bird.info()
# 派生类中实现所有基类的抽象方法后，便可实例化。