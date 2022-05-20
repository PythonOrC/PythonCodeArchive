import random
import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *  
from ui_word import Ui_word
from time import localtime

class Word(QMainWindow, Ui_word):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.file = None
        
        self. words = {}

        self.word = ''
        self.mon, self.mday, self.hour, self.minute = str(localtime().tm_mon), str(localtime().tm_mday), str(localtime().tm_hour), str(localtime().tm_min)
        if len(self.minute) == 1:
            self.minute = '0'+self.minute
        if len(self.hour) == 1:
            self.hour = '0'+self.hour
        if len(self.mday) == 1:
            self.mday = '0'+self.mday
        if len(self.mon) == 1:
            self.mon = '0'+self.mon

        self.pb_submit.clicked.connect(self.verify)
        self.pb_file.clicked.connect(self.select_file)
        self.show()
    
    def select_file(self):
        file_path = QFileDialog.getOpenFileName(caption = '选择单词文件', filter = '(*.txt)')
        if file_path[0]:
            self.file = file_path[0]
            self.lb_file_path.setText(self.file)
            self.get_words()
        else:
            QMessageBox.warning(self, '注意', '请重新选择单词文件')

    def get_words(self):
        self.words = {}
        with open(self.file,'r',encoding = 'utf-8-sig') as f:
            words = f.read()
        try:
            words = words.strip().split('\n')
            for word in words:
                word, meanings= word.split(':')
                meanings = meanings.split('；')
                self.words[word.strip()] = meanings
            self.correct_count = 0
            self.words_count = len(self.words)
            self.get_question()
        except:
            QMessageBox.warning(self,'注意','内容为空或格式有误，请重新选择文件')

    def get_question(self):
        if len(self.words) == 0:
            QMessageBox.information(self,'','单词总数{}个， 回答正确{}个，正确率为{}%'.format(self.words_count, self.correct_count, int(self.correct_count/self.words_count)*100))
            self.lb_file_path.setText = ('')
            self.lb_question.setText = ('')
            self.word = ''
            self.words = {}
        else:
            self.meaning = random.choice(list(self.words.keys()))
            self.word = self.words.pop(self.meaning)
            self.lb_question.setText(self.meaning)

    def verify(self):
        if self.word:
            answer = self.le_answer.text()
            if answer != '':
                if answer in self.word:
                    QMessageBox.information(self,'','回答正确')
                    self.correct_count += 1
                else:
                    QMessageBox.information(self, '', '回答错误')

                with open(f'{self.mon}-{self.mday} {self.hour}{self.minute} result.txt', 'a+') as f:
                    f.write(f"{self.meaning}的意思是“{'；'.join(self.word)}”，你的回答是{answer}\n\n")

                self.get_question()
                self.le_answer.clear()
                
            else:
                QMessageBox.warning(self,'注意','请输入你的回答')
        else:
            QMessageBox.warning(self,'注意','请先准备好单词')

    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Return:
            self.verify()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Word()
    sys.exit(app.exec_())
