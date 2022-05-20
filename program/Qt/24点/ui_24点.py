# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/24点/24点.ui',
# licensing of 'E:/Personal/Python/program/Qt/24点/24点.ui' applies.
#
# Created: Sat Sep  5 18:22:31 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_1.setGeometry(QtCore.QRect(20, 30, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pbtn_1.setFont(font)
        self.pbtn_1.setObjectName("pbtn_1")
        self.pbtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_2.setGeometry(QtCore.QRect(170, 30, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pbtn_2.setFont(font)
        self.pbtn_2.setObjectName("pbtn_2")
        self.pbtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_3.setGeometry(QtCore.QRect(320, 30, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pbtn_3.setFont(font)
        self.pbtn_3.setObjectName("pbtn_3")
        self.pbtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_4.setGeometry(QtCore.QRect(470, 30, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pbtn_4.setFont(font)
        self.pbtn_4.setObjectName("pbtn_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 210, 371, 41))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "24点", None, -1))
        self.pbtn_1.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pbtn_2.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pbtn_3.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pbtn_4.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))

