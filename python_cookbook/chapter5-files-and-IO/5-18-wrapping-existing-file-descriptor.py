# open a low-level file descriptor
import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

# create a file object, but don't close underlying fd when donw
f = open(fd, 'wt', closefd=False)