# 检查字符串开头或结尾
filename = "spam.txt"
res = filename.endswith('.txt')
print(res) # True
res = filename.startswith('file:')
print(res) # False
url = "http://www.python.org"
res = url.startswith("http:")
print(res) # True

import os
filenames = os.listdir('.')
print(filenames) # 当前目录下的所有文件
res = [name for name in filenames if name.endswith(('.c', '.py'))]
print(res)
res = any(name.endswith('.py') for name in filenames)
print(res)

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'ftp:', 'https:')):
        print("urlopen:")
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
url = "https://www.baidu.com"
# startswith函数的参数是tuple类型
url.startswith(tuple(choices))

res = read_data(url)
#print(res)

# 切片的试工检查字符串开头和结尾
filename = "spam.txt"
print(filename[-4:] == ".txt")
res = url[:5] == "http:" or url[:6] == "https:"
print(res)

import re
res = re.match("http:|https:|ftp:", url)
print(res)

# 检查某个文件夹中是否存在指定的文件类型
if (any(name.endswith('py') for name in os.listdir("."))):
    print(True)
else:
    print(False)
