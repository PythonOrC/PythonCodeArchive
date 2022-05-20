# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/Creative/Minecraft Potion Ingredient List/potion.ui',
# licensing of 'E:/Personal/Python/Creative/Minecraft Potion Ingredient List/potion.ui' applies.
#
# Created: Thu Nov 26 19:12:03 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Ui_potion(object):
    def setupUi(self, potion):
        potion.setObjectName("potion")
        potion.resize(291, 131)
        self.centralwidget = QWidget(potion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(16, 10, 261, 51))
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(20, 70, 261, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(20, 100, 261, 21))
        self.pushButton.setObjectName("pushButton")
        potion.setCentralWidget(self.centralwidget)

        self.retranslateUi(potion)
        QMetaObject.connectSlotsByName(potion)

    def retranslateUi(self, potion):
        potion.setWindowTitle(QApplication.translate("potion", "Potion Ingredients", None, -1))
        self.label.setText(QApplication.translate("potion", "TextLabel", None, -1))
        self.pushButton.setText(QApplication.translate("potion", "PushButton", None, -1))