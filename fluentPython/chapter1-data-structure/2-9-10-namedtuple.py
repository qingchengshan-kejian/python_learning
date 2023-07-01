from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokoyo = City('Tokyo', 'JP', 36.933, (35.68, 139.59))
print(tokoyo)
print(tokoyo.population)

# 具名元组的属性和方法
print(City._fields)

LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':', value)

