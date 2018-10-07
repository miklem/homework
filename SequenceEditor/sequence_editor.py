from PySide.QtGui import *
from PySide.QtCore import *
import os
from widgets import editorView
import SE_uis as ui


class EditorWindowClass(QMainWindow, ui.Ui_SequenceEditor_window):
    def __init__(self, parent=None):
        super(EditorWindowClass, self).__init__(parent=parent)
        self.setupUi(self)
        self.view = editorView.EditorViewClass(self)
        #add class to main window
        self.verticalLayout.addWidget(self.view)
        self.add_btn.clicked.connect(self.add_item)
        self.del_btn.clicked.connect(self.del_item)
        self.clear_btn.clicked.connect(self.clear_items)


    def add_item(self):
        self.view.s.addNode()
        self.view.s.fix_positions()

    def del_item(self):
        self.view.s.deleteNode()

    def clear_items(self):
        self.view.s.deleteNode(True)
        self.lastXpos = 20
        self.lastYpos = 20


if __name__ == '__main__':
    app = QApplication([])
    w = EditorWindowClass()

    w.show()
    app.exec_()
