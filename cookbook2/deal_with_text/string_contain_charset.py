#!/usr/bin/python

def containsAny(seq, aset):
	"""check if seq contains items in aset """
	for c in seq:
		if c in aset: 
			return True
	return False

# another method 

def containsAny2(seq, aset):
	for item in filter(aset.__contains__, seq):
		return True
	return False

# another method
def containsAny3(seq, aset):
	return bool(set(aset).intersection(seq))

seq = 'hello world!'
aset = ['x', 'y', 'z']
aset2 = ['o', 'p', 'q']

print(containsAny(seq, aset2))
print(containsAny2(seq, aset))
print(containsAny3(seq, aset2))


