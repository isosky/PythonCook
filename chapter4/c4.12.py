# 在不同的容器中进行迭代
from itertools import chain

a = [1, 2, 3, 4]
b = ['a', 'b', 'c']

# better
for x in chain(a, b):
    print(x)

# inefficent
for x in a + b:
    print(x)
