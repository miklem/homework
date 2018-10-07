from PySide.QtGui import *
from PySide.QtCore import *
import os
textArray = 'Click', 'Press', 'Enter'


class myButtonClass(QPushButton):
    def __init__(self, text):
        super(myButtonClass, self).__init__(text)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            super(myButtonClass, self). mousePressEvent(event)
        if event.button() == Qt.MouseButton.RightButton:
            #remap local coordinates to global one
            pos = event.globalPos()
            menu = QMenu()
            for i in textArray:
                menu.addAction(QAction(i, self))
            a = menu.exec_(pos)
            if a:
                self.setText(a.text())
        elif event.button() == Qt.MouseButton.MiddleButton:
            print "middle button"





