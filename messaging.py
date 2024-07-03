import json
import os
import re

class Messaging:
    def __init__(self):
        # Initialize the Messaging class by creating an empty messages file if it doesn't exist.
        self.file_path = 'messages.json'
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def is_valid_message(self, message):
        # Check if the message meets the requirements
        if len(message) > 99:
            return False, "Message cannot be longer than 99 characters."
        if len(message.strip()) == 0:
            return False, "Message cannot be empty."
        if re.search(r'[^\x00-\x7F]', message):  # Checks for non-ASCII characters
            return False, "Message contains invalid characters. Emojis and non-ASCII characters are not allowed."
        if re.search(r'\bimport\b|\bexec\b|\beval\b|\bos\b', message):  # Checks for Python keywords
            return False, "Message contains potentially dangerous content. Python code is not allowed."
        return True, ""

    def send_message(self, sender, receiver, message):
        # Validate the message before sending
        is_valid, error_message = self.is_valid_message(message)
        if not is_valid:
            return None, error_message

        # Send a message from sender to receiver and save it to the messages file.
        new_message = {'sender': sender, 'receiver': receiver, 'message': message}
        try:
            with open(self.file_path, 'r') as f:
                messages = json.load(f)
            messages.append(new_message)
            with open(self.file_path, 'w') as f:
                json.dump(messages, f)
            return new_message, ""
        except Exception as e:
            print(f"Error sending message: {e}")
            return None, "Failed to send message due to an internal error."

    def get_messages(self, user):
        # Retrieve all messages sent or received by the specified user.
        try:
            with open(self.file_path, 'r') as f:
                messages = json.load(f)
            return [msg for msg in messages if msg['sender'] == user or msg['receiver'] == user]
        except Exception as e:
            print(f"Error loading messages: {e}")
            return []  # Return an empty list in case of an error
