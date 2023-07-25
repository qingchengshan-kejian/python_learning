# mymodule.py

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def bar(self):
        print('B.bar')

# 一个模块文件，拆分多个文件
# mymodule/
#   __init__.py
#   a.py
#   b.py

# a.py
class A:
    def spam(self):
        print('A.spam')

# b.py
from .a import A
class B(A):
    def bar(self):
        print('B.bar')

# __init__.py
from .a import A
from .b import B

# 按照上述目录结构和文件编写规范，虽然拆分多个文件，但是还是可以作为一个完整的模块来使用。
import mymodule
a = mymodule.A()
a.spam()
b = mymodule.B()
b.bar()