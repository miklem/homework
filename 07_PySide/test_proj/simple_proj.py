from PySide.QtCore import *
from PySide.QtGui import *
import test_proj_uis


class test_proj_Class(QWidget, test_proj_uis.Ui_test_proj):
    def __init__(self):
        super(test_proj_Class, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('new text')
        self.count = 1
        self.additem_btn.clicked.connect(self.addItem)
        self.name_le.returnPressed.connect(self.addItem)


    def addItem(self):
        text = self.name_le.text()
        if text:
            lb = QLabel('%s: %s'%(self.count, text))
            self.items_ly.addWidget(lb)
            self.count +=1


if __name__ == '__main__':
    app = QApplication([])
    w = test_proj_Class()
    w.show()
    app.exec_()
