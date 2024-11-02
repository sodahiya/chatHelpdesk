import tkinter as tk
import ttkbootstrap as ttk
import server

window = ttk.Window(themename="cosmo")
window.title('Helpdesk')
window.geometry('800x600')

def start_server():
    print("Starting server")
    server.start_server()
    start_server_button.config(text="Server is Running")
    start_server_button.config(state="disabled")
    frame = ttk.Frame(master=window, borderwidth=10, bootstyle="success")
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    entry = ttk.Entry(master=window)
    entry.pack(fill = "x", padx = 10, pady = 10)

header_label = ttk.Label(
    master=window,
    text="Helpdesk\nServer Control Panel",
    font=("Helvetica", 24, "bold"),
    bootstyle="dark"
)
header_label.pack(pady=30)


start_server_button = ttk.Button(master=window,width=20, text='Start Server',command=start_server,bootstyle = "success-outline")
start_server_button.pack(pady = 10)


window.mainloop()



