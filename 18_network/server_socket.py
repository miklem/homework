from PySide.QtGui import *
from PySide.QtCore import *
import util
from PySide.QtNetwork import *
from widgets import server_uis as ui
from functools import partial
import socket

class ServerWindow(QWidget, ui.Ui_Server):
    def __init__(self):
        super(ServerWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.ip_le.setText(util.IP)
        self.sock = socket.socket()
        self.createConnection()

    def createConnection(self):
        self.sock.bind(('', 12345))
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        print "connected: ", addr
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        conn.close()
        self.consoleMessage(data)

    def consoleMessage(self, text):
        self.serv_te.append(text)


if __name__ == '__main__':
    app = QApplication([])
    w = ServerWindow()
    w.show()
    app.exec_()
