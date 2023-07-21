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

class specialEmployee(Employee):
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate) # calls the base classes
        self.bonus = bonus
    def hours(self, numHours):
        self.owed += numHours * self.rate * 2
        return("%.2f hours worked" % numHours)