# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Personal/Python/python_work/hello.ui',
# licensing of 'C:/Personal/Python/python_work/hello.ui' applies.
#
# Created: Sat Aug 10 17:16:39 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_hello(object):
    def setupUi(self, hello):
        hello.setObjectName("hello")
        hello.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(hello)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 110, 151, 111))
        self.label.setObjectName("label")
        hello.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hello)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        hello.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hello)
        self.statusbar.setObjectName("statusbar")
        hello.setStatusBar(self.statusbar)

        self.retranslateUi(hello)
        QtCore.QMetaObject.connectSlotsByName(hello)

    def retranslateUi(self, hello):
        hello.setWindowTitle(QtWidgets.QApplication.translate("hello", "Hello", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("hello", "Hello Codemao", None, -1))

