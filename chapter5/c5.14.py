# 绕过文件名编码
import sys,os

sys.getfilesystemencoding()
os.listdir(b'.')
