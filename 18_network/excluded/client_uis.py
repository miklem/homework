# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GoogleDrive\Dev\Code\homework\18_network\client.ui'
#
# Created: Mon Dec  3 14:57:49 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_0(object):
    def setupUi(self, 0):
        0.setObjectName("0")
        0.resize(400, 102)
        self.verticalLayout = QtGui.QVBoxLayout(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.client_le = QtGui.QLineEdit(0)
        self.client_le.setObjectName("client_le")
        self.verticalLayout.addWidget(self.client_le)
        self.conn_btn = QtGui.QPushButton(0)
        self.conn_btn.setObjectName("conn_btn")
        self.verticalLayout.addWidget(self.conn_btn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider = QtGui.QSlider(0)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.progr_lb = QtGui.QLabel(0)
        self.progr_lb.setObjectName("progr_lb")
        self.horizontalLayout.addWidget(self.progr_lb)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(0)
        QtCore.QMetaObject.connectSlotsByName(0)

    def retranslateUi(self, 0):
        0.setWindowTitle(QtGui.QApplication.translate("0", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.conn_btn.setText(QtGui.QApplication.translate("0", "connect", None, QtGui.QApplication.UnicodeUTF8))
        self.progr_lb.setText(QtGui.QApplication.translate("0", "0", None, QtGui.QApplication.UnicodeUTF8))

