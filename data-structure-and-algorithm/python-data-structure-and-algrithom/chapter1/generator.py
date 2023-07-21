# compares the running tiem of a list compared to a generator
import time
# genrator function creates an iterator of odd numbers between n and m

def oddGen(n, m):
    while n < m:
        yield n
        n += 2


# builds a list of odd nubmers between a and m
def oddList(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

# the time it takes to perform sum on an iterator
t1 = time.time()
sum(oddGen(1, 1000000))
print("Time to sum an iterator: %f" % (time.time() - t1))

# the time it takes to build and sum a list
t2 = time.time()
sum(oddList(1, 1000000))
print("Time to sum a list: %f" % (time.time() - t2))

# 生成器表达式
lst1 = [1, 2, 3, 4]
gen1 = (10**i for i in lst1)
print(gen1)
for x in gen1: print(x)
