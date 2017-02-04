# 找到最大或者最小的N个元素
import heapq

nums = [1, 2, 3, 4, 5, 8, 2, 23, 7, -4, 18, 23, 42, 31, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 40, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensice = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensice)

# 如果在集合中,N相对较小,为更好的性能可以采取以下的做法:
heap = list(nums)
heapq.heapify(heap)
print(heap)
