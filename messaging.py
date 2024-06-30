import json
import os

class Messaging:
    def __init__(self):
        # Initialize the Messaging class by creating an empty messages file if it doesn't exist.
        self.file_path = 'messages.json'
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def send_message(self, sender, receiver, message):
        # Send a message from sender to receiver and save it to the messages file.
        new_message = {'sender': sender, 'receiver': receiver, 'message': message}
        try:
            with open(self.file_path, 'r') as f:
                messages = json.load(f)
            messages.append(new_message)
            with open(self.file_path, 'w') as f:
                json.dump(messages, f)
            return new_message  # Return the new message
        except Exception as e:
            print(f"Error sending message: {e}")
            return None  # Return None in case of an error

    def get_messages(self, user):
        # Retrieve all messages sent or received by the specified user.
        try:
            with open(self.file_path, 'r') as f:
                messages = json.load(f)
            return [msg for msg in messages if msg['sender'] == user or msg['receiver'] == user]
        except Exception as e:
            print(f"Error loading messages: {e}")
            return []  # Return an empty list in case of an error
