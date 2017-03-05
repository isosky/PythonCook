# 获取目录内容的列表
import os

names = os.listdir('somedir')

import os.path

names = [name for name in os.listdir('somdedir')
         if os.path.isfile(os.path.join('somedir', name))]

pyfiles = [name for name in os.listdir('somedir')]
import glob

pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch

pyfiles = [name for name in os.listdir('somedir') if fnmatch(name, '*.py')]

