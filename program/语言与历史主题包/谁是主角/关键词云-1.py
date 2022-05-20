from wordcloud import WordCloud
import matplotlib.pyplot as plt
w = WordCloud(background_color='white')
w.generate_from_frequencies({'Codemao':100, "love":30,'learn':10})
w.to_file('codemao.png')

plt.imshow(w)
plt.axis('off')
plt.show()