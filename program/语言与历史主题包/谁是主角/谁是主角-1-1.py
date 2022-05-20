import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

with open('西游记关键词数据.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mask = mpimg.imread('图片素材.png') * 255
print(mask)

w = WordCloud(background_color='white',
              font_path='fangzheng.TTF', max_font_size=1000, width=1200, height=1200, mask=mask, contour_width=2.5,contour_color="orange")
w.generate_from_frequencies(data)
w.to_file('西游记.png')

plt.imshow(w)
plt.axis('off')
plt.show()
