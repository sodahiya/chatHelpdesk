import tkinter as tk
import ttkbootstrap as ttk


window = ttk.Window(themename="cosmo")
window.title('HelpdeskClient')
window.geometry('800x600')

def connect_client():
    print("Starting server")
    client_connect_button.config(text="Connected")
    client_connect_button.config(state="disabled")
    DEST_PORT_entry.config(state="disabled")
    DEST_IP_entry.config(state="disabled")
    frame = ttk.Frame(master=window, borderwidth=10, bootstyle="success")
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    entry = ttk.Entry(master=window)
    entry.pack(fill = "x", padx = 10, pady = 10)

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
DEST_IP_entry = ttk.Entry(master=connect_frame,textvariable=DEST_IP)
DEST_IP_entry.pack(side = "left",padx = 10, pady = 10)

label = ttk.Label(master=connect_frame,text=":")
label.pack(side = "left",padx = 10, pady = 10)

DEST_PORT = tk.StringVar(value="PORT")
DEST_PORT_entry = ttk.Entry(master=connect_frame,textvariable=DEST_PORT)
DEST_PORT_entry.pack(side = "left",padx = 10, pady = 10)

client_connect_button = ttk.Button(master=connect_frame,width=20, text='Connect',command=connect_client,bootstyle = "success-outline")
client_connect_button.pack(side = "left",pady = 10)

window.mainloop()