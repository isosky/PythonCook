# 在文本中处理HTML和XML文本
import html

s = 'Elements are written as "<tag>text</tag>"'
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

