# 检测文件是否存在
import os

print(os.path.exists('data'))
print(os.path.isfile('data'))
print(os.path.isdir('data'))
print(os.path.islink('data'))
print(os.path.realpath('data'))
