#!/usr/bin/python
from collections import deque

#first e.g.
'''ue
def search(lines, pattern, histroy = 5):
	previous_lines = deque(maxlen = histroy)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

#Example use on a file
if __name__ == '__main__':
	with open('somefile.txt') as f:
		#g=search(f, 'python', 5)
		#print(next(g))
		#print(next(g))
		for line, previous_lines in search(f, 'python', 5):
			for pline in previous_lines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)

'''

#some commands
q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)
q.append(5)
print(q)

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)

q.appendleft(4)
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)
