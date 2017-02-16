# 跳过可迭代对象中的前一部分的元素
# with open('/etc/passwd') as f:
#     for line in f:
#         print(line, end='')

from itertools import dropwhile

# with open('/etc/passwd') as f:
#     for line in dropwhile(lambda line: line.startwith('#'), f):
#         print(line, end='')

from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
