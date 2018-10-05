from PySide.QtGui import *
from PySide.QtCore import *
import editorItem


class EditorSceneClass(QGraphicsScene):
    def __init__(self):
        super(EditorSceneClass, self).__init__()
        self.setSceneRect(-1000, -1000, 2000, 2000)
        self.grid = 30
        self.lastXpos = 0
        self.lastYpos = 0
        self.addNode()

    def drawBackground(self, painter, rect):
        if False:
            painter = QPainter
        painter.fillRect(rect, QColor(30, 30, 30))
        left = int(rect.left()) - int(rect.left()) % self.grid
        top = int(rect.top()) - int(rect.top()) % self.grid
        right = int(rect.right())
        bottom = int(rect.bottom())
        lines = []
        for x in range(left, right, self.grid):
            lines.append(QLine(x, top, x, bottom))
        for y in range(top, bottom, self.grid):
            lines.append(QLine(left, y, right, y))
        painter.setPen(QPen(QColor(100, 100, 100), 1))
        painter.drawLines(lines)

    def addNode(self, pos=False):
        if not pos:
            pos = QPoint(self.lastXpos, self.lastYpos)
        else:
            pos = QPoint(pos.x(), pos.y())
        item = editorItem.EditorItemClass(self.grid, len(self.items())+1)
        self.addItem(item)
        item.setPos(pos)
        self.lastXpos = pos.x()
        self.lastYpos = pos.y() + item.h

    def deleteNode(self, clear = False):
        if clear:
            self.clear()
            self.lastXpos = 0
            self.lastYpos = 0
        else:
            for i in self.items():
                if i.selected:
                    self.removeItem(i)

    def mouseDoubleClickEvent(self, event):
        self.addNode(event.scenePos())
        super(EditorSceneClass, self).mouseDoubleClickEvent(event)

    def mouseReleaseEvent(self, event):
        self.fix_positions()
        super(EditorSceneClass, self).mouseReleaseEvent(event)



    def fix_positions(self):
        for i in self.items():
            i.adjustPos()
        for i in self.selectedItems():
            i.checkCollision()
            i.adjustXPos(self.items())