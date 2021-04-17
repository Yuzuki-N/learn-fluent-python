symbols = '@#$%^&*'
x = tuple(ord(symbol) for symbol in symbols)
print(x)
import array
y = array.array('I', (ord(symbol) for symbol in symbols))
print(y)