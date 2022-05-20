import nltk.classify.util
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk import data
from pyecharts import Liquid
import os
import webbrowser

data.path.append('./nltk_data')

#加载积极与消极评论
positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')
print(type(positive_fileids), len(negative_fileids))
#定义一个用于提取特征的函数
def extract_features(word_list):
    return dict([(word, True) for word in word_list])

#为积极评论贴标签
features_positive = []
for f in positive_fileids:
    word_list = movie_reviews.words(f)
    word_features = extract_features(word_list)
    features_positive.append((word_features, "Positive"))

features_negative = []
for f in negative_fileids:
    word_list = movie_reviews.words(f)
    word_features = extract_features(word_list)
    features_negative.append((word_features, "Negative"))

#分成训练数据集（80%）和测试数据集（20%）
threshold_factor=0.8
threshold_positive=int(
    threshold_factor * len(features_positive))
threshold_negative=int(
    threshold_factor * len(features_negative))

words_train=features_positive[:threshold_positive] + \
features_negative[:threshold_negative]

words_test=features_positive[threshold_positive:] + \
features_negative[threshold_negative:]
print("\n训练数据集的数量:", len(words_train))
print("测试数据集的数量:", len(words_test))

# 训练朴素贝叶斯分类器
classifier=NaiveBayesClassifier.train(words_train)
print("\n分类器的准确性:", nltk.classify.util.accuracy(
    classifier, words_test))

# 对狮子王电影的英文评论进行预测
# 提示信息
print("少年，《狮子王》电影英文评论，敢来挑战吗!")
print("游戏规则是：只需输入英文评论，程序会判断出正负面评价，并给出预测准确值!")
print("---------------------------------------------------------------------")
# 输入评论
review=input("请在这里，输入狮王辛巴的电影评论: ")

split_words=review.split()
features=extract_features(split_words)
class_words=classifier.prob_classify(features)

sentiment=class_words.max()
print("预测正负面评价:", sentiment)
print("预测准确度:", round(class_words.prob(sentiment), 2))

liquid= Liquid("电影《狮子王》评论 : {}.\n\n正负面评价：{} \n\n预测准确度：".format(review, sentiment))
liquid.add("Liquid", [round(class_words.prob(sentiment), 2)],
           liquid_color=['#156ACF'],)
liquid.render()
webbrowser.open("file://" + os.path.realpath("render.html"))
