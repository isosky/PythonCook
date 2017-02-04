# 让字典保持有序
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])

# 占的空间是正常的链表的两倍