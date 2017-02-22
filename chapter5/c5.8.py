# 对固定大小的记录进行迭代
from functools import partial

RECODE_SIZE = 32

with open('somefile', 'rb') as f:
    records = iter(partial(f.read(), RECODE_SIZE), b'')
    for r in records:
        print(r)
