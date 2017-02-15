# 处理无穷大和NaN
import math

a = float('inf')
b = float('-inf')
c = float('nan')

print(a)
print(b)
print(c)

print(math.isinf(a))
print(math.isnan(c))

print(a + 45)
print(a * 10)
print(10 / a)
print(a / a)

