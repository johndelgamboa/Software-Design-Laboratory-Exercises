import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
usernames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} has left the chat room!'.encode('utf-8'))
            usernames.remove(username)
            break


def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')

        client.send(''.encode('utf-8'))
        username = client.recv(1024)

        usernames.append(username)
        clients.append(client)

        print(f'The username of this client is {username}'.encode('utf-8'))
        broadcast(f'{username} has connected to the chat room '.encode('utf-8'))
        client.send('\nyou are now connected!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()