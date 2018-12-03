# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GoogleDrive\Dev\Code\homework\18_network\server.ui'
#
# Created: Mon Dec  3 14:57:54 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(371, 438)
        self.verticalLayout = QtGui.QVBoxLayout(Server)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtGui.QProgressBar(Server)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Server)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ip_le = QtGui.QLineEdit(Server)
        self.ip_le.setObjectName("ip_le")
        self.horizontalLayout.addWidget(self.ip_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.serv_te = QtGui.QTextEdit(Server)
        self.serv_te.setObjectName("serv_te")
        self.verticalLayout.addWidget(self.serv_te)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        Server.setWindowTitle(QtGui.QApplication.translate("Server", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Server", "IP:", None, QtGui.QApplication.UnicodeUTF8))

