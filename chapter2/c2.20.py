# 在字节串上执行文本操作
data = b'Hello World'
print(data[0:5])

print(data.startswith(b'Hello'))

print(data.split())

data = bytearray(b'Hello World')
print(data[0:5])

print(data.startswith(b'Hello'))

print(data.split())
