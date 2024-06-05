import tkinter as tk
from tkinter import ttk, messagebox
from messaging import Messaging
from announcements import Announcements
from forums import DiscussionForums
from appointments import AppointmentScheduling
from notifications import PushNotifications




class CampusConnect:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Connect")
        
        self.messagomg = Messaging()
        self.announcments = Announcements()
        self.fourms = DiscussionForums()
        self.appointments = AppointmentScheduling()
        self.notifications = PushNotifications()
        
        self.create_widgets()
        
    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)
        
        self.create_messaging_tab(tab_control)
        self.create_announcments_tab(tab_control)
        self.create_forums_tab(tab_control)
        self.create_appointments_tab(tab_control)
        self.create_notifications_tab(tab_control)
        
        tab_control.pack(expand=1, fill='both')
        
    def create_messaging_tab(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Messaging")
        
        sender_label = ttk.Label(tab, text="Sender")
        sender_label.grid(colum=0, row= 0, padx=10, pady=10)
        self.sender_entry = ttk.Entry(tab)
        self.sender_entry.grid(column=1, row=0, padx=10, pady=10)
        
        receiver_label = ttk.Label(tab, text="Receiver: ")
        receiver_label.grid(column=0, row=1, padx=10, pady=10)
        self.receiver_entry = ttk.Entry(tab)
        self.receiver_entry.grid(column=1, row=1, padx=10, pady=10)
        
        message_label = ttk.Label(tab, text="Message:")
        message_label.grid(column=0, row=2, padx=10, pady=10)
        self.message_entry = ttk.Entry(tab)
        self.message_entry.grid(column=1, row=2, padx=10, pady=10)

        send_button = ttk.Button(tab, text="Send Message", command=self.send_message)
        send_button.grid(column=1, row=3, padx=10, pady=10)
        
        def send_message(self):
            sender = self.sender_entry.get()
            reciver = self.receiver_entry.get()
            message = self.message_entry.get()
            self.messaging.send_message(sender, reciver, message)
            messagebox.showinfo("Success", "Message sent!")
        
        
            
                   



if __name__ == "__main__":
    root = tk.Tk()
    app = CampusConnectApp(root)
    root.mainloop()
        

        
        
            
        