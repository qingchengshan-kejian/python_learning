s = '{name} has {n} messages.'
# print(s.format(name='Guido', n=37))

# name = 'Guido'
# n = 37
# print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(s.format_map(vars(a)))

