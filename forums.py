class DiscussionForums:
    def __init__(self):
        # Initialize the DiscussionForums class with an empty list of topics.
        self.topics = []
        
    def post_topic(self, user, topic):
        # Add a new topic to the list, including the user who posted it.
        self.topics.append({"user": user, "topic": topic})
        print(f"New topic posted by {user}: {topic}")

    def get_topics(self):
        # Return the list of topics.
        return self.topics
