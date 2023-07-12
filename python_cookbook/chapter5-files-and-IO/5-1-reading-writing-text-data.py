with open('somefile.txt', 'rt') as f:
    data = f.read()
print(data)

with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)

with open('thisfile.txt', 'wt') as f:
    f.write("line1 hello\n")
    f.write("line2 world")
