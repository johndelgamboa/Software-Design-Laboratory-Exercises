from pydoc import cli
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys
import socket
from codecs import decode




BUFFSIZE = 1024
CODE = "utf-8"

class doctor(QDialog):
    def __init__(self, ):
        super(doctor, self).__init__()
        loadUi('C:/Users/Marlon/Desktop/2nd Year/2nd Sem/SD/Laboratories/Lab no 6/Postlab/Vs code/2/doctor.ui', self)

        self.connectbtn.clicked.connect(self.Connect)
        self.disconnectbtn.clicked.connect(self.Disconnect)
        self.replybtn.clicked.connect(self.send_reply)


    def Connect(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.connect(('127.0.0.1',59000))
            #msg = self.server.recv(BUFFSIZE)

            #print(msg.decode(CODE))
  
        except:
            self.chatbox.setText("No server found!")

    def Disconnect(self):
        self.server.close()
        self.chatbox.setText('Disconnected from the doctor')

    def send_reply(self):
        cli_input = self.reply.text()
        if cli_input != "":
            self.server.send(bytes(f"{cli_input}", CODE))
            drReply = decode(self.server.recv(BUFFSIZE), CODE)

            if not drReply:
                self.chatbox.setText("Doctor disconnected")
                self.Disconnect()
            else:
                self.chatbox.setText(drReply)


app = QApplication(sys.argv)
mainwindow = doctor()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(463)
widget.setFixedHeight(200)
widget.show()
app.exec_()