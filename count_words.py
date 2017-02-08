import  codecs
import  jieba
import  os
from collections import Counter

all_words = []
for filename in os.listdir('test'):
    with open('test/'+filename) as f:
        text = f.read()
        data = jieba.cut(text)
        all_words.extend(set(data))

count = Counter(all_words)
result = sorted(count.items(),key = lambda x:x[1],reverse = True)
for word in result:
    print(word[0],word[1])
