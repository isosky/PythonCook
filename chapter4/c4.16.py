# 用迭代器取代while循环
CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data==b'':
            break
        print(data)


def reader(s):
    for chunk in iter(lambda : s.recv(CHUNKSIZE),b''):
        print(chunk)
