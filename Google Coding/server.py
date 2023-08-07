import socket
import threading

PORT = 55840
clients = []
nickNames = []


# Creating a server listening for clients
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind(('localhost', PORT))
Server.listen()
print(f"[LISTENING] : Listening for connection.......!")


# Function for broadcasting the message

def broadCast(message):
    for client in clients:
        client.send(message)
    
# Function for handling Servers

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadCast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickName = nickNames[index]
            broadCast(f"{nickNames} Left The Chat :(".encode('ascii'))
            nickNames.remove(nickName)
            break

# Function for handling the messages

def recieve():
    while True:
        client, address = Server.accept()
        print(f"{address} Is Connected")

        clients.append(client)
        client.send("yo".encode('ascii'))
        nickName = client.recv(1024).decode("ascii")
        nickNames.append(nickNames)

        print(f"Nickname of client is {nickName}")
        broadCast(f"{nickName} Has Joined The Chat :)".encode("ascii"))
        client.send("You have been connected to the server :)".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

        
recieve()


