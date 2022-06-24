from cgitb import Hook
from codecs import decode
from pydoc import cli
from threading import Thread
from doctor import Doctor
import socket
BUFFSIZE = 1024
CODE = "utf-8"


class DoctorClientHandler(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        self.dr = Doctor()
    
    def receive(self):
        self.client.send(f"try".encode(CODE))
        while True:
            message = decode(self.client.recv(BUFFSIZE), CODE)
            if not message:
                print("Client disconnected")
                self.client.close()
                break
            else:
                self.client.send(bytes(self.dr.reply(message), CODE))


def main():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1',59000))
    server.listen()

    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')

        handler = DoctorClientHandler(client)
        handler.start()

if __name__=="__main__":
    main()