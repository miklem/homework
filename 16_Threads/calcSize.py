from PySide.QtCore import *
from PySide.QtGui import *
import os


class folderSizeCompute(QWidget):
    def __init__(self):
        super(folderSizeCompute, self).__init__()
        self.ly = QVBoxLayout(self)
        self.le = QLineEdit()
        self.le.setText('C:/Python27')
        self.btn = QPushButton("calc")
        self.ly.addWidget(self.le)
        self.ly.addWidget(self.btn)
        self.btn.clicked.connect(self.calc)
        self.lb = QLabel()
        self.ly.addWidget(self.lb)
        self.resize(300, 100)

    def calc(self):
        size = 0
        for path, dirs,files in os.walk(self.le.text()):
            for f in files:
                b = os.path.getsize(os.path.join(path, f))
                size += int(b/1024.0)
        self.setInfo(size)

    def setInfo(self, size):
        self.lb.setText('%s bytes' % size)


if __name__ == '__main__':
    app = QApplication([])
    w = folderSizeCompute()
    w.show()
    app.exec_()

