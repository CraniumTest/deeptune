class UserProfile:
    def __init__(self):
        self.preferences = {}

    def update_profile(self, data):
        self.preferences.update(data.get("music_preferences", {}))

    def update_with_feedback(self, feedback):
        if feedback['user_feedback']['liked']:
            pass
