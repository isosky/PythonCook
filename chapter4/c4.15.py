# 合并多个有序序列,再对整个有序序列进行迭代
import heapq

a = [1, 4, 7, 10]
b = [2, 5, 8, 11]

for c in heapq.merge(a,b):
    print(c)

# heapq.merge 对所有提供的序列都不会做一次性读取。这意味着可以利用它处理非常长的序列，而开销却非常小。