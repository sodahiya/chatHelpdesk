import tkinter as tk
import ttkbootstrap as ttk
import client
import server
window = ttk.Window()
window.title('Helpdesk')
window.geometry('800x600')

notebook = ttk.Notebook(window)
server_frame = ttk.Frame(notebook)
client_frame = ttk.Frame(notebook)

notebook.add(server_frame, text='Server')
notebook.add(client_frame, text='Client')
notebook.pack()

#server Layout

start_Server_button = ttk.Button(server_frame, text='Start Server', command = lambda : server.start_server())
start_Server_button.pack()

#client Layout
name_entry = ttk.Entry(client_frame)
name_entry.pack()
host_ip_entry = ttk.Entry(client_frame)
host_ip_entry.pack()
connect_client_button = ttk.Button(client_frame, text='Connect Client',command=lambda: client.connect_client(host_ip_entry.get()))
connect_client_button.pack()



window.mainloop()



