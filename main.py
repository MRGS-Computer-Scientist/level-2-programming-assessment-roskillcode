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
        