import tkinter as tk
from tkinter import ttk, messagebox
from messaging import Messaging
from announcements import Announcements
from forums import DiscussionForums
from appointments import AppointmentScheduling
from notifications import PushNotifications
from user_management import UserManagement

class CampusConnectApp:
    def __init__(self, root):
        # Initialize the application with root window, title, size, and initializations.
        self.root = root
        self.root.title("Campus Connect")
        self.root.geometry("800x600")

        self.current_user = None
        self.user_management = UserManagement()

        # Initialize various components of the application
        self.messaging = Messaging()
        self.announcements = Announcements()
        self.forums = DiscussionForums()
        self.appointments = AppointmentScheduling()
        self.notifications = PushNotifications()

        # Create login widgets on initialization
        self.create_login_widgets()

    def clear_frame(self):
        # Clear all widgets from the root frame.
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_login_widgets(self):
        # Create login interface with username, password fields and buttons.
        self.clear_frame()

        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10, expand=True)

        # Widgets for username and password entry
        title_label = ttk.Label(self.login_frame, text="Campus Connect", font=("Arial", 24))
        title_label.grid(column=0, row=0, columnspan=2, pady=20)

        username_label = ttk.Label(self.login_frame, text="Username:")
        username_label.grid(column=0, row=1, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.grid(column=1, row=1, padx=10, pady=10)

        password_label = ttk.Label(self.login_frame, text="Password:")
        password_label.grid(column=0, row=2, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(column=1, row=2, padx=10, pady=10)

        login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(column=0, row=3, padx=10, pady=10)

        signup_button = ttk.Button(self.login_frame, text="Signup", command=self.signup)
        signup_button.grid(column=1, row=3, padx=10, pady=10)

    def login(self):
        # Validate user credentials and log in.
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showwarning("Warning", "Both username and password are required.")
            return
        if self.user_management.authenticate_user(username, password):
            self.current_user = username
            self.create_main_widgets()
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

    def signup(self):
        # Create a new user account.
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showwarning("Warning", "Both username and password are required.")
            return
        if self.user_management.create_user(username, password):
            self.current_user = username
            self.create_main_widgets()
        else:
            messagebox.showerror("Error", "Username already exists. Please try another username.")

    def create_main_widgets(self):
        # Create main application interface with tabs for different functionalities.
        self.clear_frame()

        tab_control = ttk.Notebook(self.root)

        # Create tabs for different functionalities
        self.create_start_page(tab_control)
        self.create_messaging_tab(tab_control)
        self.create_announcements_tab(tab_control)
        self.create_forums_tab(tab_control)
        self.create_appointments_tab(tab_control)
        self.create_notifications_tab(tab_control)

        tab_control.pack(expand=1, fill='both')

    def create_start_page(self, tab_control):
        # Create 'Home' tab with welcome message and announcements.
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Home")
        
        welcome_label = ttk.Label(tab, text=f"Welcome to Campus Connect, {self.current_user}!", font=("Arial", 16))
        welcome_label.pack(pady=20)
        
        # Display area for announcements
        self.announcements_box = tk.Text(tab, state='disabled', width=80, height=15, bg="#f0f0f0", font=("Arial", 12))
        self.announcements_box.pack(pady=10, padx=10)

        self.load_announcements()

    def load_announcements(self):
        # Load announcements into the 'Home' tab.
        announcements = self.announcements.get_announcements()
        self.announcements_box.configure(state='normal')
        self.announcements_box.delete(1.0, 'end')
        for announcement in announcements:
            self.announcements_box.insert('end', f"{announcement['sender']}: {announcement['announcement']}\n\n")
        self.announcements_box.configure(state='disabled')

    def create_messaging_tab(self, tab_control):
        # Create 'Messaging' tab with chat functionality.
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Messaging")

        # Widgets for sending and receiving messages
        self.chat_box = tk.Text(tab, state='disabled', width=80, height=15, bg="#f0f0f0", font=("Arial", 12))
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
        self.message_entry = tk.Text(tab, height=4, width=40)
        self.message_entry.grid(column=1, row=3, padx=10, pady=10)

        send_button = ttk.Button(tab, text="Send Message", command=self.send_message)
        send_button.grid(column=1, row=4, padx=10, pady=10)

        self.load_chat_history()

    def send_message(self):
        # Send a message from one user to another.
        sender = self.sender_entry.get()
        receiver = self.receiver_entry.get()
        message = self.message_entry.get("1.0", tk.END).strip()  # Get message from Text widget and strip any extra whitespace

        if sender and receiver and message:
            new_message, error_message = self.messaging.send_message(sender, receiver, message)
            if new_message:
                self.append_message_to_chat(new_message)
                messagebox.showinfo("Success", "Message sent!")
            else:
                messagebox.showerror("Error", error_message)
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def append_message_to_chat(self, message):
        # Append a message to the chat box.
        self.chat_box.configure(state='normal')
        self.chat_box.insert('end', f"{message['sender']} to {message['receiver']}: {message['message']}\n")
        self.chat_box.configure(state='disabled')
        self.chat_box.yview('end')

    def load_chat_history(self):
        # Load chat history for the current user.
        messages = self.messaging.get_messages(self.current_user)
        for message in messages:
            self.append_message_to_chat(message)

    def create_announcements_tab(self, tab_control):
        # Create 'Announcements' tab with functionality to post announcements.
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
        # Post an announcement.
        sender = self.announcement_sender_entry.get()
        announcement = self.announcement_entry.get()
        if sender and announcement:
            self.announcements.post_announcement(sender, announcement)
            self.announcements.save_announcements()  # Save announcements to file
            messagebox.showinfo("Success", "Announcement posted!")
            self.load_announcements()  # Reload announcements on the home page
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def create_forums_tab(self, tab_control):
        # Create 'Forums' tab for discussion forums.
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Forums")
        # Add your forum functionality here

    def create_appointments_tab(self, tab_control):
        # Create 'Appointments' tab for scheduling appointments.
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Appointments")
        # Add your appointment scheduling functionality here

    def create_notifications_tab(self, tab_control):
        # Create 'Notifications' tab for managing notifications.
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text="Notifications")
        # Add your notifications functionality here


if __name__ == "__main__":
    root = tk.Tk()
    app = CampusConnectApp(root)
    root.mainloop()
