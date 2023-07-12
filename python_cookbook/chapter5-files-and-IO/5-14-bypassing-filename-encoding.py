import sys

print(sys.getfilesystemencoding())

# write a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

import os
print(os.listdir('.'))
print(os.listdir(b'.'))
