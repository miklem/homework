from PySide.QtCore import *
from PySide.QtGui import *

class CustomDialogClass(QDialog):
    def __init__(self):
        super(CustomDialogClass, self).__init__()

        self.ly = QVBoxLayout(self)
        self.le = QLineEdit()

        self.ly.addWidget(self.le)

        self.ok_btn = QPushButton("ok")
        self.ly.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton("cancel")
        self.ly.addWidget(self.cancel_btn)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)


    def getData(self):
        return dict(text = self.le.text())
        