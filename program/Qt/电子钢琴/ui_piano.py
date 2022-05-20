# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/电子钢琴/piano.ui',
# licensing of 'E:/Personal/Python/program/Qt/电子钢琴/piano.ui' applies.
#
# Created: Sat Sep 19 18:56:59 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Piano(object):
    def setupUi(self, Piano):
        Piano.setObjectName("Piano")
        Piano.resize(520, 700)
        self.centralwidget = QtWidgets.QWidget(Piano)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_keyboard = QtWidgets.QLabel(self.centralwidget)
        self.lb_keyboard.setGeometry(QtCore.QRect(10, 10, 500, 250))
        self.lb_keyboard.setObjectName("lb_keyboard")
        self.label_b = QtWidgets.QLabel(self.centralwidget)
        self.label_b.setGeometry(QtCore.QRect(390, 190, 40, 40))
        self.label_b.setObjectName("label_b")
        self.label_ch = QtWidgets.QLabel(self.centralwidget)
        self.label_ch.setGeometry(QtCore.QRect(455, 190, 40, 40))
        self.label_ch.setObjectName("label_ch")
        self.label_a = QtWidgets.QLabel(self.centralwidget)
        self.label_a.setGeometry(QtCore.QRect(330, 190, 40, 40))
        self.label_a.setObjectName("label_a")
        self.label_g = QtWidgets.QLabel(self.centralwidget)
        self.label_g.setGeometry(QtCore.QRect(270, 190, 40, 40))
        self.label_g.setObjectName("label_g")
        self.label_f = QtWidgets.QLabel(self.centralwidget)
        self.label_f.setGeometry(QtCore.QRect(200, 190, 40, 40))
        self.label_f.setObjectName("label_f")
        self.label_e = QtWidgets.QLabel(self.centralwidget)
        self.label_e.setGeometry(QtCore.QRect(150, 190, 40, 40))
        self.label_e.setObjectName("label_e")
        self.label_d = QtWidgets.QLabel(self.centralwidget)
        self.label_d.setGeometry(QtCore.QRect(90, 190, 40, 40))
        self.label_d.setObjectName("label_d")
        self.label_c = QtWidgets.QLabel(self.centralwidget)
        self.label_c.setGeometry(QtCore.QRect(25, 190, 40, 40))
        self.label_c.setObjectName("label_c")
        self.pbtn = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn.setGeometry(QtCore.QRect(10, 250, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbtn.setFont(font)
        self.pbtn.setObjectName("pbtn")
        self.label_music = QtWidgets.QLabel(self.centralwidget)
        self.label_music.setGeometry(QtCore.QRect(10, 290, 501, 401))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_music.setFont(font)
        self.label_music.setAlignment(QtCore.Qt.AlignCenter)
        self.label_music.setObjectName("label_music")
        Piano.setCentralWidget(self.centralwidget)

        self.retranslateUi(Piano)
        QtCore.QMetaObject.connectSlotsByName(Piano)

    def retranslateUi(self, Piano):
        Piano.setWindowTitle(QtWidgets.QApplication.translate("Piano", "电子钢琴", None, -1))
        self.lb_keyboard.setText(QtWidgets.QApplication.translate("Piano", "TextLabel", None, -1))
        self.label_b.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.label_ch.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.label_a.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.label_g.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.label_f.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.label_e.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.label_d.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.label_c.setText(QtWidgets.QApplication.translate("Piano", "", None, -1))
        self.pbtn.setText(QtWidgets.QApplication.translate("Piano", "选择乐谱", None, -1))
        self.label_music.setText(QtWidgets.QApplication.translate("Piano", "乐谱", None, -1))

