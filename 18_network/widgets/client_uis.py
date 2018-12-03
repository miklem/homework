# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GoogleDrive\Dev\Code\homework\18_network\widgets\client.ui'
#
# Created: Mon Dec  3 15:27:38 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_clientForm(object):
    def setupUi(self, clientForm):
        clientForm.setObjectName("clientForm")
        clientForm.resize(400, 102)
        self.verticalLayout = QtGui.QVBoxLayout(clientForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ip_le = QtGui.QLineEdit(clientForm)
        self.ip_le.setObjectName("ip_le")
        self.verticalLayout.addWidget(self.ip_le)
        self.conn_btn = QtGui.QPushButton(clientForm)
        self.conn_btn.setObjectName("conn_btn")
        self.verticalLayout.addWidget(self.conn_btn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider = QtGui.QSlider(clientForm)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.progr_lb = QtGui.QLabel(clientForm)
        self.progr_lb.setObjectName("progr_lb")
        self.horizontalLayout.addWidget(self.progr_lb)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(clientForm)
        QtCore.QMetaObject.connectSlotsByName(clientForm)

    def retranslateUi(self, clientForm):
        clientForm.setWindowTitle(QtGui.QApplication.translate("clientForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.conn_btn.setText(QtGui.QApplication.translate("clientForm", "connect", None, QtGui.QApplication.UnicodeUTF8))
        self.progr_lb.setText(QtGui.QApplication.translate("clientForm", "0", None, QtGui.QApplication.UnicodeUTF8))

