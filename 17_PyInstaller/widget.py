from PySide.QtCore import *
from PySide.QtGui import *
import os
import sys, os
from ctypes import *


def getRootDir(*args):
    if getattr(sys, 'frozen', False):
        application_path = toLongName(os.path.abspath(os.path.dirname(sys.executable)))
    else:
        application_path = os.path.dirname(__file__)
    if args:
        application_path = os.path.join(application_path, os.path.join(*args))
    application_path = application_path.replace('\\','/')
    return application_path


def toLongName(path):
    buf = create_unicode_buffer(500)
    windll.kernel32.GetLongPathNameW(unicode(path), buf, 500)
    return buf.value


class WidgetClass(QWidget):
    def __init__(self):
        super(WidgetClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.i = 0
        self.btn = QPushButton('click')
        self.ly.addWidget(self.btn)
        self.resize(300, 100)
        self.btn.clicked.connect(self.hello)

    def hello(self):
        # self.btn.setText(str(self.i))
        # self.i += 1

        # print os.path.dirname(__file__)+'/widget.py'
        # print sys.executable

        # print getRootDir()

        path = getRootDir()
        img = QFileDialog.getOpenFileName(self, 'Open File', path)
        if img[0]:
            i = QPixmap(img[0]).scaled(500, 500)
            out = os.path.join(path, 'scaled.jpg')
            i.save(out, 'JPG')



if __name__ == '__main__':
    app = QApplication([])
    if getattr(sys, 'frozen', False):
        QApplication.addLibraryPath(sys._MEIPASS)

    w = WidgetClass()

    w.show()
    app.exec_()

