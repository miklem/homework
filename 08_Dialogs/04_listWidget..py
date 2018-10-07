from PySide.QtGui import *
import os
path = os.path.dirname(__file__)


class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.list = QListWidget()
        ly.addWidget(self.list)
        self.resize(400,200)
        self.fillList()
        self.list.itemClicked.connect(self.updateText)
        self.list.itemDoubleClicked.connect(self.openFile)

        #show content
        self.textBrowser = QTextBrowser()
        ly.addWidget(self.textBrowser)

    def fullPath(self, item):
        return os.path.join(path, item.text())

    def fillList(self):
        self.list.addItem("test")
        self.list.addItem("test2")
        for f in os.listdir(path):
            self.list.addItem(f)

    def openFile(self, item):
        path = self.fullPath(item)
        os.system(path)


    def updateText(self, item):
        # print item.text()
        text = open(self.fullPath(item)).read()
        self.textBrowser.setText(text)



if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()