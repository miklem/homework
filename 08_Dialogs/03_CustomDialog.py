
from PySide.QtCore import *
from PySide.QtGui import *
import dialog as d


class CustomDialogClass(QWidget):
    def __init__(self):
        super(CustomDialogClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.btn = QPushButton('open')
        self.ly.addWidget(self.btn)
        self.resize(300, 200)
        self.btn.clicked.connect(self.showMessage)

    def showMessage(self):
        self.dial = d.CustomDialogClass()
        r = self.dial.exec_()
        if r:
            print self.dial.getData()


if __name__ == '__main__':
    app = QApplication([])
    w = CustomDialogClass()
    w.show()
    app.exec_()