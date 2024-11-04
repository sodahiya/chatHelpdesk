import socket
import threading

# Define Variables
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024
client_socket = None

def send_message(message):
    """Sends messages to the server."""
    if client_socket:
        client_socket.send(message.encode(ENCODER))

def receive_messages(callback):
    """Receives messages from the server and calls the provided callback to display them."""
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if not message:
                break  # Exit if the server disconnects
            callback(message)  # Call the callback function to display the message
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def connect_client(DEST_IP, message_callback):
    """Connects to the server and starts the message receiving thread."""
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((DEST_IP, DEST_PORT))
        print("Connected to the server")

        # Start a thread for receiving messages
        threading.Thread(target=receive_messages, args=(message_callback,), daemon=True).start()
    except Exception as e:
        print(f"Failed to connect to the server: {e}")
