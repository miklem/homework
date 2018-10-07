import random

from PySide.QtCore import *
from PySide.QtGui import *

import iconTutorial_uis as ui
from png.icons import icon

from png import rsc

class iconWidgetClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(iconWidgetClass, self).__init__()
        self.setupUi(self)
        # self.widget = QWidget(self)
        # self.setCentralWidget(self.widget)

        #ui
        self.setWindowIcon(QIcon(icon['item3']))
        self.fill_btn.setText('')
        self.fill_btn.setFixedSize(QSize(40, 40))
        self.fill_btn.setIconSize(QSize(32, 32))
        self.fill_btn.setFlat(1)
        # self.fill_btn.setIcon(QIcon(icon['create']))
        self.fill_btn.setIcon(QIcon(':/ico/download-1.png'))
        self.clear_btn.setText('')
        self.clear_btn.setFixedSize(QSize(40,40))
        self.clear_btn.setIconSize(QSize(32,32))
        self.clear_btn.setFlat(1)
        self.clear_btn.setIcon(QIcon("E:/GoogleDrive/3D/Python/education/10_Menu/png/dislike.png"))
        #connects
        self.fill_btn.clicked.connect(self.fillList)
        self.clear_btn.clicked.connect(self.clearList)

        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setIconSize(QSize(64, 64))
        self.listWidget.setResizeMode(QListWidget.ResizeMode.Adjust)


    def fillList(self):
        self.clearList()
        self.fillComboBox()
        for i in range(10):
            item = QListWidgetItem('Item %s' % i)
            item.setIcon(self.getRandomIcon())
            self.listWidget.addItem(item)

    def clearList(self):
        self.listWidget.clear()
        self.comboBox.clear()

    def fillComboBox(self):
        for i in range(10):
            #order is important
            self.comboBox.addItem("Item %s" % i)
            self.comboBox.setItemIcon(i, self.getRandomIcon())

    def getRandomIcon(self):
        return QIcon(icon[random.choice(['item1', 'item2', 'item3'])])


if __name__ == '__main__':
    app = QApplication([])
    w = iconWidgetClass()
    w.show()
    app.exec_()
