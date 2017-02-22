# 处理路径名
import os

path = '/Users/beazley/Data/data.csv'
os.path.basename(path)
os.path.dirname(path)

os.path.join('tmp', 'data', os.path.basename(path))

path = '~/Data/data.csv'
os.path.expanduser(path)

