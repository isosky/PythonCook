# 从字符串中去掉不要的字符
# strip() lstrip() rstrip()
s = 'Hello world \n'
print(s)
print(s.strip())

t = '---------hello========='
print(t.lstrip('-'))
print(t.rstrip('='))