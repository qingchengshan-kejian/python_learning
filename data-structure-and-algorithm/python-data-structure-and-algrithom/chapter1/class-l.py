class Employee(object):
    numEmployee = 0 # 类属性，静态 or 动态属性？
    def __init__(self, name, rate):
        self.owed = 0 # 实例属性，静态 or 动态属性？
        self.name = name
        self.rate = rate
        Employee.numEmployee +=1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return ("%.2f hours worked" % numHours)

    def pay(self):
        self.owed = 0
        return ("payed %s " % self.name)

emp1 = Employee('kexia', 19)
emp2 = Employee('yue', 20)
print(Employee.numEmployee)
print(emp1.hours(20))
print(emp1.owed)
print(emp1.pay())
emp3 = Employee('yue2', 20)
print(Employee.numEmployee)

# 参考打印信息，比较类和实例
print(dir(Employee))
print(dir(emp1))