# 查找和替换文本
text = 'yeah,but no, but yeah,but no,but yeah'
text.replace('yeah', 'yep')

text = 'Toady is 11/27/2012. PyCon starts 3/13/2013'

import re

re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

datepat=re.compile(r'(\d+)/(\d+)/(\d+)')

newtext,n=datepat.subn(r'\3-\1-\2',text)
print(n)