import io

s = io.StringIO()
# print(s.write('hello world\n'))

# 输出到io.StringIO()对象
print('this is a test', file=s)
print(s.getvalue())

s = io.StringIO('hello\nworld\n')
print(s.read(4))
# read 4个后，再次read则是剩下的
print(s.read())

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
