from PySide.QtCore import *
from PySide.QtGui import *
import os
import time



class folderSizeCompute(QWidget):
    def __init__(self):
        super(folderSizeCompute, self).__init__()
        self.ly = QVBoxLayout(self)
        self.le = QLineEdit()
        self.le.setText('C:/windows')
        self.btn = QPushButton("calc")
        self.ly.addWidget(self.le)
        self.ly.addWidget(self.btn)
        self.btn.clicked.connect(self.calc)
        self.lb = QLabel()
        self.ly.addWidget(self.lb)
        self.resize(300, 100)

    def calc(self):
        path = self.le.text()
        self.obj = Worker(path)
        self.t = QThread()
        self.obj.moveToThread(self.t)
        self.t.started.connect(self.obj.start)
        self.obj.finishedSignal.connect(self.t.quit)
        self.obj.updateSignal.connect(self.setInfo)
        self.t.start()

    def setInfo(self, size):
        self.lb.setText('%s bytes' % size)


class Worker(QObject):
    finishedSignal = Signal()
    updateSignal = Signal(int)
    def __init__(self, path):
        super(Worker, self).__init__()
        self.path = path

    def start(self):
        size = 0
        st = time.time()
        for path, dirs, files in os.walk(self.path):
            for f in files:
                b = os.path.getsize(os.path.join(path, f))
                size += int(b/(1024))
                if(time.time() - st) > 0.5:
                    self.updateSignal.emit(size)
                    st=time.time()
        self.finishedSignal.emit()



if __name__ == '__main__':
    app = QApplication([])
    w = folderSizeCompute()
    w.show()
    app.exec_()

