import os
from PySide.QtGui import *
from PySide.QtCore import *
from IC_settings import settings
from res.icons import icons

class SourceFilesListClass(QListWidget):
    def __init__(self):
        super(SourceFilesListClass, self).__init__()
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setViewMode(QListView.ListMode)
        self.setIconSize(QSize(32, 32))
        # self.files = []
        # self.paths = []

    def startDrag(self, event):
        drag = QDrag(self)
        pix = QPixmap(icon)

    def dragEnterEvent(self, event=QDragEnterEvent):
        # calls first
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.add_object(f.toLocalFile())

    def dropEvent(self, event):
        print "drop"

    def add_object(self, path=None):
        if path:
            item = None
            type = 'file'
            if os.path.isfile(path):
                if not path in settings.files:
                    item = QListWidgetItem(self)
                    settings.files.append(path)
            elif os.path.isdir(path):
                if not path in settings.paths:
                    type = 'folder'
                    item = QListWidgetItem(self)
                    settings.paths.append(path)
                    full_path = ""
                    for root, dirs, files in os.walk(path):
                        for f in files:
                            full_path = os.path.join(root, f)
                            settings.files.append(full_path)
        else:
            pass
        if item:
            item.setIcon(QIcon(self.__set_item_icon(type)))
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)

    def del_all_item(self):
        self.clear()
        settings.files = []
        settings.paths = []

    @staticmethod
    def __set_item_icon(type="file"):
        if type == "file":
            return QIcon(icons.get('file', ""))
        if type == "folder":
            return QIcon(icons.get('folder', ""))
