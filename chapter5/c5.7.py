# 读写压缩的数据文件
import gzip

with gzip.open('somefile', 'rt') as f:
    text = f.read()

import bz2

with bz2.open('somefile', 'rt') as f:
    text = f.read()

text = 'a'

with gzip.open('somefile', 'wt') as f:
    f.write(text)

with bz2.open('somefile', 'wt') as f:
    f.write(text)
