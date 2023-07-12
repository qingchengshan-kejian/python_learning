import os

path = '/Users/yue/data/data.csv'
print(os.path.basename(path))

print(os.path.basename(path))

print(os.path.join('tmp', 'data', os.path.basename(path)))

path = '~/data/data.csv'
print(os.expanduser(path))

print(os.path.splitext(path))


