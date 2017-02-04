# 筛选序列中的元素
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

temp1 = [n for n in mylist if n > 0]

temp2 = [n if n > 0 else 0 for n in mylist]

values = ['1', '2', '3', '-4', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))

print(ivals)

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

address = [n['address'] for n in rows]
print(address)

counts = [0, 3, 10, 4, 1, 7, 6, 11]

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(address,more5)))
