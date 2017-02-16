# 对迭代器做切片操作
def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# c[10:20]
import itertools

for x in itertools.islice(c, 10, 20):
    print(x)
