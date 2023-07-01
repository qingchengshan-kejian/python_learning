mylist = [1, 4, -5, 10, -7, 2, 3, -1]
a = [n for n in mylist if n > 0]
print(a)

b = [n for n in mylist if n < 0]
print(b)

pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)