from PySide.QtCore import *
from PySide.QtGui import *
import IOextended as ioe
import os
reload(ioe)
IO_ext = ioe.IOextendedClass()
worker = 'python ' + IO_ext.getRelativeFilePath('worker.py')

class WorkerClass(QWidget):
    def __init__(self):
        super(WorkerClass, self).__init__()

        self.ly = QVBoxLayout(self)
        self.start_btn = QPushButton('start')
        self.start_btn.clicked.connect(self.runWorker)
        self.ly.addWidget(self.start_btn)
        self.out = QTextBrowser()
        self.ly.addWidget(self.out)

        self.progress = QProgressBar()
        self.ly.addWidget(self.progress)
        self.progress.setValue(0)


    def runWorker(self):
        print "Thread runned"
        self.p = QProcess()
        self.p.finished.connect(self.finish)
        self.p.readyRead.connect(self.readOut)
        self.p.start(worker)
        self.start_btn.setEnabled(0)


    def readOut(self):
        out = str(self.p.readAll()).strip() #return QByteArray. Check how to convert it properly to str
        self.showMsg(out)

    def finish(self):
        self.start_btn.setEnabled(1)
        self.showMsg("Done")

    def showMsg(self, msg):
        self.out.append(msg)


if __name__ == '__main__':
    app = QApplication([])
    w = WorkerClass()
    w.show()
    app.exec_()
