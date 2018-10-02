# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GoogleDrive\3D\Python\education\14_GraphScene\homework\SE.ui'
#
# Created: Thu Mar 22 21:50:20 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SequenceEditor_window(object):
    def setupUi(self, SequenceEditor_window):
        SequenceEditor_window.setObjectName("SequenceEditor_window")
        SequenceEditor_window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(SequenceEditor_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtGui.QPushButton(self.centralwidget)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.del_btn = QtGui.QPushButton(self.centralwidget)
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout.addWidget(self.del_btn)
        self.clear_btn = QtGui.QPushButton(self.centralwidget)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.swgt = QtGui.QWidget(self.centralwidget)
        self.swgt.setObjectName("swgt")
        self.verticalLayout.addWidget(self.swgt)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        SequenceEditor_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(SequenceEditor_window)
        self.statusbar.setObjectName("statusbar")
        SequenceEditor_window.setStatusBar(self.statusbar)

        self.retranslateUi(SequenceEditor_window)
        QtCore.QMetaObject.connectSlotsByName(SequenceEditor_window)

    def retranslateUi(self, SequenceEditor_window):
        SequenceEditor_window.setWindowTitle(QtGui.QApplication.translate("SequenceEditor_window", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("SequenceEditor_window", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("SequenceEditor_window", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setText(QtGui.QApplication.translate("SequenceEditor_window", "Clear", None, QtGui.QApplication.UnicodeUTF8))

