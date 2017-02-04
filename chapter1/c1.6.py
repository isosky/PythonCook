# 在字典中将键映射到多个值上
d = {
    'a': [1, 2, 3, 4],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)

# before
d = {}
for key, value in d:
    if key not in d:
        d[key] = []
    d[key].append(value)

# after
d = defaultdict(list)
for key, value in d:
    d[key].append(value)
