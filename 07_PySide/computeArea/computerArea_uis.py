# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GoogleDrive\3D\Python\education\07_PySide\computeArea\computerArea.ui'
#
# Created: Thu Oct 26 15:10:40 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_computerArea(object):
    def setupUi(self, computerArea):
        computerArea.setObjectName("computerArea")
        computerArea.resize(203, 273)
        self.centralwidget = QtGui.QWidget(computerArea)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shape_cbb = QtGui.QComboBox(self.groupBox)
        self.shape_cbb.setObjectName("shape_cbb")
        self.shape_cbb.addItem("")
        self.shape_cbb.addItem("")
        self.verticalLayout.addWidget(self.shape_cbb)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.sq_grpb = QtGui.QGroupBox(self.centralwidget)
        self.sq_grpb.setObjectName("sq_grpb")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.sq_grpb)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.sq_grpb)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sq_height_spb = QtGui.QSpinBox(self.sq_grpb)
        self.sq_height_spb.setProperty("value", 5)
        self.sq_height_spb.setObjectName("sq_height_spb")
        self.horizontalLayout.addWidget(self.sq_height_spb)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.sq_grpb)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sq_width_spb = QtGui.QSpinBox(self.sq_grpb)
        self.sq_width_spb.setProperty("value", 5)
        self.sq_width_spb.setObjectName("sq_width_spb")
        self.horizontalLayout_2.addWidget(self.sq_width_spb)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.sq_grpb)
        self.ci_grpb = QtGui.QGroupBox(self.centralwidget)
        self.ci_grpb.setObjectName("ci_grpb")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.ci_grpb)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.ci_grpb)
        self.label_3.setMinimumSize(QtCore.QSize(70, 0))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ci_radius_spb = QtGui.QSpinBox(self.ci_grpb)
        self.ci_radius_spb.setProperty("value", 5)
        self.ci_radius_spb.setObjectName("ci_radius_spb")
        self.horizontalLayout_3.addWidget(self.ci_radius_spb)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.ci_grpb)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.compute_btn = QtGui.QPushButton(self.centralwidget)
        self.compute_btn.setObjectName("compute_btn")
        self.horizontalLayout_4.addWidget(self.compute_btn)
        self.result_lbl = QtGui.QLabel(self.centralwidget)
        self.result_lbl.setObjectName("result_lbl")
        self.horizontalLayout_4.addWidget(self.result_lbl)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        computerArea.setCentralWidget(self.centralwidget)

        self.retranslateUi(computerArea)
        QtCore.QMetaObject.connectSlotsByName(computerArea)

    def retranslateUi(self, computerArea):
        computerArea.setWindowTitle(QtGui.QApplication.translate("computerArea", "calc", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("computerArea", "Select shape", None, QtGui.QApplication.UnicodeUTF8))
        self.shape_cbb.setItemText(0, QtGui.QApplication.translate("computerArea", "square", None, QtGui.QApplication.UnicodeUTF8))
        self.shape_cbb.setItemText(1, QtGui.QApplication.translate("computerArea", "circle", None, QtGui.QApplication.UnicodeUTF8))
        self.sq_grpb.setTitle(QtGui.QApplication.translate("computerArea", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("computerArea", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("computerArea", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.ci_grpb.setTitle(QtGui.QApplication.translate("computerArea", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("computerArea", "Radiush", None, QtGui.QApplication.UnicodeUTF8))
        self.compute_btn.setText(QtGui.QApplication.translate("computerArea", "Compute", None, QtGui.QApplication.UnicodeUTF8))
        self.result_lbl.setText(QtGui.QApplication.translate("computerArea", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

