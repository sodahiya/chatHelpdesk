import socket
import threading

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

client_socket_list = []
client_name_dist = {}

def broadcast_message(message, sender_socket=None):
    """Broadcast a message to all clients except the sender."""
    for client in client_socket_list:
        if client != sender_socket:  # Avoid echoing back to the sender
            client.send(message.encode(ENCODER))

def handle_client(client_socket):
    """Receives messages from a client and handles them."""
    # Receive the client name from the client
    client_name = client_socket.recv(BYTESIZE).decode(ENCODER)
    client_name_dist[client_socket] = client_name  # Store the name

    welcome_message = f"{client_name} has joined the chat."
    print(welcome_message)
    broadcast_message(welcome_message, client_socket)

    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if not message or message.lower() == "quit":
                leave_message = f"{client_name} has left the chat."
                print(leave_message)
                broadcast_message(leave_message, client_socket)
                client_socket_list.remove(client_socket)
                client_socket.close()
                break

            print(f"{message}")
            broadcast_message(f"{message}", client_socket)
        except ConnectionResetError:
            # Handle abrupt disconnections
            leave_message = f"{client_name} has unexpectedly disconnected."
            print(leave_message)
            broadcast_message(leave_message, client_socket)
            client_socket_list.remove(client_socket)
            client_socket.close()
            break

def connect_client():
    """Accepts new clients and starts a thread for each one."""
    while True:
        client_socket, address = server_socket.accept()
        client_socket_list.append(client_socket)
        print(f"Connected to {address}")

        # Start a new thread to handle the connected client
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def start_server():
    print(HOST_IP)
    print("Server is Running...")

    connection_thread = threading.Thread(target=connect_client)
    connection_thread.start()