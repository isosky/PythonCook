# 以固定的列数重新格式化文本
import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes," \
    "the eyes, not around the eyes, don't look around the eyes " \
    "look into my eyes, you'er under."

print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent=''))
print(textwrap.fill(s, 40, subsequent_indent=''))

import os
print(os.get_terminal_size().columns)

