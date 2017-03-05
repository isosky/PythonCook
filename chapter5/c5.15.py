# 打印无法解码的文件名
import os
def bad_filename(filename):
    return repr(filename)[1:-1]


filename = 's'
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))

files = os.listdir('/')
print(files)

