import pickle

data = ... # some python object
f = open('somefile', 'wb')
# dump an object to a file
pickle.dump(data, f)

# dump an object to a string
s = pickle.dumps(data)

# restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)

# restore from a string
data = pickle.loads(s)