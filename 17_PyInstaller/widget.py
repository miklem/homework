from PySide.QtCore import *
from PySide.QtGui import *
import os

class WidgetClass(QWidget):
    def __init__(self):
        super(WidgetClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.i = 0
        self.btn = QPushButton('click')
        self.ly.addWidget(self.btn)
        self.btn.clicked.connect(self.hello)

    def hello(self):
        # self.btn.setText(str(self.i))
        # self.i += 1
        print os.path.dirname(__file__)+'/widget.py'

if __name__ == '__main__':
    app = QApplication([])
    w = WidgetClass()
    w.show()
    app.exec_()
