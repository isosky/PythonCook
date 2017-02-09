# 利用shell通配符做字符串匹配
# fnmatch fnmatch() fnmatchcase()

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '.txt'))
print(fnmatch('foo.txt', '?oo.txt'))

print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
# fnmatch的匹配模式采用的大小写区分规则和底层文件系统相同

