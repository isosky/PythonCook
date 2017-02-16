# 以索引-值对的形式迭代序列
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 1):
    print(idx, val)


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}:Parse error : {}'.format(lineno, e))

