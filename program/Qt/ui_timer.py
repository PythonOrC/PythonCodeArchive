# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/timer.ui',
# licensing of 'E:/Personal/Python/program/Qt/timer.ui' applies.
#
# Created: Sat Oct 26 19:27:09 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Timer(object):
    def setupUi(self, Timer):
        Timer.setObjectName("Timer")
        Timer.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Timer)
        self.centralwidget.setObjectName("centralwidget")
        self.lcd_timer = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_timer.setGeometry(QtCore.QRect(250, 40, 221, 121))
        self.lcd_timer.setObjectName("lcd_timer")
        self.pb_start = QtWidgets.QPushButton(self.centralwidget)
        self.pb_start.setGeometry(QtCore.QRect(180, 180, 75, 23))
        self.pb_start.setObjectName("pb_start")
        self.pb_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pb_stop.setGeometry(QtCore.QRect(430, 180, 75, 23))
        self.pb_stop.setObjectName("pb_stop")
        Timer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Timer)
        QtCore.QMetaObject.connectSlotsByName(Timer)

    def retranslateUi(self, Timer):
        Timer.setWindowTitle(QtWidgets.QApplication.translate("Timer", "MainWindow", None, -1))
        self.pb_start.setText(QtWidgets.QApplication.translate("Timer", "Start", None, -1))
        self.pb_stop.setText(QtWidgets.QApplication.translate("Timer", "Stop", None, -1))

