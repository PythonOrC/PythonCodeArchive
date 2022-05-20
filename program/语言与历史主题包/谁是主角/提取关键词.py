import codecs
import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with codecs.open('西游记.txt','r', 'utf-8-sig') as f:
    content = f.read()

tags = jieba.analyse.extract_tags(content, topK=50, withWeight=True)


w = WordCloud(background_color='white',font_path='fangzheng.TTF',max_font_size=1000)
w.generate_from_frequencies(dict(tags))
w.to_file('西游记.png')

plt.imshow(w)
plt.axis('off')
plt.show()
