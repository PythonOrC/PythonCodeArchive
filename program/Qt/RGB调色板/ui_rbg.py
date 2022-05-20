# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/RGB调色板/rbg.ui',
# licensing of 'E:/Personal/Python/program/Qt/RGB调色板/rbg.ui' applies.
#
# Created: Sat Oct 31 23:47:30 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_RGB(object):
    def setupUi(self, RGB):
        RGB.setObjectName("RGB")
        RGB.resize(332, 387)
        self.centralwidget = QtWidgets.QWidget(RGB)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 16, 311, 361))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slider_r = QtWidgets.QSlider(self.widget)
        self.slider_r.setMaximum(255)
        self.slider_r.setOrientation(QtCore.Qt.Horizontal)
        self.slider_r.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_r.setObjectName("slider_r")
        self.horizontalLayout.addWidget(self.slider_r)
        self.label_r = QtWidgets.QLabel(self.widget)
        self.label_r.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_r.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_r.setObjectName("label_r")
        self.horizontalLayout.addWidget(self.label_r)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slider_g = QtWidgets.QSlider(self.widget)
        self.slider_g.setMaximum(255)
        self.slider_g.setOrientation(QtCore.Qt.Horizontal)
        self.slider_g.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_g.setObjectName("slider_g")
        self.horizontalLayout_2.addWidget(self.slider_g)
        self.label_g = QtWidgets.QLabel(self.widget)
        self.label_g.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_g.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_g.setObjectName("label_g")
        self.horizontalLayout_2.addWidget(self.label_g)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.slider_b = QtWidgets.QSlider(self.widget)
        self.slider_b.setMaximum(255)
        self.slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.slider_b.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_b.setObjectName("slider_b")
        self.horizontalLayout_3.addWidget(self.slider_b)
        self.label_b = QtWidgets.QLabel(self.widget)
        self.label_b.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_b.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_b.setObjectName("label_b")
        self.horizontalLayout_3.addWidget(self.label_b)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        RGB.setCentralWidget(self.centralwidget)

        self.retranslateUi(RGB)
        QtCore.QMetaObject.connectSlotsByName(RGB)

    def retranslateUi(self, RGB):
        RGB.setWindowTitle(QtWidgets.QApplication.translate("RGB", "RGB调色板", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("RGB", "TextLabel", None, -1))
        self.label_r.setText(QtWidgets.QApplication.translate("RGB", "R", None, -1))
        self.label_g.setText(QtWidgets.QApplication.translate("RGB", "G", None, -1))
        self.label_b.setText(QtWidgets.QApplication.translate("RGB", "B", None, -1))

