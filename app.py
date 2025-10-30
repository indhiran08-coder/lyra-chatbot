from flask import Flask, render_template, request, jsonify
import random
import nltk
from nltk.stem import WordNetLemmatizer

# Download necessary NLP resources
nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()

# Emotion-based responses
responses = {
    "greeting": [
        "Hey there! 🌸 I'm Lyra, your mental health buddy. How are you feeling today?",
        "Hello beautiful soul! 💖 What’s on your mind?",
        "Hi! 😊 I’m here for you — how are you doing today?"
    ],
    "sad": [
        "I’m really sorry you’re feeling this way 💙. Do you want to talk about what’s making you feel down?",
        "It’s okay to not be okay sometimes. I’m listening. 🕊️",
        "You’re not alone. Want to share what happened?"
    ],
    "happy": [
        "That’s awesome! 😄 I love hearing happy things. What made your day so good?",
        "Yay! 🌈 Keep smiling — you deserve every bit of happiness!",
        "I’m so glad to hear that! 😊"
    ],
    "stressed": [
        "Take a deep breath 🌬️... You’re doing your best. Want me to guide you through a short relaxation exercise?",
        "Stress can be tough 😔, but remember: you’re stronger than you think.",
        "Let’s take a small step together to feel calmer. Would you like that?"
    ],
    "angry": [
        "It’s okay to feel angry 😤. Talking about it can help. What triggered it?",
        "That sounds frustrating. Do you want to let it out? I’m all ears.",
        "Anger often hides pain. Want to tell me what’s beneath it?"
    ],
    "default": [
        "I’m here to listen 🫶. Tell me more.",
        "That sounds interesting — go on!",
        "Hmm, I see... would you like to talk more about that?"
    ]
}

# Simple emotion detection keywords
emotion_keywords = {
    "sad": ["sad", "upset", "unhappy", "depressed", "down"],
    "happy": ["happy", "joy", "good", "great", "excited"],
    "stressed": ["stress", "worried", "anxious", "tired", "pressure"],
    "angry": ["angry", "mad", "furious", "irritated", "annoyed"]
}


def detect_emotion(user_input):
    words = nltk.word_tokenize(user_input.lower())
    lemmatized = [lemmatizer.lemmatize(word) for word in words]
    for emotion, keywords in emotion_keywords.items():
        if any(word in lemmatized for word in keywords):
            return emotion
    return "default"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    emotion = detect_emotion(user_message)
    bot_reply = random.choice(responses.get(emotion, responses["default"]))
    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
