# 字符串连接及合并
# join()
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)

c = 'hehe'
print('{} {}'.format(a, b))
# +比join慢很多

data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

print(a + ':' + b + ':' + c)  # ugly
print(':'.join([a, b, c]))  # still ugly
print(a, b, c, sep=';')  # better

'''
# version1
f.write(chunk1+chunk2)

#version2
f.write(chunk1)
f.write(chunk2)
'''


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())

for part in sample():
    # f.write(part)
    pass

def combine(source,maxsize):
    parts =[]
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size>maxsize:
            yield ''.join(parts)
            parts=[]
            size=0
    yield ''.join(parts)

for part in combine(sample(),32768):
    #f.write(part)
    pass

