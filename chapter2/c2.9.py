# 将Unicode文本统一表示为规范形式
s1 = 'Spciy Jalape\u00f1o'
s2 = 'Spciy Jalapen\u0303o'

print(s1)
print(s2)

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)

