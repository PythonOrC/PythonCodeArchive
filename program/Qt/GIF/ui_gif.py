# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/GIF/gif.ui',
# licensing of 'E:/Personal/Python/program/Qt/GIF/gif.ui' applies.
#
# Created: Sat Sep 26 19:20:50 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_gif(object):
    def setupUi(self, gif):
        gif.setObjectName("gif")
        gif.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(gif)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 761, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbtn_slow = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbtn_slow.setObjectName("pbtn_slow")
        self.horizontalLayout_4.addWidget(self.pbtn_slow)
        self.pbtn_pause = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbtn_pause.setObjectName("pbtn_pause")
        self.horizontalLayout_4.addWidget(self.pbtn_pause)
        self.pbtn_play = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbtn_play.setObjectName("pbtn_play")
        self.horizontalLayout_4.addWidget(self.pbtn_play)
        self.pbtn_fast = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbtn_fast.setObjectName("pbtn_fast")
        self.horizontalLayout_4.addWidget(self.pbtn_fast)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        gif.setCentralWidget(self.centralwidget)

        self.retranslateUi(gif)
        QtCore.QMetaObject.connectSlotsByName(gif)

    def retranslateUi(self, gif):
        gif.setWindowTitle(QtWidgets.QApplication.translate("gif", "PySide2与GIF", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("gif", "TextLabel", None, -1))
        self.pbtn_slow.setText(QtWidgets.QApplication.translate("gif", "减速", None, -1))
        self.pbtn_pause.setText(QtWidgets.QApplication.translate("gif", "暂停", None, -1))
        self.pbtn_play.setText(QtWidgets.QApplication.translate("gif", "播放", None, -1))
        self.pbtn_fast.setText(QtWidgets.QApplication.translate("gif", "加速", None, -1))

