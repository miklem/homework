from PySide.QtGui import *
from PySide.QtCore import *

class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.label = QLabel('text')
        layout.addWidget(self.label)
        self.button = QPushButton("press")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.action)

    def action(self):
        self.label.setText('new text')
        self.button.setText('pressed')
        


if __name__=='__main__':
    app = QApplication([])
    w = myWidget()
    w.show()
    app.exec_()
