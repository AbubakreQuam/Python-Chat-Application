#Importing modules

from datetime import date
import time, socket, sys
import Tkinter as tk
top = tk.Tk()

#Frame Title
top.title("SERVER SECURED ENHANCED PYTHON CHAT APP INTERFACE")

#Message send function
def send():
    messages= entry_field.get()
    message= "You:  "+ messages
    entry_field.insert(tk.END, " ")
    conn.send(messages.encode())
    msg_list1.insert(tk.END, message)
    msg_list.insert(tk.END, message)

#Message recieve function
def receive():
    s_name = conn.recv(1024)
    s_name = s_name.decode()
    messag= "Available Client:  "+ s_name
    msg_list1.insert(tk.END, messag)
    msg_list.insert(tk.END, messag)


messages_frame = tk.Frame(top) 
#Using date fuction to get today's date
today= date.today()
today_date = today.strftime("%B %d, %Y")
my_msg1= "ENCRYPTED CHAT MESSSAGES" + "     " + today_date
scrollbar = tk.Scrollbar(messages_frame)  
# Following will contain the messages.
msg_list = tk.Listbox(messages_frame, bg='black', fg='white',  height=30, width=80, yscrollcommand=scrollbar.set)
msg_list.insert(tk.END, my_msg1)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
msg_list.pack(side=tk.RIGHT)
msg_list.pack()
messages_frame.pack()
entry_field = tk.Entry(top, width=166)
entry_field.insert(tk.END, "Type your message")
entry_field.pack()
send_button = tk.Button(top, bd="10px", text="SEND MESSAGE", width=70, command=send)
send_button.pack(side=tk.RIGHT)
send_button1 = tk.Button(top, bd="10px", text="RECEIVE MESSAGE", width=70, command=receive)
send_button1.pack(side=tk.LEFT)


my_msg= "DECRYPTED CHAT MESSSAGES"+ "     " + today_date
scrollbar1 = tk.Scrollbar(messages_frame) 
# Following will contain the messages.
msg_list1 = tk.Listbox(messages_frame, bg='white', fg='black', height=30, width=80,  yscrollcommand=scrollbar.set)
msg_list1.insert(tk.END, my_msg)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
msg_list1.pack(side=tk.LEFT)
msg_list1.pack()
messages_frame.pack()
top.protocol("WM_DELETE_WINDOW")
print("\nEstablishing Connection....\n")
print("Initialising....\n")
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print (str(host + "   " + ip))   
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0])
tk.mainloop()