# 在字符串的开头或结尾处做文本匹配
filename = 'spam.txt'
filename.endswith('.txt')
filename.startswith('file:')

url = 'http://www.python.org'
url.startswith('http:')

import os

filename = os.listdir('.')
print(filename)

from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(choices)  # 会报错 需要传入turple
url.startswith(tuple(choices))

# 同样可以可用切片或者正则表达式来完成这个工作,不过前者不够优雅,后者对于这个场景来说,太笨重了
