# 从序列中移除重复项且保持元素件顺序不变

# 序列中的元素是可哈希的时候可以按下面的方法来做
def deque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(deque(a)))


# 如果是不可哈希的
def deques(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
