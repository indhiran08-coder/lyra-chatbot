from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import requests, os, uuid
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

HF_API_KEY = os.getenv("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")
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

def generate_response(user_input, mood):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    prompt = f"""
    You are Lyra, a friendly and caring mental health companion.
    Your tone is warm, understanding, and gentle.
    The user's mood is {mood}.
    User: {user_input}
    Lyra:
    """
    res = requests.post(
        f"https://api-inference.huggingface.co/models/{MODEL}",
        headers=headers,
        json={"inputs": prompt}
    )
    data = res.json()
    if isinstance(data, list) and len(data) > 0:
        return data[0]["generated_text"].split("Lyra:")[-1].strip()
    return "I'm here for you. You can share anything with me."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    mood = request.form.get('mood', 'neutral')
    bot_reply = generate_response(user_message, mood)

    # Voice
    tts = gTTS(bot_reply, lang='en', tld='co.uk')
    filename = f"voice_{uuid.uuid4()}.mp3"
    tts.save(os.path.join('static', filename))

    return jsonify({'response': bot_reply, 'voice': filename})

if __name__ == '__main__':
    app.run(debug=True)
