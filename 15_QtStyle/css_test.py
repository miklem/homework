from PySide.QtCore import *
from PySide.QtGui import *
from widgets import css_test_uis as ui


class StyleWidgetClass(QMainWindow, ui.Ui_testUi):
    def __init__(self):
        super(StyleWidgetClass, self).__init__()
        self.setupUi(self)
        
        
if __name__ == '__main__':
    app = QApplication([])
    w = StyleWidgetClass()
    w.show()
    app.exec_()