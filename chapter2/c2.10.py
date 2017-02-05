# 用正则表达式处理Unicode字符
import re
num = re.compile('\d+')
print(num.match('123'))

print(num.match('\u0661\u0662\u0663'))

# 应该安装第三方的正则表达式库,比如regex