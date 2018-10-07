from PySide.QtGui import *
from PySide.QtCore import *
import os

icon = os.path.join(os.path.dirname(__file__), 'edit.png')

class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.files = []
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def startDrag(self, dropAction):
        drag = QDrag(self)
        mimedata = QMimeData()
        url = []
        for i in self.selectedItems():
            url.append(i.data(Qt.UserRole))
        mimedata.setUrls([QUrl.fromLocalFile(x) for x in url])
        drag.setMimeData(mimedata)
        pix = QPixmap(icon)
        drag.setPixmap(pix)
        r = drag.exec_()
        if r == Qt.DropAction.MoveAction:
            print r
            self.deleteSelected()

    def deleteSelected(self):
        for s in self.selectedItems():
            self.files.remove(s.data(32))
            self.takeItem(self.indexFromItem(s).row())




    def dropEvent(self,event):
        print "drop"
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.addFile(f.toLocalFile())

    def dragEnterEvent(self,event):
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            event.accept()
        else:
            event.ignore()

    def addFile(self, path):
        if not path in self.files:
            item = QListWidgetItem(self)
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.files.append(path)



if __name__ == '__main__':
    app = QApplication([])
    w = listWidgetClass()
    w.show()
    app.exec_()