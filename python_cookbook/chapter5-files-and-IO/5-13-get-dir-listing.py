import os

# get all regular files
names = [name for name in os.listdir('somedir')
         if os.path.isfile(os.path.join('somedir', name))]

# get all dirs
dirnames = [name for name in os.listdir('somedir')
            if os.path.isdir(os.path.join('somedir', name))]

pyfiles = [name for name in os.listdir('somedir')
           if name.endswith('.py')]

# 另外一种方式
import glob
pyfiles = glob.glob('somedir/*.py')

# 又是另外一种方式
from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
           if fnmatch(name, '*.py')]