import tkinter as tk
import json
from tkinter import ttk, messagebox
from messaging import Messaging
from announcements import Announcements
from forums import DiscussionForums
from appointments import AppointmentScheduling
from notifications import PushNotifications



    
    
    
class CampusConnectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Connect")

        self.current_user = "hamish"  # Replace with actual logic to get current user

        self.messaging = Messaging()
        self.announcements = Announcements()
        self.forums = DiscussionForums()
        self.appointments = AppointmentScheduling()
        self.notifications = PushNotifications()

        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        self.create_start_page(tab_control)
        self.create_messaging_tab(tab_control)
        self.create_announcements_tab(tab_control)
        self.create_forums_tab(tab_control)
        self.create_appointments_tab(tab_control)
        self.create_notifications_tab(tab_control)

        tab_control.pack(expand=1, fill='both')

    def create_start_page(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Home")
        welcome_label = ttk.Label(tab, text="Welcome to Campus Connect!", font=("Arial", 16))
        welcome_label.pack(pady=20)

    def create_messaging_tab(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Messaging")

        self.chat_box = tk.Text(tab, state='disabled', width=50, height=15)
        self.chat_box.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        sender_label = ttk.Label(tab, text="Sender:")
        sender_label.grid(column=0, row=1, padx=10, pady=10)
        self.sender_entry = ttk.Entry(tab)
        self.sender_entry.grid(column=1, row=1, padx=10, pady=10)

        receiver_label = ttk.Label(tab, text="Receiver:")
        receiver_label.grid(column=0, row=2, padx=10, pady=10)
        self.receiver_entry = ttk.Entry(tab)
        self.receiver_entry.grid(column=1, row=2, padx=10, pady=10)

        message_label = ttk.Label(tab, text="Message:")
        message_label.grid(column=0, row=3, padx=10, pady=10)
        self.message_entry = ttk.Entry(tab)
        self.message_entry.grid(column=1, row=3, padx=10, pady=10)

        send_button = ttk.Button(tab, text="Send Message", command=self.send_message)
        send_button.grid(column=1, row=4, padx=10, pady=10)

        self.load_chat_history()

    def send_message(self):
        sender = self.sender_entry.get()
        receiver = self.receiver_entry.get()
        message = self.message_entry.get()

        if sender and receiver and message:
            new_message = self.messaging.send_message(sender, receiver, message)
            if new_message:  # Check if new_message is not None
                self.append_message_to_chat(new_message)
                messagebox.showinfo("Success", "Message sent!")
            else:
                messagebox.showerror("Error", "Failed to send message. Please try again.")
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def append_message_to_chat(self, message):
        self.chat_box.configure(state='normal')
        self.chat_box.insert('end', f"{message['sender']} to {message['receiver']}: {message['message']}\n")
        self.chat_box.configure(state='disabled')
        self.chat_box.yview('end')

    def load_chat_history(self):
        messages = self.messaging.get_messages(self.current_user)
        for message in messages:
            self.append_message_to_chat(message)

    def create_announcements_tab(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Announcements")

        # Announcement posting section
        post_frame = ttk.LabelFrame(tab, text="Post New Announcement")
        post_frame.grid(column=0, row=0, padx=10, pady=10, sticky="ew")

        sender_label = ttk.Label(post_frame, text="Sender:")
        sender_label.grid(column=0, row=0, padx=10, pady=5)
        self.announcement_sender_entry = ttk.Entry(post_frame)
        self.announcement_sender_entry.grid(column=1, row=0, padx=10, pady=5)

        announcement_label = ttk.Label(post_frame, text="Announcement:")
        announcement_label.grid(column=0, row=1, padx=10, pady=5)
        self.announcement_entry = ttk.Entry(post_frame)
        self.announcement_entry.grid(column=1, row=1, padx=10, pady=5)

        post_button = ttk.Button(post_frame, text="Post Announcement", command=self.post_announcement)
        post_button.grid(column=1, row=2, padx=10, pady=5, sticky="e")

        # Announcements display section
        display_frame = ttk.LabelFrame(tab, text="Announcements")
        display_frame.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")

        self.announcement_listbox = tk.Listbox(display_frame, height=10, width=50)
        self.announcement_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        scrollbar = ttk.Scrollbar(display_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.announcement_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.announcement_listbox.yview)

        self.load_announcements()

    def post_announcement(self):
        sender = self.announcement_sender_entry.get()
        announcement = self.announcement_entry.get()
        if sender and announcement:
            self.announcements.post_announcement(sender, announcement)
            self.load_announcements()
            messagebox.showinfo("Success", "Announcement posted!")
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def load_announcements(self):
        self.announcement_listbox.delete(0, tk.END)
        announcements = self.announcements.get_announcements()
        for announcement in announcements:
            self.announcement_listbox.insert(tk.END, f"{announcement['sender']}: {announcement['announcement']}")

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
        if user and topic:
            self.forums.post_topic(user, topic)
            messagebox.showinfo("Success", "Topic posted!")
        else:
            messagebox.showwarning("Warning", "All fields are required!")

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

    def schedule_appointment(self):
        student = self.student_entry.get()
        faculty = self.faculty_entry.get()
        datetime = self.datetime_entry.get()
        if student and faculty and datetime:
            self.appointments.schedule_appointment(student, faculty, datetime)
            messagebox.showinfo("Success", "Appointment scheduled!")
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def create_notifications_tab(self, tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Notifications")

        user_label = ttk.Label(tab, text="User:")
        user_label.grid(column=0, row=0, padx=10, pady=10)
        self.notification_user_entry = ttk.Entry(tab)
        self.notification_user_entry.grid(column=1, row=0, padx=10, pady=10)

        notification_label = ttk.Label(tab, text="Notification:")
        notification_label.grid(column=0, row=1, padx=10, pady=10)
        self.notification_entry = ttk.Entry(tab)
        self.notification_entry.grid(column=1, row=1, padx=10, pady=10)

        send_button = ttk.Button(tab, text="Send Notification", command=self.send_notification)
        send_button.grid(column=1, row=2, padx=10, pady=10)

    def send_notification(self):
        user = self.notification_user_entry.get()
        notification = self.notification_entry.get()
        if user and notification:
            self.notifications.send_notification(user, notification)
            messagebox.showinfo("Success", "Notification sent!")
        else:
            messagebox.showwarning("Warning", "All fields are required!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CampusConnectApp(root)
    root.mainloop()
