class Messaging:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, message):
        self.messages.append({"sender": sender, "receiver": receiver, "message": message})
        print(f"Message sent from {sender} to {receiver}: {message}")

    def get_messages(self, user):
        return [msg for msg in self.messages if msg["receiver"] == user or msg["sender"] == user]
