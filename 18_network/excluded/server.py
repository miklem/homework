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
        self.tcpServer = QTcpServer()
        self.tcpServer.listen(QHostAddress(QHostAddress.Any), util.PORT)
        self.tcpServer.newConnection.connect(self.createConnection)

    def createConnection(self):
        connection = self.tcpServer.nextPendingConnection()
        connection.nextBlockSize = 0
        connection.readyRead.connect(partial(self.receiveMessage, connection))
        adr = str(connection.peerAddress().toString())
        self.consoleMessage('Connect to:' + adr)

    def consoleMessage(self, text):
        self.serv_te.append(text)

    def receiveMessage(self, socket):
        if False:
            socket = QTcpSocket()
        if socket.bytesAvailable() > 0:
            stream = QDataStream(socket)
            stream.setVersion(QDataStream.Qt_4_8)
            if socket.nextBlockSize == 0:
                if socket.bytesAvailable() < SIZEOF_UINT32:
                    return
                socket.nextBlockSize = stream.readInt32()
            if socket.bytesAvailable() < socket.
        #
        #


if __name__ == '__main__':
    app = QApplication([])
    w = ServerWindow()
    w.show()
    app.exec_()
