import flet as ft
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
# Defining the page of GUI
def main(page :ft.Page):
    page.window_height = 500
    page.window_width = 500
    page.update()
    canvas = ft.Column(height=390,alignment=ft.MainAxisAlignment.START)
    message = ft.TextField(height=45, width=380, cursor_height=20 ,icon=ft.icons.EMOJI_EMOTIONS, autofocus=True)
    def send_msg(i):
        canvas.controls.append(ft.Text(message.value))
        message.value = ""
        page.update()
        
    
    page.add(
        canvas,ft.Row(controls=[message, ft.ElevatedButton("send", on_click=send_msg)])
    )
    
    
    
 
ft.app(target=main)
