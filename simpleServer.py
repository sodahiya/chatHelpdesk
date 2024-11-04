import socket
import threading

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message_callback = None

def start_server():
    server_socket.bind((HOST_IP, HOST_PORT))
    server_socket.listen()
    print("Server is running...... \nOn")
    print(f"{HOST_IP}:{HOST_PORT}")

    client_socket , client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    threading.Thread(target=receive_messages, args=(client_socket,),daemon=True).start()

    return client_socket

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if message:
                print(f"Client : {message}")
                if message_callback:
                    message_callback(message)
            else:
                break
        except ConnectionResetError:
            print("Client has disconnected")
            break

    client_socket.close()

def send_message(client_socket,message):
    if client_socket:
        client_socket.send(message.encode(ENCODER))

def set_message_callback(callback):
    global message_callback
    message_callback = callback