class MusicGenerator:
    def __init__(self):
        pass

    def generate_music(self, user_profile, emotion, context):
        track_details = {
            "genre": user_profile.preferences['genres'][0],
            "tempo": self.determine_tempo(emotion),
            "instrumentation": context['location'],
        }
        return track_details

    def determine_tempo(self, emotion):
        if emotion == "happy":
            return "fast"
        elif emotion == "calm":
            return "slow"
        else:
            return "medium"
