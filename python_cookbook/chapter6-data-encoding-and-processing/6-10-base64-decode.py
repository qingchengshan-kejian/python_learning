# some byte data
s = b'hello'
import base64

# encode
a = base64.b64encode(s)
print(a)
print(base64.b64decode(a))