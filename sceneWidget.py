from PySide.QtGui import *
from PySide.QtCore import *
import exampleItem


class ExampleSceneClass(QGraphicsScene):
    def __init__(self):
        super(ExampleSceneClass, self).__init__()
        self.setSceneRect(-200, -200, 400, 400)
        self.fillScene()

    def fillScene(self):
        item = exampleItem.ExampleItemCLass()
        self.addItem(item)

    def drawBackground(self, painter, rec):
        painter.setPen(QPen(Qt.red, 3))
        painter.drawRect(self.sceneRect())
        painter.setPen(QPen(Qt.black))
        painter.drawText(0, 0, '0')
        painter.drawText(-200, -200, '-200')
        painter.drawText(200, 200, '200')

        painter.setPen(QPen(Qt.black, 1))
        painter.drawLine(0, -300, 0 , 300)
        painter.drawLine(-300, 0, 300 , 0)

