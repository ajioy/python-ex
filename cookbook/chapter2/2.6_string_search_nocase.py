import re
import pdb
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']
# 无法修复字符串的大小写保持一致
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

# 用辅助函数修复大小写无法保持一致的问题
def matchcase(word): # 不明白这里两个函数定义
    def replace(m):
        pdb.set_trace()
        text = m.group()

        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace # 返回一个回调函数

res = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(res)

