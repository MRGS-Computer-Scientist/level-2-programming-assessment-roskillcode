class PushNotifications:
    def __init__(self):
        # Initialize the PushNotifications class with an empty list of notifications.
        self.notifications = []
        
    def send_notification(self, user, notification):
        # Send a notification to the specified user and print a confirmation message.
        self.notifications.append({"user": user, "notification": notification})
        print(f"Notification sent to {user}: {notification}")

    def get_notifications(self, user):
        # Retrieve all notifications for the specified user.
        return [notif for notif in self.notifications if notif["user"] == user]
