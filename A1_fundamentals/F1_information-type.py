Str = str('Hello World')
Int = int(10)
Float = float(100.5)
Complex = complex(1j)
List = list(('B', 'A'))
Tuple = tuple(('A', 'B'))
Range = range(6)
Dictionary = dict(name = 'Kelson', age = 24)
Set = set(('A', 'B', 'C'))
Bool = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
MemoryView = memoryview(bytes(5))

print(Str, Int, Float, Complex, List, Tuple, Range, Dictionary, Set, Bool, Bytes, ByteArray, MemoryView)

from datetime import datetime
data = datetime.today().date()
print(data)

print(type(Str), type(Int), type(Float), type(Complex), type(List), type(Tuple), type(Range), type(Dictionary), type(Set), type(Bool), type(Bytes), type(ByteArray), type(MemoryView))
