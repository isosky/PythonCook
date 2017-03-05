# 为已打开的文件添加或修改编码方式
import urllib.request
import io
import sys

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)

