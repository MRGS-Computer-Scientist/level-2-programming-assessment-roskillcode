class PushNotifications:
    def __init__(self):
        self.notifications = []
    def send_notification(self, user, notificaiton):
        self.notifications.append({"user": user, "notification": notification})
        print(f"Notification sent to {user}: {notificaiton}")
    def get_notifications(self, user):
    return [notif for notif in self.notifications if notif["user"] == user]