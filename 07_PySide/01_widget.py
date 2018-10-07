from PySide.QtGui import *
from PySide.QtCore import *

class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.label = QLabel("text")
        self.layout.addWidget(self.label)
        self.button = QPushButton("button")
        self.layout.addWidget(self.button)

        self.line = QLineEdit()
        self.line.textChanged.connect(self.text)
        self.layout.addWidget(self.line)

        @self.button.clicked.connect
        #change text on click
        def click():
            if self.line.text() !="":
                self.label.setText(self.line.text())
                self.replace()
            else:
                print "empty"


    def text(self, arg):
        #rename label as I type here
        # self.label.setText(self.line.text())
        pass


    def replace(self):
        
        pass


app = QApplication([])
w = myWidget()
w.show()
app.exec_()
