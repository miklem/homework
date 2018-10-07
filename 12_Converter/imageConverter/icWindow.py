from PySide.QtGui import *
from PySide.QtCore import *
import os
from imageConverter import converter

import iConverter_uis as ui
from widgets import filesWidget


class imageConverterClass(QMainWindow, ui.Ui_iConverter ):
    def __init__(self):
        super(imageConverterClass, self).__init__()
        self.setupUi(self)
        self.list = filesWidget.listWidgetClass()
        self.files_lt.addWidget(self.list)
        self.start_btn.clicked.connect(self.start)

    def start(self):
        files = self.list.getAllFiles()
        if files:
            inc = 100 / len(files)
            out = self.out_le.text()
            for f in files:
                converter.convert(f, out)
                self.progressBar.setValue(self.progressBar.value() + inc)
        self.progressBar.setValue(0)


if __name__ == '__main__':
    app = QApplication([])
    w = imageConverterClass()
    w.show()
    app.exec_()
