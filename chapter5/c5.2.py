# 将输出重定向到文件中
with open('somefile.txt', 'rt') as f:
    print('hello world ', file=f)
