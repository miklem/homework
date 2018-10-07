from PySide.QtGui import *
from PySide.QtCore import *
import os
import button
textArray = 'Click', 'Press', 'Enter'


class widgetMenuCLass(QWidget):
    def __init__(self):
        super(widgetMenuCLass, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = button.myButtonClass('Click')
        # self.btn = QPushButton('Click')
        ly.addWidget(self.btn)
        self.line = QLineEdit()
        ly.addWidget(self.line)

        self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        self.btn.customContextMenuRequested.connect(self.openMenu)

        self.line.setContextMenuPolicy(Qt.CustomContextMenu)
        self.line.customContextMenuRequested.connect(self.openMenu)

    # def openMenu2(self, pos):
    #     #remap local coordinates to global one
    #     pos = self.line.mapToGlobal(pos)
    #     #creates standart line edit menu
    #     menu = self.line.createStandardContextMenu()
    #     #creates splitter
    #     menu.addSeparator()
    #     for i in textArray:
    #         menu.addAction(QAction(i, self))
    #     a = menu.exec_(pos) #QCursor().pos()
    #     if a:
    #         self.line.setText(a.text())

    def openMenu(self, pos):
        #remap local coordinates to global one
        pos = self.sender().mapToGlobal(pos)
        try:
            menu = self.sender().createStandardContextMenu()
        except:
            menu = QMenu()
        for i in textArray:
            menu.addAction(QAction(i, self))
        a = menu.exec_(pos) #QCursor().pos()
        if a:
            self.sender().setText(a.text())



if __name__ == '__main__':
    app = QApplication([])
    w = widgetMenuCLass()
    w.show()
    app.exec_()