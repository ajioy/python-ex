import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
# 贪婪模式匹配，尽可能长的匹配
print(str_pat.findall(text2))

# 非贪婪匹，尽可能短的匹配
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))


