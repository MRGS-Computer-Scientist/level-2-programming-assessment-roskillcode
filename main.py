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


    def create_announcements_tab(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Announcements")

        sender_label = ttk.Label(tab, text="Sender:")
        sender_label.grid(column=0, row=0, padx=10, pady=10)
        self.announcement_sender_entry = ttk.Entry(tab)
        self.announcement_sender_entry.grid(column=1, row=0, padx=10, pady=10)

        announcement_label = ttk.Label(tab, text="Announcement:")
        announcement_label.grid(column=0, row=1, padx=10, pady=10)
        self.announcement_entry = ttk.Entry(tab)
        self.announcement_entry.grid(column=1, row=1, padx=10, pady=10)

        post_button = ttk.Button(tab, text="Post Announcement", command=self.post_announcement)
        post_button.grid(column=1, row=2, padx=10, pady=10)
        
    def post_announcement(self):
        sender = self.announcement_sender_entry.get()
        announcement = self.announcement_entry.get()
        self.announcements.post_announcement(sender, announcement)
        messagebox.showinfo("Success", "Announcement posted!")
        
    def create_forums_tab(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Forums")

        user_label = ttk.Label(tab, text="User:")
        user_label.grid(column=0, row=0, padx=10, pady=10)
        self.forum_user_entry = ttk.Entry(tab)
        self.forum_user_entry.grid(column=1, row=0, padx=10, pady=10)

        topic_label = ttk.Label(tab, text="Topic:")
        topic_label.grid(column=0, row=1, padx=10, pady=10)
        self.forum_topic_entry = ttk.Entry(tab)
        self.forum_topic_entry.grid(column=1, row=1, padx=10, pady=10)

        post_button = ttk.Button(tab, text="Post Topic", command=self.post_topic)
        post_button.grid(column=1, row=2, padx=10, pady=10)


    def post_topic(self):
        user = self.forum_user_entry.get()
        topic = self.forum_topic_entry.get()
        self.forums.post_topic(user, topic)
        messagebox.showinfo("Success", "Topic posted!")
        
    def create_appointments_tab(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Appointments")

        student_label = ttk.Label(tab, text="Student:")
        student_label.grid(column=0, row=0, padx=10, pady=10)
        self.student_entry = ttk.Entry(tab)
        self.student_entry.grid(column=1, row=0, padx=10, pady=10)

        faculty_label = ttk.Label(tab, text="Faculty:")
        faculty_label.grid(column=0, row=1, padx=10, pady=10)
        self.faculty_entry = ttk.Entry(tab)
        self.faculty_entry.grid(column=1, row=1, padx=10, pady=10)

        datetime_label = ttk.Label(tab, text="DateTime:")
        datetime_label.grid(column=0, row=2, padx=10, pady=10)
        self.datetime_entry = ttk.Entry(tab)
        self.datetime_entry.grid(column=1, row=2, padx=10, pady=10)

        schedule_button = ttk.Button(tab, text="Schedule Appointment", command=self.schedule_appointment)
        schedule_button.grid(column=1, row=3, padx=10, pady=10)

                    
                   



if __name__ == "__main__":
    root = tk.Tk()
    app = CampusConnectApp(root)
    root.mainloop()
        

        
        
            
        