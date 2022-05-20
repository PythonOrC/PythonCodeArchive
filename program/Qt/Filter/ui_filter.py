# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Personal/Python/program/Qt/Filter/filter.ui',
# licensing of 'E:/Personal/Python/program/Qt/Filter/filter.ui' applies.
#
# Created: Sat Sep  7 19:17:32 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_process_img(object):
    def setupUi(self, process_img):
        process_img.setObjectName("process_img")
        process_img.resize(799, 491)
        self.centralwidget = QtWidgets.QWidget(process_img)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pb_file = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pb_file.setFont(font)
        self.pb_file.setObjectName("pb_file")
        self.cb_filter_list = QtWidgets.QComboBox(self.splitter)
        self.cb_filter_list.setMinimumSize(QtCore.QSize(300, 0))
        self.cb_filter_list.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.cb_filter_list.setFont(font)
        self.cb_filter_list.setObjectName("cb_filter_list")
        self.cb_filter_list.addItem("")
        self.cb_filter_list.addItem("")
        self.cb_filter_list.addItem("")
        self.cb_filter_list.addItem("")
        self.cb_filter_list.addItem("")
        self.cb_filter_list.addItem("")
        self.pb_process = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pb_process.setFont(font)
        self.pb_process.setObjectName("pb_process")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_input_img = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lb_input_img.setFont(font)
        self.lb_input_img.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_input_img.setObjectName("lb_input_img")
        self.horizontalLayout.addWidget(self.lb_input_img)
        self.lb_output_img = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lb_output_img.setFont(font)
        self.lb_output_img.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_output_img.setObjectName("lb_output_img")
        self.horizontalLayout.addWidget(self.lb_output_img)
        self.verticalLayout.addLayout(self.horizontalLayout)
        process_img.setCentralWidget(self.centralwidget)

        self.retranslateUi(process_img)
        QtCore.QMetaObject.connectSlotsByName(process_img)

    def retranslateUi(self, process_img):
        process_img.setWindowTitle(QtWidgets.QApplication.translate("process_img", "滤镜处理", None, -1))
        self.pb_file.setText(QtWidgets.QApplication.translate("process_img", "选择图片文件", None, -1))
        self.cb_filter_list.setItemText(0, QtWidgets.QApplication.translate("process_img", "模糊滤镜", None, -1))
        self.cb_filter_list.setItemText(1, QtWidgets.QApplication.translate("process_img", "轮廓滤镜", None, -1))
        self.cb_filter_list.setItemText(2, QtWidgets.QApplication.translate("process_img", "浮雕滤镜", None, -1))
        self.cb_filter_list.setItemText(3, QtWidgets.QApplication.translate("process_img", "锐化滤镜", None, -1))
        self.cb_filter_list.setItemText(4, QtWidgets.QApplication.translate("process_img", "平滑滤镜", None, -1))
        self.cb_filter_list.setItemText(5, QtWidgets.QApplication.translate("process_img", "边缘增强滤镜", None, -1))
        self.pb_process.setText(QtWidgets.QApplication.translate("process_img", "开始处理", None, -1))
        self.lb_input_img.setText(QtWidgets.QApplication.translate("process_img", "处理前", None, -1))
        self.lb_output_img.setText(QtWidgets.QApplication.translate("process_img", "处理后", None, -1))

