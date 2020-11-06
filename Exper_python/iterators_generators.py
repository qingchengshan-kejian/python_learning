'''
i = iter('abc')
print i.next()
print i.next()
print i.next()
'''
'''
#self defined iterator
class MyIterator(object):
	"""docstring for MyIterator"""
	def __init__(self, step):
		self.step = step
	def next(self):
		"""Returns the next elment"""
		if self.step ==0:
			raise StopIteration
		self.step -= 1
		return self.step
	def __iter__(self):
		"""Returns the iterator itself."""
		return self
for el in MyIterator(4):
	print el

#iterator produces an object which can read it looply.
'''
'''
def fibonacci():
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a+b
fib = fibonacci()
print fib.next()
print fib.next()
print fib.next()

print [fib.next() for i in range(10)]
'''
'''
import tokenize
reader = open('list_comprehensions.py').next
tokens = tokenize.generate_tokens(reader)
print tokens.next()
print tokens.next()
'''

'''
def power(values):
	for value in values:
		print 'powering %s' % value
		yield value

def adder(values):
	for value in values:
		print 'adding to %s' % value
		if value % 2 == 0:
			yield value + 3
		else:
			yield value + 2

elements = [1, 4, 7, 9, 12, 19]
powers = power(elements)
res = adder(power(elements))
#for poweri in powers:
#	print poweri
for resi in res:
	print resi
'''
'''
def psychologist():
	print "Please tell me your problems"
	while True:
		answer = (yield) #wait for input info from send function.
		if answer is not None:
			if answer.endswith('?'):
				print ("Don't ask your self to much questions")
			elif 'good' in answer:
				print "A that's good, go on"
			elif 'bad' in answer:
				print "Don't be so negative"

free = psychologist()
free.next()
free.send('I feel bad')
free.send("Why I shouldn't ?")
free.send("ok then i should find what is good for me")
'''
'''
def my_generator():
	try:
		yield 'somethinng'
	except ValueError:
		yield 'dealing with the exception'
	finally:
		print "ok let's clean"
gen = my_generator()
print gen.next()
print gen.throw(ValueError('mean mean mean'))
gen.close()
'''

#generator expression
iter = (x**2 for x in range(10) if x%2 ==0)
for el in iter:
	print el









