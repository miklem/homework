from PySide.QtCore import *
from PySide.QtGui import *
from widgets import css_test_uis as ui
import os

style = os.path.join(os.path.dirname(__file__), 'style.css')


class StyleWidgetClass(QMainWindow, ui.Ui_testUi):
    def __init__(self):
        super(StyleWidgetClass, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.assignCSS)

    def assignCSS(self):
        self.setStyleSheet(open(style).read())

        
if __name__ == '__main__':
    app = QApplication([])
    w = StyleWidgetClass()
    w.show()
    app.exec_()