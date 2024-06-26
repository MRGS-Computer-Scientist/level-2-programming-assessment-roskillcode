import json
import os

class UserManagement:
    def __init__(self, user_data_file="users.json"):
        # Initialize the UserManagement class with the path to the user data file.
        self.user_data_file = user_data_file
        self.users = self.load_users()

    def load_users(self):
        # Load users from the user data file if it exists, otherwise return an empty dictionary.
        if os.path.exists(self.user_data_file):
            with open(self.user_data_file, "r") as file:
                return json.load(file)
        return {}

    def save_users(self):
        # Save the current users to the user data file.
        with open(self.user_data_file, "w") as file:
            json.dump(self.users, file)

    def authenticate_user(self, username, password):
        # Check if the username exists and the password matches.
        if username in self.users and self.users[username] == password:
            return True
        return False

    def create_user(self, username, password):
        # Create a new user if the username does not already exist.
        if username not in self.users:
            self.users[username] = password
            self.save_users()
            return True
        return False
