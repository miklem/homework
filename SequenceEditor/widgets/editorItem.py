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
        self.gapL = 60
        self.gapR = 60
        self.setAcceptHoverEvents(True)
        self.resizePadding = 10
        self.resizeL = False
        self.resizeR = False
        self.startPos = None
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.selected = False
        self.fontSize = 10
        self.roundness = 5


    def boundingRect(self, *args, **kwargs):
        return QRectF(self.x, self.y, self.w, self.h)

    def paint(self, painter, options, widget):
        rec = self.boundingRect()
        selectedItem = self.sceneBoundingRect()
        if False:
            painter = QPainter()
        if not self.hover:
            color = Qt.black
            self.selected = False
        else:
            color = Qt.darkGray
            self.selected = False
        if self.isSelected():
            color = Qt.yellow
            self.selected = True

        painter.setPen(QPen(color))
        linearGradient = QLinearGradient(0, selectedItem.height(), 0, 0)
        linearGradient.setColorAt(1.0, Qt.white)
        linearGradient.setColorAt(0.0, color)
        painter.setBrush(QBrush(linearGradient))
        painter.setPen(QPen(color))
        painter.drawRoundedRect(rec, self.roundness, self.roundness)

        painter.setFont(QFont("Arial", self.fontSize))
        painter.setPen(QPen(Qt.black))

        text = 'Node {0}'.format(self.num)
        font = QFont("Arial", self.fontSize)
        elided = self.elideText(selectedItem, text, font)  # note: truncate text to make it look nicer
        painter.drawText(rec, Qt.AlignCenter, elided)

        # coordinates
        font = QFont("Arial", self.fontSize)
        painter.setFont(font)
        textPos = (selectedItem.height() / 2) - self.fontSize / 2
        textL = self.elideText(rec.adjusted(15, textPos, 0, 0), '{0:.1f}'.format(selectedItem.x()), font)
        textR = self.elideText(rec.adjusted(0, textPos, -15, 0), '{0:.1f}'.format(selectedItem.width()), font)
        painter.drawText(rec.adjusted(15, textPos, 0, 0), Qt.AlignLeft, textL)
        painter.drawText(rec.adjusted(0, textPos, -15, 0), Qt.AlignRight, textR)

        # markers
        if not self.hover:
            pass
        else:
            linearGradient2 = QLinearGradient(rec.bottomLeft(), rec.bottomRight())
            linearGradient2.setColorAt(0, Qt.red)
            linearGradient2.setColorAt(0.1, QColor(255, 255, 255, 0))
            linearGradient2.setColorAt(0.9, QColor(255, 255, 255, 0))
            linearGradient2.setColorAt(1, Qt.red)
            painter.setBrush(QBrush(linearGradient2))
            painter.drawRoundedRect(rec, self.roundness, self.roundness)




    def elideText(self, item, text, font):
        metrics = QFontMetrics(font)
        if item.width() < 200:
            width = (item.width()/3.5)
        else:
            width = (item.width() / 2)
        elided = metrics.elidedText(text, Qt.ElideMiddle, width)
        return elided

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
        xpos = [[x, x.sceneBoundingRect().x(), x.sceneBoundingRect().y(), x.sceneBoundingRect().width(),
                 x.sceneBoundingRect().height()] for x in items]

        for item, x, y, w, h in xpos:
            if item != self:
                selected = self.sceneBoundingRect()
                if abs(selected.y() - y) < 2 * h:
                    delta_R_to_L = selected.x() + selected.width() - x
                    delta_R_to_R = selected.x() + selected.width() - x - w
                    delta_L_to_L = selected.x() - x
                    delta_L_to_R = selected.x() - x - w
                    if abs(delta_R_to_L) < self.gapL:
                        self.setPos(self.pos() - QPoint(delta_R_to_L, 0))
                    if abs(delta_R_to_R) < self.gapR:
                        self.setPos(self.pos() - QPoint(delta_R_to_R, 0))
                    if abs(delta_L_to_L) < self.gapL:
                        self.setPos(self.pos() - QPoint(delta_L_to_L, 0))
                    if abs(delta_L_to_R) < self.gapR:
                        self.setPos(self.pos() - QPoint(delta_L_to_R, 0))

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
                tmp1 = self.x
                tmp2 = self.w
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
