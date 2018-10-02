import sys
from PySide import QtGui, QtCore

class MyView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        QtGui.QGraphicsView.__init__(self, parent=parent)

        self.scene = QtGui.QGraphicsScene(self)
        self.item = QtGui.QGraphicsRectItem(300,400,100,100)
        self.scene.addItem(self.item)
        self.setScene(self.scene)

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        #This initializes the main window or form
        super(Window,self).__init__(parent=parent)
        self.setGeometry(50,50,900,700)
        self.setWindowTitle("Pre-Alignment system")

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    view = MyView(GUI)
    GUI.show()
    sys.exit(app.exec_())

run()