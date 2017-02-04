# 通过公共键对字典列表排序
rows = [
    {'fname': 'Brian', 'lmane': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lmane': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lmane': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lmane': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# 可以用lambda来代替itemgetter
rows_by_fname = sorted(rows, key=lambda r: r['fname'])

# itemgetter比lambda更快
