# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Personal/Python/python_work/charts/charts.ui',
# licensing of 'C:/Personal/Python/python_work/charts/charts.ui' applies.
#
# Created: Sat Aug 17 16:50:31 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Charts(object):
    def setupUi(self, Charts):
        Charts.setObjectName("Charts")
        Charts.resize(521, 379)
        self.centralwidget = QtWidgets.QWidget(Charts)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_title = QtWidgets.QLabel(self.centralwidget)
        self.lb_title.setGeometry(QtCore.QRect(190, 0, 121, 51))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.lb_title.setFont(font)
        self.lb_title.setObjectName("lb_title")
        self.pb_data = QtWidgets.QPushButton(self.centralwidget)
        self.pb_data.setGeometry(QtCore.QRect(20, 50, 51, 21))
        self.pb_data.setFlat(False)
        self.pb_data.setObjectName("pb_data")
        self.cb_chartlist = QtWidgets.QComboBox(self.centralwidget)
        self.cb_chartlist.setGeometry(QtCore.QRect(80, 50, 51, 21))
        self.cb_chartlist.setObjectName("cb_chartlist")
        self.cb_chartlist.addItem("")
        self.cb_chartlist.addItem("")
        self.cb_chartlist.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 481, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vl_chart = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vl_chart.setContentsMargins(0, 0, 0, 0)
        self.vl_chart.setObjectName("vl_chart")
        self.lb_info = QtWidgets.QLabel(self.centralwidget)
        self.lb_info.setGeometry(QtCore.QRect(350, 50, 143, 16))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(15)
        self.lb_info.setFont(font)
        self.lb_info.setObjectName("lb_info")
        Charts.setCentralWidget(self.centralwidget)

        self.retranslateUi(Charts)
        QtCore.QMetaObject.connectSlotsByName(Charts)

    def retranslateUi(self, Charts):
        Charts.setWindowTitle(QtWidgets.QApplication.translate("Charts", "图表分析软件", None, -1))
        self.lb_title.setText(QtWidgets.QApplication.translate("Charts", "我的数据图表", None, -1))
        self.pb_data.setText(QtWidgets.QApplication.translate("Charts", "选择数据", None, -1))
        self.cb_chartlist.setItemText(0, QtWidgets.QApplication.translate("Charts", "折线图", None, -1))
        self.cb_chartlist.setItemText(1, QtWidgets.QApplication.translate("Charts", "柱状图", None, -1))
        self.cb_chartlist.setItemText(2, QtWidgets.QApplication.translate("Charts", "饼状图", None, -1))
        self.lb_info.setText(QtWidgets.QApplication.translate("Charts", "请先选择数据文件...", None, -1))

