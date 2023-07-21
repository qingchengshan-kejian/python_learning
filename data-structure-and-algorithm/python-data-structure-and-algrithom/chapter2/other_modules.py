import itertools
from collections import deque

dq = deque('abc')
dq.append('d')
dq.appendleft('z')
dq.extend('efg')
dq.extendleft('yxw')
print(dq)
# print(dq.pop())
# print(dq.popleft())
# print(dq.rotate(2))
dq.rotate(2)
print(dq)
print(list(itertools.islice(dq, 3, 9)))


dq2 = deque([], maxlen=3)
for i in range(6):
    dq2.append(i)
    print(dq2)


from collections import ChainMap
defaults = {
    'theme': 'Default',
    'language': 'eng',
    'showIndex': True,
    'showFooter': True
}

cm = ChainMap(defaults)
cm2 = cm.new_child({'theme': 'bluesky'})
print(cm)
print(cm2)
print(cm2['theme'])
print(cm2.pop('theme'))
print(cm2['theme'])