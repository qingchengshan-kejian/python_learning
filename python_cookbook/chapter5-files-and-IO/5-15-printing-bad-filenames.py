def bad_filename(filename):
    return repr(filename)[1:-1]

# try:
#     print(filename)
# except UnicodeEncodeError:
#     print(bad_filename(filename))

import os
files = os.listdir('.')
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))