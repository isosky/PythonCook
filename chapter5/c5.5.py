# 对已不存在的文件执行写入操作
import os

with open('somefile', 'xt') as f:
    f.write('hh')

if not os.path.exists('somefile'):
    with open("somefile", 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')
