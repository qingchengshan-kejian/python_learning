_formats = {
'ymd' : '{d.year}-{d.month}-{d.day}',
'mdy' : '{d.month}/{d.day}/{d.year}',
'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2012, 12, 21)
# 使用format(obj},其实就是调用obj的__format__方法
# obj的初始化，就是调用obj的__init__方法
# obj的输出打印，就是调用obj的__repr__方法 或者 __str__方法
print(format(d))
print(format(d, 'mdy'))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))