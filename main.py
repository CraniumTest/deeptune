from deeptune.music_generation import MusicGenerator
from deeptune.user_profile import UserProfile
from deeptune.emotion_analyzer import EmotionAnalyzer
from deeptune.context_detector import ContextDetector

def main():
    user_profile = UserProfile()
    emotion_analyzer = EmotionAnalyzer()
    context_detector = ContextDetector()
    music_generator = MusicGenerator()
    
    user_profile_input = {
        "music_preferences": {
            "genres": ["jazz", "classical"],
            "instruments": ["piano", "violin"]
        },
        "streaming_history": [...]
    }
    
    user_emotion_data = {
        "heart_rate": 76,
        "text_sentiment": "happy"
    }
    
    context_data = {
        "location": "home",
        "time_of_day": "evening"
    }

    user_profile.update_profile(user_profile_input)
    current_emotion = emotion_analyzer.analyze_emotion(user_emotion_data)
    user_context = context_detector.detect_context(context_data)
    music_track = music_generator.generate_music(user_profile, current_emotion, user_context)
    feedback = get_mock_feedback()
    user_profile.update_with_feedback(feedback)
    print("Generated music track details:", music_track)

def get_mock_feedback():
    return {
        "track_id": 123,
        "user_feedback": {
            "liked": True,
            "specific_comments": "Loved the violin intro!"
        }
    }

if __name__ == "__main__":
    main()
