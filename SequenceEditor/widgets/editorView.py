from PySide.QtGui import *
from PySide.QtCore import *
import os
import editorScene


class EditorViewClass(QGraphicsView):
    def __init__(self, parent=None):
        super(EditorViewClass, self).__init__(parent=parent)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #hide scrolls
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.s = editorScene.EditorSceneClass()
        self.setScene(self.s)
        self.pan = False
        self.lastX = 0
        self.lastY = 0



    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.pan = True
            self.lastX = event.x()
            self.lastY = event.y()

        else:
            super(EditorViewClass, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.pan:
            self.setInteractive(False)
            valX = self.horizontalScrollBar().value() - (event.x() - self.lastX)
            self.horizontalScrollBar().setValue(valX)
            self.lastX = event.x()
            valY = self.verticalScrollBar().value() - (event.y() - self.lastY)
            self.verticalScrollBar().setValue(valY)
            self.lastY = event.y()
            self.setInteractive(True)
        else:
            super(EditorViewClass, self).mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        super(EditorViewClass, self).mouseReleaseEvent(event)
        self.pan = False

    def wheelEvent(self, event):
        zoomInFactor = 1.2
        zoomOutFactor = 1/zoomInFactor

        if event.delta()>0:
            zoom = zoomInFactor
        else:
            zoom = zoomOutFactor

        self.scale(zoom, zoom)

    def mouseWheelEvent(self, event):
        super(EditorViewClass, self).wheelEvent(event)


