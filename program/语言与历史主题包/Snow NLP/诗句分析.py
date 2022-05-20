from snownlp import SnowNLP, summary
from pyecharts import Line
import webbrowser
import os

with open('滚滚长江东逝水.txt','r', encoding='utf-8-sig') as txt:
    text = txt.readlines()

sen_score = {}
sentiment = []
poem = []

for i in text:
    a1 = SnowNLP(i)
    a2 = a1.sentiments
    sentiment.append(a2)
    poem.append(i)
    sen_score[a2] = i
print(sen_score)
print(poem)
print(sentiment)

b = sorted(sentiment)
print(b)

print(b[0],sen_score[b[0]])
print(b[-1], sen_score[b[-1]])

s = ' '.join(text)
print(s)

t = SnowNLP(s)
print(t.summary(1))

n = []
for i in poem:
    n.append(i[0:4])

line = Line('滚滚长江东逝水', '明状元-杨慎')
line.add('诗词之美', n, sentiment, is_label_show=False, mark_point=['max', 'min'])
line.render()

webbrowser.open("file://" + os.path.realpath('render.html'))
