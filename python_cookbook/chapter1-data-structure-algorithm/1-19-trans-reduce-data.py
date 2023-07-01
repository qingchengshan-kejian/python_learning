# nums = [1, 2, 3, 4, 5]
# s = sum(x * x for x in nums)
# print(s)

# determine if any .py files exist in a firectory
# import os
# files = os.listdir('.')
# if any(name.endswith('.py') for name in files):
#     print('There be python!')
# else:
#     print('Sorry, no python.')

# output a tuple as csv
# s = ('ACME', 50, 123.45)
# print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

