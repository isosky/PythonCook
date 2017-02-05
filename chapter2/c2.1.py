# 针对任意多的分隔符拆分字符串
# split()只能处理比较简单的情况.
line = 'asdf fjdk; afed, fjek,asdf,    too'

import re

print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
