from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

# 🧠 Simple mental health chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    if "sad" in user_input or "depressed" in user_input:
        return "I’m really sorry you’re feeling this way. Remember, it’s okay to not be okay sometimes. Want me to tell you a relaxing tip?"
    elif "yes" in user_input:
        return "Try taking a slow deep breath and think about something you’re grateful for today."
    elif "stress" in user_input:
        return "Stress is natural. But you can try the 4-7-8 breathing technique — inhale for 4 seconds, hold for 7, exhale for 8."
    elif "thank" in user_input:
        return "You’re most welcome! I’m always here if you need someone to talk to."
    else:
        return "I’m Lyra 💬, your AI mental health buddy. How are you feeling today?"

# 🎧 Convert text to speech and play it
def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("start response.mp3")

# 🌐 Homepage
@app.route("/")
def home():
    return render_template("index.html")

# 💬 Chatbot endpoint
@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.form["msg"]
    bot_reply = get_response(user_msg)
    speak_text(bot_reply)
    return jsonify({"response": bot_reply})

# 🚀 Main entry point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Important for Render
    app.run(host="0.0.0.0", port=port, debug=True)
