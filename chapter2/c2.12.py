# 文本过滤和清理

s = 'python\fis\tawesome\n'
print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(a)
print(b.translate(cmb_chrs))

digitmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if
            unicodedata.category(chr(c)) == 'Nd'}

print(len(digitmap))  # todo 书上的长度是460
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# replace 比translate要快