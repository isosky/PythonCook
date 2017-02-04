# 在两个字典中寻找相同点
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# find keys in common
a.keys() & b.keys()  # {'x','y'}

# find keys in a that not in b
a.keys() - b.keys()

# fine (key,value) pairs in common
a.items() & b.items()

# make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - b.keys()}
