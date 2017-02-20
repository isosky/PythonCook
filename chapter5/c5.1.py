# 读写文本数据
with open('somefile.txt', 'rt') as f:
    data = f.read()

with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)

