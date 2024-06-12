import json
import os

class UserManagement:
    def __init__(self):
        self.file_path = 'users.json'
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def save_user(self, username, password):
        with open(self.file_path, 'r') as f:
            users = json.load(f)
        if username in users:
            return False
        users[username] = password
        with open(self.file_path, 'w') as f:
            json.dump(users, f)
        return True

    def verify_user(self, username, password):
        with open(self.file_path, 'r') as f:
            users = json.load(f)
        if username in users and users[username] == password:
            return True
        return False
