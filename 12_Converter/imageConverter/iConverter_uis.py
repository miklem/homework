# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GoogleDrive\3D\Python\education\12_Converter\imageConverter\iConverter.ui'
#
# Created: Wed Nov 22 20:14:27 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_iConverter(object):
    def setupUi(self, iConverter):
        iConverter.setObjectName("iConverter")
        iConverter.resize(354, 444)
        self.centralwidget = QtGui.QWidget(iConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iConv_lb = QtGui.QLabel(self.centralwidget)
        self.iConv_lb.setObjectName("iConv_lb")
        self.horizontalLayout.addWidget(self.iConv_lb)
        self.browseIconv_btn = QtGui.QPushButton(self.centralwidget)
        self.browseIconv_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.browseIconv_btn.setObjectName("browseIconv_btn")
        self.horizontalLayout.addWidget(self.browseIconv_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.files_lt = QtGui.QVBoxLayout()
        self.files_lt.setObjectName("files_lt")
        self.verticalLayout.addLayout(self.files_lt)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.out_le = QtGui.QLineEdit(self.centralwidget)
        self.out_le.setObjectName("out_le")
        self.horizontalLayout_2.addWidget(self.out_le)
        self.browseOut_btn = QtGui.QPushButton(self.centralwidget)
        self.browseOut_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.browseOut_btn.setObjectName("browseOut_btn")
        self.horizontalLayout_2.addWidget(self.browseOut_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_btn = QtGui.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(1, 1)
        iConverter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(iConverter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 21))
        self.menubar.setObjectName("menubar")
        iConverter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(iConverter)
        self.statusbar.setObjectName("statusbar")
        iConverter.setStatusBar(self.statusbar)

        self.retranslateUi(iConverter)
        QtCore.QMetaObject.connectSlotsByName(iConverter)

    def retranslateUi(self, iConverter):
        iConverter.setWindowTitle(QtGui.QApplication.translate("iConverter", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.iConv_lb.setText(QtGui.QApplication.translate("iConverter", "path", None, QtGui.QApplication.UnicodeUTF8))
        self.browseIconv_btn.setText(QtGui.QApplication.translate("iConverter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.browseOut_btn.setText(QtGui.QApplication.translate("iConverter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.start_btn.setText(QtGui.QApplication.translate("iConverter", "start", None, QtGui.QApplication.UnicodeUTF8))

