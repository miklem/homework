from PySide.QtGui import *
from PySide.QtCore import *
import os
from PySide.QtNetwork import *
from widgets import client_uis as ui
import util


class ClientWindow(QWidget, ui.Ui_clientForm):
    def __init__(self):
        super(ClientWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.ip_le.setText(util.IP)

    def connectToServer(self):
        ip = self.ip_le.text()
        self.server = QTcpSocket()
        self.server.connectToHost(ip, util.PORT)

    def messageToServer(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    w = ClientWindow()
    w.show()
    app.exec_()
