import socket
import threading

# Define Variables  # Update if needed
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024
client_name = "Client"

# Create and connect the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Send client Name to the server
#client_socket.send(client_name.encode(ENCODER))

def send_message():
    """Sends messages to the server."""
    while True:
        message = input(f"{client_name}: ")
        if message.lower() == 'quit':  # Handle quit gracefully
            client_socket.send(f"{client_name} has left the chat.".encode(ENCODER))
            client_socket.close()
            break  # Exit the send loop
        client_socket.send(f"{client_name}: {message}".encode(ENCODER))

def receive_message():
    """Receives messages from the server."""
    while True:
        message = client_socket.recv(BYTESIZE).decode(ENCODER)
        if not message:
            break  # Exit if the server disconnects
        print(message)

def connect_client(DEST_IP):
    """Accepts new clients and starts a thread for each one."""
    # Start send and receive threads
    print("Connected to the server ")
    client_socket.connect((DEST_IP, DEST_PORT))

    t1 = threading.Thread(target=send_message)
    t2 = threading.Thread(target=receive_message)

    t1.start()
    t2.start()