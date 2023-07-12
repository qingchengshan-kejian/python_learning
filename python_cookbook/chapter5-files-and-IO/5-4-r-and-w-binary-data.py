# with open('somfile.bin', 'rb') as f:
#     data = f.read()
# # rb  b for binary
#
# with open('somefile.bin', 'wb') as f:
#     f.write(b'this')

# t = 'hello world'
# for c in t:
#     print(c)
#
# # Byte string
# b = b'hello world'
# for c in b:
#     print(c)

# with open('somefile.bin', 'rb') as f:
#     data = f.read(16)
#     text = data.decode('utf-8')
#
# with open('somefile.bin', 'wb') as f:
#     text = 'hello world'
#     f.write(text.encode('utf-8'))

# import array
# nums = array.array('i', [1, 2, 3, 4])
# # 'i' for signed int
# print(nums)
# with open('data.bin', 'wb') as f:
#     f.write(nums)

import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)

