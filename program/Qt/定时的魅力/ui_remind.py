# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/定时的魅力/remind.ui',
# licensing of 'E:/Personal/Python/program/Qt/定时的魅力/remind.ui' applies.
#
# Created: Sat Oct 17 18:31:19 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Remind(object):
    def setupUi(self, Remind):
        Remind.setObjectName("Remind")
        Remind.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Remind)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        Remind.setCentralWidget(self.centralwidget)

        self.retranslateUi(Remind)
        QtCore.QMetaObject.connectSlotsByName(Remind)

    def retranslateUi(self, Remind):
        Remind.setWindowTitle(QtWidgets.QApplication.translate("Remind", "定时提醒器", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Remind", "TextLabel", None, -1))

