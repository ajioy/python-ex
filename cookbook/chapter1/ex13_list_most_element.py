# 序列中出现次数最多的元素
# 词频
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)

top_three = word_counts.most_common(3)
print(top_three) #[('eyes', 8), ('the', 5), ('look', 4)] 
print(word_counts['the'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# 手动增加计数
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes']) # 9

word_counts.update(morewords)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

c = a + b
print(c)

d = a - b
print(d)
