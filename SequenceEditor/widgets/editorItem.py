from PySide.QtGui import *
from PySide.QtCore import *


class EditorItemClass(QGraphicsItem):
    def __init__(self, height, num):
        super(EditorItemClass, self).__init__()
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = height
        self.num = num
        self.hover = None
        self.gapL = 20
        self.gapR = 20
        self.setAcceptHoverEvents(True)
        self.resizePadding = 10
        self.resizeL = False
        self.resizeR = False
        self.startPos = None
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.selected = False

    def boundingRect(self, *args, **kwargs):
        return QRectF(self.x, self.y, self.w, self.h)

    def paint(self, painter, options, widget):
        rec = self.boundingRect()
        if False:
            painter = QPainter()
        painter.fillRect(rec, Qt.black)
        painter.fillRect(rec.adjusted(1, 1, -1, -1), Qt.white)
        if not self.hover:
            color = Qt.gray
            self.selected = False
        else:
            color = Qt.darkGray
            self.selected = False
        if self.isSelected():
            color = Qt.yellow
            self.selected = True
        painter.fillRect(rec.adjusted(3, 3, -3, -3), color)
        painter.setFont(QFont("Arial", 10))
        painter.setPen(QPen(Qt.black))
        painter.drawText(rec, Qt.AlignCenter, 'Node {0}'.format(self.num))
        #markers
        painter.setPen(Qt.NoPen)
        painter.fillRect(QRect(self.x + 4, 4, self.resizePadding, self.h - 8), Qt.red)
        painter.fillRect(QRect(self.x + self.w - 4 - self.resizePadding, 4, self.resizePadding, self.h - 8), Qt.red)

    def adjustPos(self):
        y = self.pos().y()
        delta = y % self.h
        if delta > self.h/2:
            delta = self.h - delta
            self.setPos(self.pos() + QPoint(0, delta))
        else:
            self.setPos(self.pos() - QPoint(0, delta))

    def adjustXPos(self, items):
        #store [item, startX, width, startY, height]
        xpos = [[x, x.pos().x(),x.w, x.pos().y(), x.h] for x in items]

        for item, x, w, y, h in xpos:
            if item != self:
                if abs(self.pos().y() - y) < 2*h:
                    delta_l = ((self.pos().x()) - x) + self.w
                    delta_r = (x + w) - self.pos().x()
                    if (delta_l > self.gapL) and (delta_l < self.gapL*2):
                        self.setPos(self.pos() - QPoint(delta_l, 0))
                        break
                    if (delta_r > self.gapR) and (delta_r < self.gapR*2):
                        self.setPos(self.pos() + QPoint(delta_r, 0))
                        break
                    if (delta_l < self.gapL) and (delta_l > -self.gapL*2):
                        self.setPos(self.pos() - QPoint(delta_l, 0))
                        break
                        self.setPos(self.pos() - QPoint(delta_l, 0))
                    if (delta_r < self.gapR) and (delta_r > -self.gapR*2):
                        self.setPos(self.pos() + QPoint(delta_r, 0))
                        break









    # def adjustXPos(self, items):
    #     for i in items:
    #         delta = (self.pos().x()+self.w)-i.pos().x()
    #         print delta
    #
    #     # xpos = [[x.pos().x()] for x in items]
    #     #
    #     # for x in xpos:
    #     #     delta = (x[0]-(self.pos().x()+self.w))
    #     #     print delta
    #     #     # if delta < 0:
    #     #     #     self.setPos(self.pos() - QPoint(delta, 0))
    #     #     #     print "moved"


        # if any(self.pos().x() >= x[0] for x in xpos):
        #     delta = self.pos().x()-x[0]
        #     print delta
        #     self.setPos(self.pos()-QPoint(20, 0))
        #     print "moved"



    def checkCollision(self):
        coll = self.scene().collidingItems(self)
        if coll:
            self.setPos(self.pos()+QPoint(0, self.h))
            self.checkCollision()

    def hoverMoveEvent(self, event):
        self.hover = True
        p = event.pos().x()
        if self.x < p < self.x + self.resizePadding:
            self.setCursor(Qt.SizeHorCursor)
            self.resizeL = True
        elif self.x + self.w - self.resizePadding < p < self.w:
            self.setCursor(Qt.SizeHorCursor)
            self.resizeR = True
        else:
            self.setCursor(Qt.SizeAllCursor)
            self.resizeR = self.resizeL = False

        super(EditorItemClass, self).hoverMoveEvent(event)

    def hoverEnterEvent(self, event):
        super(EditorItemClass, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.hover = False
        super(EditorItemClass, self).hoverLeaveEvent(event)

    def mousePressEvent(self, event):
        self.startPos = event.pos()
        super(EditorItemClass, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.resizeL or self.resizeR:
            delta = (self.startPos - event.pos()).x()
            self.startPos = event.pos()
            if self.resizeL:
                tmp1= self.x
                tmp2= self.w
                self.x = self.x - delta
                self.w = self.w + delta
                if self.scene().collidingItems(self):
                    self.x = tmp1
                    self.w = tmp2
            else:
                temp = self.w
                self.w -= delta
                if self.scene().collidingItems(self):
                    self.w = temp
            if self.resizeR:
                pass
            self.scene().update()
        else:
            super(EditorItemClass, self).mouseMoveEvent(event)
