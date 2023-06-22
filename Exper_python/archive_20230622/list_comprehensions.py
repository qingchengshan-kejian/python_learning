
'''
numbers = range(10)
size = len(numbers)
evens = []
i = 0
while i < size:
	if i%2 == 0:
		evens.append(i)
	i += 1
print evens
'''
#replaced by
'''
evens = [i for i in range(10) if i % 2 ==0]
print evens
'''
'''
i = 0
seq = ["one", "two", "three"]
for element in seq:
	seq[i] = '%d:%s' %(i, seq[i])
	i += 1

print seq
'''
#replaced by
seq = ["one", "two", "three"]
for i, element in enumerate(seq):
	seq[i] = '%d:%s' %(i, seq[i])
print seq

