from struct import *

# store as byte data
packed_data = pack('iif', 12, 21, 21.5)
print(packed_data)

# show the data
unpack_data = unpack('iif', packed_data)
print(unpack_data)
