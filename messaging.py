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

    def send_message(self, sender, receiver, message):
        # Validate the message
        if not self.is_valid_message(message):
            return {"status": "error", "message": "Invalid message format or content."}

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

    def is_valid_message(self, message):
        # Check message length
        if len(message) > 99:
            return False
        
        # Check if message is empty
        if not message.strip():
            return False
        
        # Check for invalid characters (like Emoji)
        # Example: Assuming emojis are not allowed, you can customize this check
        if any(ord(char) > 127 for char in message):
            return False
        
        # Check for Python code (basic check)
        if self.contains_python_code(message):
            return False
        
        return True

    def contains_python_code(self, message):
        # Example check for basic Python code detection
        python_keywords = ['import', 'def', 'class', 'for', 'while', 'if', 'else', 'try', 'except']
        for keyword in python_keywords:
            if keyword in message:
                return True
        return False

    def get_messages(self, user):
        # Retrieve all messages sent or received by the specified user.
        try:
            with open(self.file_path, 'r') as f:
                messages = json.load(f)
            return [msg for msg in messages if msg['sender'] == user or msg['receiver'] == user]
        except Exception as e:
            print(f"Error loading messages: {e}")
            return []  # Return an empty list in case of an error
