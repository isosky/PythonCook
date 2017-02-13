# 同二进制/八进制和十六进制数打交道

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

x = -1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

print(format(2 ** 32 + x, 'b'))
print(format(2 ** 32 + x, 'x'))
