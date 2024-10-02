import socket
import threading

HOST = '20.20.17.40'  # localhost
PORT = 55555
clients = []
usernames = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} left the chatroom!".encode('ascii'))
            usernames.remove(username)
            break

def receive(server):
    while True:
        Client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send('username'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)
        
        print(f"username of the client is {username}!")
        broadcast(f"{username} joined the chat!".encode('ascii'))
        client.send("Connected to the server!".encode('ascii'))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
    
print("Sever is listening")
receive(server_socket)
