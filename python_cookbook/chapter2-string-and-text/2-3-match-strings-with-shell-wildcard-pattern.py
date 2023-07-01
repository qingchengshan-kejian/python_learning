from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt', '?oo.txt'))

print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
names_match = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(names_match)