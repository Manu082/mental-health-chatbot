# Rule-based emotion detection using keywords

def detect_emotion(processed_text):
    """
    Detects emotion from lemmatized text using predefined keyword rules
    """

    emotion_keywords = {
        "sad": ["sad", "lonely", "depress", "down", "unhappy", "hopeless"],
        "happy": ["happy", "joy", "excited", "good", "great", "positive"],
        "angry": ["angry", "mad", "furious", "annoy", "irritate"],
        "anxious": ["anxious", "worry", "nervous", "stress", "fear"],
        "neutral": ["okay", "fine", "normal", "calm"]
    }

    for emotion, keywords in emotion_keywords.items():
        for word in keywords:
            if word in processed_text:
                return emotion

    return "neutral"


def get_response(emotion):
    """
    Returns a supportive response based on detected emotion
    """

    responses = {
        "sad": "I'm sorry you're feeling sad. You're not alone, and things can get better 💙",
        "happy": "That's wonderful to hear! Keep enjoying the positive moments 😊",
        "angry": "I understand your anger. Try taking a deep breath and giving yourself some space 🌿",
        "anxious": "It's okay to feel anxious. Slow breathing and short breaks may help 🌼",
        "neutral": "Thanks for sharing. I'm here whenever you want to talk 🙂"
    }

    return responses.get(emotion, responses["neutral"])


# Testing the rule engine
if __name__ == "__main__":
    test_text = "feel stress anxious today"
    emotion = detect_emotion(test_text)
    print("Detected Emotion:", emotion)
    print("Response:", get_response(emotion))
