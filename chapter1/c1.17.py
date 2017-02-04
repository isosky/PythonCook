# 从字典中提取子集
# dictionary comprehension
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 200}

tech_name = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_name}
# 同样的方法,但是要慢1.6倍,可以看14.13
p2 = {key: prices[key] for key in prices.keys() & tech_name}
