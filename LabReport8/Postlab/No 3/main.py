from unicodedata import name
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys
import threading
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Chatroom(QDialog):
    def __init__(self, ):
        super(Chatroom, self).__init__()
        loadUi('C:/Users/User/Desktop/Postlab6\No 3/chatroom.ui', self)   
        self.replybtn.clicked.connect(self.send)
        self.connectbtn.clicked.connect(self.connect)
        self.discobtn.clicked.connect(self.disconnect_server)
        self.replybtn.setDefault(False)
        self.reply.setReadOnly(True)
        self.discobtn.setDefault(False)
        self.connected = False

    def send(self):
        line = self.reply.text()
        if line =="":
            return
        send_msg = f"{self.username}: {line}"
        client.send(send_msg.encode('utf-8'))
        self.reply.clear()

    def client_receive(self):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == "":
                    return
                else:
                    print(message)
                    self.chatbox.append(message)
            except:
                print('Error!')
                client.close()
                break

    def connect(self):
        if self.connected == True:
            return

        username = self.usernameLine.text()
        if username == "":
            self.status.setText("Status: "+"Please Enter your name")
            return

        self.username = username       
        try:
            client.connect(('127.0.0.1', 59000))
        except:
            self.status.setText("Status: "+"Server offline")
            return

        client.send(username.encode('utf-8'))
        self.status.setText("Status:"+"Connected")
        self.connected = True
        self.usernameLine.setReadOnly(True)
        self.replybtn.setDefault(True)
        self.reply.setReadOnly(False)
        self.connectbtn.setDefault(False)
        self.discobtn.setDefault(True)

        receive_thread = threading.Thread(target=self.client_receive)
        send_thread = threading.Thread(target=self.send)
        
        send_thread.start()
        receive_thread.start()

    def disconnect_server(self):
        self.usernameLine.clear()
        if self.connected == False:
            return
        self.status.setText("Status: "+"Disconnected")
        self.usernameLine.setReadOnly(False)
        self.replybtn.setDefault(False)
        self.reply.setReadOnly(True)
        client.close()

    
app = QApplication(sys.argv)
mainwindow = Chatroom()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(730)
widget.setFixedHeight(394)
widget.show()
app.exec_()