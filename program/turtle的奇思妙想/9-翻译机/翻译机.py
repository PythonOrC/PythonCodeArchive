import turtle
import webbrowser
import requests
import json
pen = turtle.Pen()
screen = turtle.Screen()

while True:
    word = screen.textinput('翻译窗口', '输入你想查找的词')
    if word == "QUIT":
        exit()
    pen.home()
    screen.clear()
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    data = {
        'i': word,
        'doctype': 'json'
    }
    sent_content = requests.post(url, data=data)
    result = sent_content.json()['translateResult'][0][0]['tgt']
    pen.write(result, True, "center", ("Arial", 20, "bold"))
    with open('book.txt', 'a') as f:
        f.write(sent_content.json()['translateResult'][0][0]['tgt'] +
                ' ' + sent_content.json()['translateResult'][0][0]['src']+'\n')
turtle.done()
