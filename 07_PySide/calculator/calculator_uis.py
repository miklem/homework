# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GoogleDrive\3D\Python\education\07_PySide\calculator\calculator.ui'
#
# Created: Sun Oct 29 17:55:13 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_calc_ManWindow(object):
    def setupUi(self, calc_ManWindow):
        calc_ManWindow.setObjectName("calc_ManWindow")
        calc_ManWindow.resize(338, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calc_ManWindow.sizePolicy().hasHeightForWidth())
        calc_ManWindow.setSizePolicy(sizePolicy)
        calc_ManWindow.setMinimumSize(QtCore.QSize(0, 0))
        calc_ManWindow.setMaximumSize(QtCore.QSize(3460, 2670))
        self.centralwidget = QtGui.QWidget(calc_ManWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.history_lb = QtGui.QLabel(self.centralwidget)
        self.history_lb.setWordWrap(True)
        self.history_lb.setObjectName("history_lb")
        self.verticalLayout.addWidget(self.history_lb)
        self.digit_le = QtGui.QLineEdit(self.centralwidget)
        self.digit_le.setObjectName("digit_le")
        self.verticalLayout.addWidget(self.digit_le)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.div_btn = QtGui.QPushButton(self.centralwidget)
        self.div_btn.setObjectName("div_btn")
        self.gridLayout.addWidget(self.div_btn, 2, 3, 1, 1)
        self.divx_btn = QtGui.QPushButton(self.centralwidget)
        self.divx_btn.setObjectName("divx_btn")
        self.gridLayout.addWidget(self.divx_btn, 1, 3, 1, 1)
        self.pow_btn = QtGui.QPushButton(self.centralwidget)
        self.pow_btn.setObjectName("pow_btn")
        self.gridLayout.addWidget(self.pow_btn, 1, 2, 1, 1)
        self.b6_btn = QtGui.QPushButton(self.centralwidget)
        self.b6_btn.setObjectName("b6_btn")
        self.gridLayout.addWidget(self.b6_btn, 4, 2, 1, 1)
        self.b7_btn = QtGui.QPushButton(self.centralwidget)
        self.b7_btn.setObjectName("b7_btn")
        self.gridLayout.addWidget(self.b7_btn, 3, 0, 1, 1)
        self.result_btn = QtGui.QPushButton(self.centralwidget)
        self.result_btn.setObjectName("result_btn")
        self.gridLayout.addWidget(self.result_btn, 6, 3, 1, 1)
        self.b1_btn = QtGui.QPushButton(self.centralwidget)
        self.b1_btn.setObjectName("b1_btn")
        self.gridLayout.addWidget(self.b1_btn, 5, 0, 1, 1)
        self.mul_btn = QtGui.QPushButton(self.centralwidget)
        self.mul_btn.setObjectName("mul_btn")
        self.gridLayout.addWidget(self.mul_btn, 3, 3, 1, 1)
        self.neg_btn = QtGui.QPushButton(self.centralwidget)
        self.neg_btn.setObjectName("neg_btn")
        self.gridLayout.addWidget(self.neg_btn, 6, 0, 1, 1)
        self.sqrt_btn = QtGui.QPushButton(self.centralwidget)
        self.sqrt_btn.setObjectName("sqrt_btn")
        self.gridLayout.addWidget(self.sqrt_btn, 1, 1, 1, 1)
        self.b9_btn = QtGui.QPushButton(self.centralwidget)
        self.b9_btn.setObjectName("b9_btn")
        self.gridLayout.addWidget(self.b9_btn, 3, 2, 1, 1)
        self.dot_btn = QtGui.QPushButton(self.centralwidget)
        self.dot_btn.setObjectName("dot_btn")
        self.gridLayout.addWidget(self.dot_btn, 6, 2, 1, 1)
        self.b2_btn = QtGui.QPushButton(self.centralwidget)
        self.b2_btn.setObjectName("b2_btn")
        self.gridLayout.addWidget(self.b2_btn, 5, 1, 1, 1)
        self.b3_btn = QtGui.QPushButton(self.centralwidget)
        self.b3_btn.setObjectName("b3_btn")
        self.gridLayout.addWidget(self.b3_btn, 5, 2, 1, 1)
        self.plus_btn = QtGui.QPushButton(self.centralwidget)
        self.plus_btn.setObjectName("plus_btn")
        self.gridLayout.addWidget(self.plus_btn, 5, 3, 1, 1)
        self.b0_btn = QtGui.QPushButton(self.centralwidget)
        self.b0_btn.setObjectName("b0_btn")
        self.gridLayout.addWidget(self.b0_btn, 6, 1, 1, 1)
        self.minus_btn = QtGui.QPushButton(self.centralwidget)
        self.minus_btn.setObjectName("minus_btn")
        self.gridLayout.addWidget(self.minus_btn, 4, 3, 1, 1)
        self.b8_btn = QtGui.QPushButton(self.centralwidget)
        self.b8_btn.setObjectName("b8_btn")
        self.gridLayout.addWidget(self.b8_btn, 3, 1, 1, 1)
        self.b4_btn = QtGui.QPushButton(self.centralwidget)
        self.b4_btn.setObjectName("b4_btn")
        self.gridLayout.addWidget(self.b4_btn, 4, 0, 1, 1)
        self.b5_btn = QtGui.QPushButton(self.centralwidget)
        self.b5_btn.setObjectName("b5_btn")
        self.gridLayout.addWidget(self.b5_btn, 4, 1, 1, 1)
        self.percent_btn = QtGui.QPushButton(self.centralwidget)
        self.percent_btn.setObjectName("percent_btn")
        self.gridLayout.addWidget(self.percent_btn, 1, 0, 1, 1)
        self.clear_btn = QtGui.QPushButton(self.centralwidget)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout.addWidget(self.clear_btn, 2, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        calc_ManWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(calc_ManWindow)
        QtCore.QMetaObject.connectSlotsByName(calc_ManWindow)
        calc_ManWindow.setTabOrder(self.b1_btn, self.b2_btn)
        calc_ManWindow.setTabOrder(self.b2_btn, self.b3_btn)
        calc_ManWindow.setTabOrder(self.b3_btn, self.b4_btn)
        calc_ManWindow.setTabOrder(self.b4_btn, self.b5_btn)
        calc_ManWindow.setTabOrder(self.b5_btn, self.b6_btn)
        calc_ManWindow.setTabOrder(self.b6_btn, self.b7_btn)
        calc_ManWindow.setTabOrder(self.b7_btn, self.b8_btn)
        calc_ManWindow.setTabOrder(self.b8_btn, self.b9_btn)
        calc_ManWindow.setTabOrder(self.b9_btn, self.b0_btn)
        calc_ManWindow.setTabOrder(self.b0_btn, self.neg_btn)
        calc_ManWindow.setTabOrder(self.neg_btn, self.dot_btn)
        calc_ManWindow.setTabOrder(self.dot_btn, self.percent_btn)
        calc_ManWindow.setTabOrder(self.percent_btn, self.sqrt_btn)
        calc_ManWindow.setTabOrder(self.sqrt_btn, self.pow_btn)
        calc_ManWindow.setTabOrder(self.pow_btn, self.divx_btn)
        calc_ManWindow.setTabOrder(self.divx_btn, self.clear_btn)
        calc_ManWindow.setTabOrder(self.clear_btn, self.div_btn)
        calc_ManWindow.setTabOrder(self.div_btn, self.mul_btn)
        calc_ManWindow.setTabOrder(self.mul_btn, self.minus_btn)
        calc_ManWindow.setTabOrder(self.minus_btn, self.plus_btn)
        calc_ManWindow.setTabOrder(self.plus_btn, self.result_btn)

    def retranslateUi(self, calc_ManWindow):
        calc_ManWindow.setWindowTitle(QtGui.QApplication.translate("calc_ManWindow", "NotTheBestCalc", None, QtGui.QApplication.UnicodeUTF8))
        self.history_lb.setText(QtGui.QApplication.translate("calc_ManWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.div_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.divx_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "1/x", None, QtGui.QApplication.UnicodeUTF8))
        self.pow_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "X^2", None, QtGui.QApplication.UnicodeUTF8))
        self.b6_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.b7_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.result_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.b1_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.mul_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.neg_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "+-", None, QtGui.QApplication.UnicodeUTF8))
        self.sqrt_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "sqrt", None, QtGui.QApplication.UnicodeUTF8))
        self.b9_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.dot_btn.setText(QtGui.QApplication.translate("calc_ManWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.b2_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.b3_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.plus_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.b0_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.minus_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.b8_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.b4_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.b5_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.percent_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setText(QtGui.QApplication.translate("calc_ManWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
