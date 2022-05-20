from nltk import data
import nltk.classify.util
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from pyecharts import Liquid
import webbrowser
import os


data.path.append('./nltk_data')

positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')

print(type(positive_fileids), len(negative_fileids))

def extract_features(word_list):
    return dict([(word, True) for word in word_list])

features_positive = []
for f in positive_fileids:
    word_list = movie_reviews.words(f)
    word_features = extract_features(word_list)
    features_positive.append((word_features, 'Positive'))

features_negative = []
for f in negative_fileids:
    word_list = movie_reviews.words(f)
    word_features = extract_features(word_list)
    features_negative.append((word_features, 'Negative'))

threshold_factor = 0.8
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))

words_train = features_positive[:threshold_positive] + \
    features_negative[:threshold_negative]

words_test = features_positive[threshold_positive:] + \
    features_negative[threshold_negative:]
print('\n训练数据集的数量：', len(words_train))
print('测试数据集的数量：', len(words_test))

classifier = NaiveBayesClassifier.train(words_train)
print('\n分类器的准确性：', nltk.classify.util.accuracy(classifier, words_test))

print('《狮子王》电影评测')
print('输入英文评测，程序会判断出正负面评论，并给出预测准确度！')
print('-----------------------------------------------------------')
review = input('请输入电影评论：')
split_words = review.split()
features = extract_features(split_words)
class_words = classifier.prob_classify(features)
sentiment = class_words.max()
print('预测正负面评价：', sentiment)
print('预测准确度：',round(class_words.prob(sentiment),2))

liquid = Liquid('电影《狮子王》评论：{} \n\n正负面评价：{} \n\n预测准确度：'.format(review,sentiment))
liquid.add('Liquid', [round(class_words.prob(sentiment), 2)],liquid_color = ['#156ACF'])
liquid.render()
webbrowser.open('file://'+os.path.realpath('render.html'))
