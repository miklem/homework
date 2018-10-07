from PySide.QtGui import *
from PySide.QtCore import *
import os
import button



class MainWindowClass(QMainWindow):
    def __init__(self):
        super(MainWindowClass, self).__init__()

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        #menuBar
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        #menu
        self.menu = QMenu("File")
        self.menu_bar.addMenu(self.menu)
        #actions
        self.actionOpen = QAction("open", self)
        self.actionOpen.triggered.connect(self.action)
        self.menu.addAction(self.actionOpen)

        #the same in one line
        self.menu.addAction(QAction('Save', self, triggered = self.action2))
        #subMenu
        self.smenu = QMenu('Sub')
        self.menu.addMenu(self.smenu)

        for i in range(10):
            self.smenu.addAction(QAction('Item %s' % i, self,
                                         triggered=lambda x=i:self.action2(x)))





    def action(self):
        print "Action"

    def action2(self, number):
        print number

if __name__ == '__main__':
    app = QApplication([])
    w = MainWindowClass()
    w.show()
    app.exec_()
