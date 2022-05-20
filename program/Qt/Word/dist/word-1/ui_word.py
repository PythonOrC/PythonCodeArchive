# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/Word/word.ui',
# licensing of 'E:/Personal/Python/program/Qt/Word/word.ui' applies.
#
# Created: Sat Oct  5 17:26:13 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_word(object):
    def setupUi(self, word):
        word.setObjectName("word")
        word.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(word)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_file_path = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lb_file_path.setFont(font)
        self.lb_file_path.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_file_path.setObjectName("lb_file_path")
        self.verticalLayout.addWidget(self.lb_file_path)
        self.pb_file = QtWidgets.QPushButton(self.centralwidget)
        self.pb_file.setObjectName("pb_file")
        self.verticalLayout.addWidget(self.pb_file)
        self.lb_question = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lb_question.setFont(font)
        self.lb_question.setText("")
        self.lb_question.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_question.setObjectName("lb_question")
        self.verticalLayout.addWidget(self.lb_question)
        self.le_answer = QtWidgets.QLineEdit(self.centralwidget)
        self.le_answer.setObjectName("le_answer")
        self.verticalLayout.addWidget(self.le_answer)
        self.pb_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pb_submit.setObjectName("pb_submit")
        self.verticalLayout.addWidget(self.pb_submit)
        word.setCentralWidget(self.centralwidget)

        self.retranslateUi(word)
        QtCore.QMetaObject.connectSlotsByName(word)

    def retranslateUi(self, word):
        word.setWindowTitle(QtWidgets.QApplication.translate("word", "MainWindow", None, -1))
        self.lb_file_path.setText(QtWidgets.QApplication.translate("word", "单词文件路径", None, -1))
        self.pb_file.setText(QtWidgets.QApplication.translate("word", "选择单词文件", None, -1))
        self.pb_submit.setText(QtWidgets.QApplication.translate("word", "提交答案", None, -1))

