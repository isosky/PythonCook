# 文本模式的匹配和查找
import re

text1 = '11/27/2012'
text2 = 'Nov 27,2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.match(text2))
text = 'Toady is 11/27/2012. PyCon starts 3/13/2013'
print(datepat.findall(text))

