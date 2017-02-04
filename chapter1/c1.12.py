# 找出序列中出现次数最多的元素
words = ['look', 'into', 'my', 'eyes', 'look']

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['eyes', 'in', 'my']

word_counts.update(morewords)
# Counter可以与数据运算操作结合起来使用
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
c = a + b
print(c)
c = a - b
print(c)
