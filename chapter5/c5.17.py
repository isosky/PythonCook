# 将字节数据写入文本文件
import sys

sys.stdout.write(b'Hello\n')
sys.stdout.buffer.write(b'Hello\n')
