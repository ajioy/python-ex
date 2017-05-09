import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
print(comment.findall(text1))

text2 = '''/* this is a 
multiline comment */
'''

print(text2)
# 无法匹配换行符
print(comment.findall(text2)) # []

# to fix problem
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# re.DOTALL让点(.)匹配包括换行符在内的任意字符
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
