import tkinter as tk
import ttkbootstrap as ttk
import simpleClient

window = ttk.Window(themename="cosmo")
window.title('Helpdesk Client')
window.geometry('800x600')

chat_frame = None
message_entry = None
canvas = None
scrollbar = None

def display_message_server(message):
    """Display a new message from the server in the chat frame."""
    message_label = ttk.Label(master=chat_message_frame, text=f"Server : {message}", bootstyle="info")
    message_label.pack(fill="x", padx=10, pady=5, anchor="w")
    # Auto-scroll to the bottom
    canvas.yview_moveto(1)

def display_message_client(message):
    """Display a new message from the client in the chat frame."""
    message_label = ttk.Label(master=chat_message_frame, text=f"Client : {message}", bootstyle="secondary")
    message_label.pack(fill="x", padx=10, pady=5, anchor="w")
    # Auto-scroll to the bottom
    canvas.yview_moveto(1)

def connect_client():
    dest_ip = DEST_IP.get()
    simpleClient.connect_client(dest_ip, display_message_server)  # Pass the callback

    print("Connected")
    client_connect_button.config(text="Connected")
    client_connect_button.config(state="disabled")
    DEST_PORT_entry.config(state="disabled")
    DEST_IP_entry.config(state="disabled")

    # Initialize the chat frame for displaying messages
    global chat_frame, chat_message_frame, canvas, scrollbar
    chat_frame = ttk.Frame(master=window, borderwidth=10)
    chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(chat_frame)
    scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    # Configure scrolling
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Make the scrollable frame available for message display
    chat_message_frame = scrollable_frame

    # Input and Send Button
    send_frame = ttk.Frame(master=window)
    send_frame.pack(fill="x", padx=10, pady=10)
    global message_entry
    message_entry = ttk.Entry(master=send_frame)
    message_entry.pack(side="left", fill="x", expand=True, padx=10)
    message_entry.bind("<Return>", lambda event: send_message(message_entry.get()))  # Call send_message on Enter key press

    send_button = ttk.Button(master=send_frame, text="Send", command=lambda: send_message(message_entry.get()), bootstyle="primary")
    send_button.pack(side="left", padx=10)

def send_message(message):
    if message:
        simpleClient.send_message(message)
        display_message_client(message)
        message_entry.delete(0, tk.END)  # Clear the entry box

header_label = ttk.Label(
    master=window,
    text="Helpdesk\nClient Control Panel",
    font=("Helvetica", 24, "bold"),
    bootstyle="dark"
)
header_label.pack(pady=30)

connect_frame = ttk.Frame(master=window, borderwidth=10)
connect_frame.pack()

DEST_IP = tk.StringVar(value="IP ADDRESS")
DEST_IP_entry = ttk.Entry(master=connect_frame, textvariable=DEST_IP)
DEST_IP_entry.pack(side="left", padx=10, pady=10)

label = ttk.Label(master=connect_frame, text=":")
label.pack(side="left", padx=10, pady=10)

DEST_PORT = tk.StringVar(value="12345")
DEST_PORT_entry = ttk.Entry(master=connect_frame, textvariable=DEST_PORT)
DEST_PORT_entry.pack(side="left", padx=10, pady=10)

client_connect_button = ttk.Button(master=connect_frame, width=20, text='Connect', command=connect_client, bootstyle="success-outline")
client_connect_button.pack(side="left", pady=10)

# Start the main event loop
window.mainloop()
