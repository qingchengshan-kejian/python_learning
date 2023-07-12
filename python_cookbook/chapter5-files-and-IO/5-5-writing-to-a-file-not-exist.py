# with open('somefile', 'wt') as f:
#     f.write('hello\n')

# xt参数，指定文件必须不存在
# x创建新文件
# with open('somefile', 'xt') as f:
#     f.write('hello\n')

import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('hello\n')
else:
    print('file already exists!')


