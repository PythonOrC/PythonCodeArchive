# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Pillow/3-一张旧照片/picture_adj.ui',
# licensing of 'E:/Personal/Python/program/Pillow/3-一张旧照片/picture_adj.ui' applies.
#
# Created: Sat Jan  2 17:45:05 2021
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_pbtn = QtWidgets.QPushButton(self.centralwidget)
        self.open_pbtn.setGeometry(QtCore.QRect(20, 20, 681, 21))
        self.open_pbtn.setObjectName("open_pbtn")
        self.if_open_lb = QtWidgets.QLabel(self.centralwidget)
        self.if_open_lb.setGeometry(QtCore.QRect(20, 70, 761, 21))
        self.if_open_lb.setText("")
        self.if_open_lb.setObjectName("if_open_lb")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 711, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.r_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.r_slider.setMinimum(-255)
        self.r_slider.setMaximum(255)
        self.r_slider.setOrientation(QtCore.Qt.Horizontal)
        self.r_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.r_slider.setObjectName("r_slider")
        self.verticalLayout.addWidget(self.r_slider)
        self.g_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.g_slider.setMinimum(-255)
        self.g_slider.setMaximum(255)
        self.g_slider.setOrientation(QtCore.Qt.Horizontal)
        self.g_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.g_slider.setObjectName("g_slider")
        self.verticalLayout.addWidget(self.g_slider)
        self.b_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.b_slider.setMinimum(-255)
        self.b_slider.setMaximum(255)
        self.b_slider.setOrientation(QtCore.Qt.Horizontal)
        self.b_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.b_slider.setObjectName("b_slider")
        self.verticalLayout.addWidget(self.b_slider)
        self.contrast_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.contrast_slider.setMinimum(0)
        self.contrast_slider.setMaximum(300)
        self.contrast_slider.setProperty("value", 100)
        self.contrast_slider.setSliderPosition(100)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.contrast_slider.setObjectName("contrast_slider")
        self.verticalLayout.addWidget(self.contrast_slider)
        self.brightness_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(300)
        self.brightness_slider.setProperty("value", 100)
        self.brightness_slider.setSliderPosition(100)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.brightness_slider.setObjectName("brightness_slider")
        self.verticalLayout.addWidget(self.brightness_slider)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(750, 90, 35, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.r_lb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.r_lb.setObjectName("r_lb")
        self.verticalLayout_2.addWidget(self.r_lb)
        self.g_lb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.g_lb.setObjectName("g_lb")
        self.verticalLayout_2.addWidget(self.g_lb)
        self.b__lb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.b__lb.setObjectName("b__lb")
        self.verticalLayout_2.addWidget(self.b__lb)
        self.contrast_lb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.contrast_lb.setObjectName("contrast_lb")
        self.verticalLayout_2.addWidget(self.contrast_lb)
        self.brightness_lb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.brightness_lb.setObjectName("brightness_lb")
        self.verticalLayout_2.addWidget(self.brightness_lb)
        self.render_pbtn = QtWidgets.QPushButton(self.centralwidget)
        self.render_pbtn.setGeometry(QtCore.QRect(20, 470, 761, 21))
        self.render_pbtn.setObjectName("render_pbtn")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 510, 761, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(710, 20, 70, 21))
        self.checkBox.setObjectName("checkBox")
        self.save_pbtn = QtWidgets.QPushButton(self.centralwidget)
        self.save_pbtn.setGeometry(QtCore.QRect(20, 560, 761, 23))
        self.save_pbtn.setObjectName("保存图片")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.open_pbtn.setText(QtWidgets.QApplication.translate("MainWindow", "选择图片", None, -1))
        self.r_lb.setText(QtWidgets.QApplication.translate("MainWindow", "红", None, -1))
        self.g_lb.setText(QtWidgets.QApplication.translate("MainWindow", "绿", None, -1))
        self.b__lb.setText(QtWidgets.QApplication.translate("MainWindow", "蓝", None, -1))
        self.contrast_lb.setText(QtWidgets.QApplication.translate("MainWindow", "对比度", None, -1))
        self.brightness_lb.setText(QtWidgets.QApplication.translate("MainWindow", "明亮度", None, -1))
        self.render_pbtn.setText(QtWidgets.QApplication.translate("MainWindow", "渲染图片", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "Film Mode", None, -1))
        self.save_pbtn.setText(QtWidgets.QApplication.translate("MainWindow", "保存图片", None, -1))
