import socket
import threading

PORT = 55840
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", PORT))

nickName = input("Enter your nickName : ")

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "yo":
                client.send(nickName.encode("ascii"))
            else:
                print(message)
        except:
            print("An error has occured")
            client.close()
            break

def write():
    while True:
        message = f"{nickName} : {input()}"
        client.send(message.encode("ascii"))


recieve_thread = threading.Thread(target=recieve)
write_thread = threading.Thread(target=write)
recieve_thread.start()
write_thread.start()

                
