a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# find keys in common
common_keys = a.keys() & b.keys()
print(common_keys)

# find keys in a that are not in b
keys_in_a_not_in_b = a.keys() - b.keys()
print(keys_in_a_not_in_b)

# find key-value pairs in common
key_value_common = a.items() & b.items()
print(key_value_common)

# make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)
