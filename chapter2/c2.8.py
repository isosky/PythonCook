# 编写多行模式的正则表达式
import re

comment = re.compile(r'/\*(.*)?\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a' \
'multiline comment
*/'''

print(comment.findall(text1))

print(comment.findall(text2))

# 添加换行符的支持
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# re.DOTALL
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
