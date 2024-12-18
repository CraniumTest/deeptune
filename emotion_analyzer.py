class EmotionAnalyzer:
    def analyze_emotion(self, data):
        if data['heart_rate'] > 70:
            return "happy"
        else:
            return "calm"
