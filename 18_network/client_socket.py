from PySide.QtGui import *
from PySide.QtCore import *
import os
import socket
from widgets import client_uis as ui
import util


class ClientWindow(QWidget, ui.Ui_clientForm):
    def __init__(self):
        super(ClientWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.ip_le.setText(util.IP)
        self.sock = socket.socket()
        self.conn_btn.clicked.connect(self.connectToServer)

    def connectToServer(self):
        print "trying to connect..."
        ip = self.ip_le.text()
        self.sock.connect((ip, util.PORT))
        self.sock.send('hello,world!')
        data = self.sock.recv(1024)
        self.sock.close()
        print data


if __name__ == '__main__':
    app = QApplication([])
    w = ClientWindow()
    w.show()
    app.exec_()
