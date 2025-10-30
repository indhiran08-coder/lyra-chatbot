# 💫 LYRA — AI Powered Mental Health Chatbot 💬

> “Sometimes, all we need is someone to listen — even if that someone is an AI friend.”

---

## 🌈 Overview

**Lyra** is an **AI-powered mental health companion** designed to offer **empathy, positivity, and relaxation** through friendly conversations.  
It helps users express their feelings, reduce stress, and receive gentle emotional support.  
Built using **Flask**, **Python**, and **modern web technologies**, Lyra provides a warm, interactive, and calming chat experience.  

---

## 🧠 Key Features

✨ **Emotion-Aware Responses** — Understands user feelings (like stress, anxiety, sadness, happiness).  
🔊 **Text-to-Speech (optional)** — Soothing voice replies using `gTTS`.  
💬 **Instant Real-Time Chat** — Built with Flask backend + JavaScript frontend.  
🎨 **Elegant Interface** — Simple, professional, and user-friendly design.  
☁️ **Deployable** — Easily hosted online via Render or other cloud platforms.  

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|------------------|
| 💻 **Backend** | Flask (Python) |
| 🎨 **Frontend** | HTML, CSS, JavaScript |
| 🗣️ **Voice Engine** | gTTS (Google Text-to-Speech) |
| ☁️ **Hosting** | Render |
| 🧠 **Logic** | Rule-based AI chatbot |

---

## 🗂️ Project Structure

lyra-chatbot/
│
├── app.py # Main Flask application
├── requirements.txt # Project dependencies
│
├── templates/
│ └── index.html # Chatbot UI page
│
├── static/
│ ├── style.css # Styling for chatbot
│ └── script.js # Handles chat functionality
│
└── assets/
└── background.mp3 # Optional ambient music

---

## ⚙️ How to Run Locally

```bash
# 1️⃣ Clone the repository
git clone https://github.com/indhiran08-coder/lyra-chatbot.git
cd lyra-chatbot

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the app
python app.py

