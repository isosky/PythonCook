# 从字节串中打包和解包大整数

data = b'\x00\x123V\x00x\x90\xab\x00\xcd\xef\x01\x004\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

import struct

hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)
