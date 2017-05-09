s = ' hello, ajioy \n'
# strip(), lstrip(), rstrip(),删除开始或结尾的字符，默认空白字符
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello======='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))

# strip()方法对中间的字符不会产生影响
s = ' hello           ajioy \n'
print(s.strip())
print(s.replace(' ', ''))
import re
# 把多个空格化为一个
print(re.sub('\s+', ' ', s))

# 配合strip()从文件中读取多行数据
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
