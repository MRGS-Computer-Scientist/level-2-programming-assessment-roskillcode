import json
import os

class Announcements:
    def __init__(self, announcements_file="announcements.json"):
        #Initialize the Announcements class and load existing announcements from a file.
        self.announcements_file = announcements_file
        self.announcements = self.load_announcements()

    def load_announcements(self):
        #Load announcements from the specified JSON file.
        if os.path.exists(self.announcements_file):
            with open(self.announcements_file, "r") as file:
                return json.load(file)
        return []

    def save_announcements(self):
        #Save the current list of announcements to the JSON file.
        with open(self.announcements_file, "w") as file:
            json.dump(self.announcements, file)

    def post_announcement(self, sender, announcement):
        #Add a new announcement and save the updated list to the file.
        self.announcements.append({"sender": sender, "announcement": announcement})
        self.save_announcements()

    def get_announcements(self):
        #Return the list of all announcements.
        return self.announcements
