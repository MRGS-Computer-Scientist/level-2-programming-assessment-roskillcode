import json
import os

class Announcements:
    def __init__(self, announcements_file="announcements.json"):
        self.announcements_file = announcements_file
        self.announcements = self.load_announcements()

    def load_announcements(self):
        if os.path.exists(self.announcements_file):
            with open(self.announcements_file, "r") as file:
                return json.load(file)
        return []

    def save_announcements(self):
        with open(self.announcements_file, "w") as file:
            json.dump(self.announcements, file)

    def post_announcement(self, sender, announcement):
        self.announcements.append({"sender": sender, "announcement": announcement})
        self.save_announcements()

    def get_announcements(self):
        return self.announcements
