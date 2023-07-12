import os

print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))
print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/etc/passwd'))
print(os.path.islink('/usr/local/bin/python3'))
print(os.path.relpath('/usr/local/bin/python3'))


print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))

import time
print(time.ctime(os.path.getmtime('/etc/passwd')))