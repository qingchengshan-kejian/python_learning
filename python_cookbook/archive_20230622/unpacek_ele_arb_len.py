#!/usr/bin/python

#use 'star expressions'
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

print(name, email, phone_numbers)

#anther e.g.
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing, current)

#another e.g.
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)

for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)

#another e.g.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)

#another e.g.
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)

#another e.g.
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head, tail)

def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head

print(sum(items))


