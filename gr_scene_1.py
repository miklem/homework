from PySide.QtGui import *
from PySide.QtCore import *
import sceneWidget


class ExampleViewClass(QGraphicsView):
    def __init__(self):
        super(ExampleViewClass, self).__init__()
        self.s = sceneWidget.ExampleSceneClass()
        self.setScene(self.s)


if __name__ == '__main__':
    app = QApplication([])
    w = ExampleViewClass()
    w.show()
    app.exec_()