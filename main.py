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
        