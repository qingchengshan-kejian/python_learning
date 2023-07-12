from functools import partial

RECORD_SIZE = 32

with open('somefile.data', 'rb') as f:
    # 转为可迭代对象
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)