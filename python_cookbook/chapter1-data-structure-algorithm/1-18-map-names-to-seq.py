from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)

print(sub.addr)
print(sub.joined)

print(len(sub))

addr, joined = sub
print(addr)
print(joined)
