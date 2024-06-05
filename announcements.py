class Announcements:
    def __init__(self):
        self.announcements = []

    def post_announcement(self, sender, announcement):
        self.announcements.append({"sender": sender, "announcement": announcement})
        print(f"Announcement posted by {sender}: {announcement}")

    def get_announcements(self):
        return self.announcements
