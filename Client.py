#Importing modules

import socket, sys, time
import Tkinter as tk, tkMessageBox
from datetime import date
top = tk.Tk()

#Frame Title
top.title("CLIENT SECURED ENHANCED PYTHON CHAT APP INTERFACE")

#Message send function

def send():  
    messages= entry_field.get()
    message= "You:  "+ messages
    #clearing input field
    entry_field.insert(tk.END, " ")
    s.send(messages.encode())
    msg_list1.insert(tk.END, message)
    msg_list.insert(tk.END, message)
    
#Message receive function    

def receive():
    s_name = s.recv(1024)
    s_name = s_name.decode()
    messag= "Available Server:  "+ s_name
    msg_list1.insert(tk.END, messag)
    msg_list.insert(tk.END, messag)


messages_frame = tk.Frame(top)


#Using date fuction to get today's date
today= date.today()
today_date =today.strftime("%B %d, %Y")
my_msg1= "ENCRYPTED CHAT MESSSAGES" + "     " + today_date
scrollbar = tk.Scrollbar(messages_frame)  

# Following will contain the messages.
msg_list = tk.Listbox(messages_frame, bg='black', fg='white', height=30, width=80, yscrollcommand=scrollbar.set)
msg_list.insert(tk.END,  my_msg1)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
msg_list.pack(side=tk.RIGHT)
msg_list.pack()
messages_frame.pack()


entry_field = tk.Entry(top, width=166)
entry_field.insert(tk.END, "Type your message")
entry_field.pack()
send_button = tk.Button(top, bd="10px",text="SEND MESSAGE", width=70, command=send)
send_button.pack(side=tk.RIGHT)
send_button1 = tk.Button(top, bd="10px", text="RECEIVE MESSAGE", width=70, command=receive)
send_button1.pack(side=tk.LEFT)


my_msg= "DECRYPTED CHAT MESSSAGES" + "     " + today_date
scrollbar1 = tk.Scrollbar(messages_frame)  

# Following will contain the messages.
msg_list1 = tk.Listbox(messages_frame, bg='white', fg='black', height=30, width=80,  yscrollcommand=scrollbar.set)
msg_list1.insert(tk.END, my_msg)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
msg_list1.pack(side=tk.LEFT)
msg_list1.pack()
messages_frame.pack()


top.protocol("WM_DELETE_WINDOW")

print("\nWelcome to Chat Room\n")
print("Initialising....\n")

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
("Input")
host = input("Input Host Ip Address: ")
name = str("Tepman")
port = input("Input Port Number: ")
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")
tk.mainloop()
