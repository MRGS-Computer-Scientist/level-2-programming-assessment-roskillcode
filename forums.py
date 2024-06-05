class DiscussionForums:
    def __init__(self):
        self.topics = []
        
    def post_topic(self, user, topic):
        self.topics.append({"user": user, "topic": topic})
        print(f"New topic posted by {user}: {topic}")

    def get_topics(self):
        return self.topics