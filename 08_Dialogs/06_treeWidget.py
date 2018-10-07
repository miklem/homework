from PySide.QtGui import *
from PySide.QtCore import *
import os
path = os.path.dirname(os.path.dirname(__file__))


class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.tree = QTreeWidget()
        ly.addWidget(self.tree)
        self.tree.header().hide()
        #connect
        self.tree.itemChanged.connect(self.action)
        self.updateTree()

    #recursion
    def fillTree(self, parent = None, root = None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        if not root:
            root = path #path is taken from top
        for f in os.listdir(root):
            if f[0] in ['.', '_']: 
                continue
            item = QTreeWidgetItem()
            item.setText(0, f)
            parent.addChild(item)
            fullpath = os.path.join(root, f)
            if os.path.isdir(fullpath):
                self.fillTree(item, fullpath)
            else:
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                item.setData(0, Qt.UserRole, {'path':os.path.normpath(fullpath)})
    
    
    def updateTree(self):
        self.tree.blockSignals(True)
        self.fillTree()
        self.tree.blockSignals(False)


    def action(self, item):
        print item.text(0)
        print item.data(0, Qt.UserRole)
        print os.path.dirname(item.data(0, Qt.UserRole))
        #rename(old path, new path)
        os.rename(item.data(0, Qt.UserRole), os.path.join(os.path.dirname(item.data(0, Qt.UserRole)), item.text(0)))

        # item = QTreeWidgetItem()
        # item.setText(0, "item")
        # self.tree.addTopLevelItem(item)

        # item = QTreeWidgetItem()
        # item.setText(0, "item2")
        # self.tree.invisibleRootItem().addChild(item)




if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()


