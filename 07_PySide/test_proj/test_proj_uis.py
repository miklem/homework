# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GoogleDrive\3D\Python\education\07_PySide\test_proj\test_proj.ui'
#
# Created: Wed Oct 25 17:42:04 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_test_proj(object):
    def setupUi(self, test_proj):
        test_proj.setObjectName("test_proj")
        test_proj.resize(400, 300)
        self.verticalLayout_3 = QtGui.QVBoxLayout(test_proj)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.additem_btn = QtGui.QPushButton(test_proj)
        self.additem_btn.setObjectName("additem_btn")
        self.verticalLayout_2.addWidget(self.additem_btn)
        self.name_le = QtGui.QLineEdit(test_proj)
        self.name_le.setObjectName("name_le")
        self.verticalLayout_2.addWidget(self.name_le)
        self.items_ly = QtGui.QVBoxLayout()
        self.items_ly.setObjectName("items_ly")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.items_ly.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.items_ly)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(test_proj)
        QtCore.QMetaObject.connectSlotsByName(test_proj)

    def retranslateUi(self, test_proj):
        test_proj.setWindowTitle(QtGui.QApplication.translate("test_proj", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.additem_btn.setText(QtGui.QApplication.translate("test_proj", "Add", None, QtGui.QApplication.UnicodeUTF8))

