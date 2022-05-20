from wordcloud import WordCloud
import matplotlib.pyplot as plt
import codecs
import jieba
import jieba.analyse


with codecs.open("西游记.txt", 'r', 'utf-8-sig') as f:
    content = f.read()


tags = jieba.analyse.extract_tags(
    content, topK=40, withWeight=True)  # 从文中提取20个关键词，带权重
print(tags)
print(dict(tags))
w = WordCloud(background_color='white', font_path='fangzheng.TTF',
              max_font_size=1000)  # 生成一个词云对象
w.generate_from_frequencies(dict(tags))  # 传入字典，生成词云
w.to_file('西游记.png')  # 把词云存入文件


plt.imshow(w)  # 把要展示的词云对象传入
plt.axis('off')  # 关闭坐标轴的显示
plt.show()  # 展示图像
