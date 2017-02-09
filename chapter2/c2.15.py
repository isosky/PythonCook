# 给字符串中的变量名做差值处理

s = '{name} has {n} message.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))

