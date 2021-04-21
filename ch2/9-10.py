from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', '36.933', (35.689, 139.691))
print(tokyo)

print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', '21.935', LatLong(28.613, 77.208))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
