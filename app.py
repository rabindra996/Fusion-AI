from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ================= DATABASE =================
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            response TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ================= CHATBOT =================
def bot_reply(msg):
    msg = msg.lower()

    # ===== HUGE KNOWLEDGE BASE =====
    data = {
        "python": "Python is an easy and powerful programming language used in AI, web and data science.",
        "java": "Java is used in Android apps and backend systems.",
        "c++": "C++ is used in games and system programming.",
        "html": "HTML is used to create structure of web pages.",
        "css": "CSS is used to design and style websites.",
        "javascript": "JavaScript makes websites interactive.",
        "ai": "AI means Artificial Intelligence 🤖 machines that can think.",
        "machine learning": "Machine learning allows systems to learn from data.",
        "deep learning": "Deep learning uses neural networks.",
        "database": "Database stores and manages data.",
        "sql": "SQL is used to manage databases.",
        "computer": "Computer is an electronic machine that processes data.",
        "cpu": "CPU is the brain of the computer.",
        "ram": "RAM is temporary memory.",
        "os": "Operating system manages system resources.",
        "network": "Network connects computers.",
        "internet": "Internet is global network.",
        "study": "Study daily and revise regularly 📚",
        "exam": "Prepare well and stay confident.",
        "motivation": "You can achieve anything 💪",
        "success": "Success comes from hard work.",
        "project": "This is your Fusion AI chatbot project 🚀",
    }

    # ===== CHAT =====
    if "hello" in msg or "hi" in msg:
        return "Hello 👋 I'm Fusion AI! Ask me anything 😊"

    if "how are you" in msg:
        return "I'm doing great 😄 Hope you're fine!"

    if "bye" in msg:
        return "Goodbye 👋 Keep learning!"

    # ===== SEARCH =====
    for key in data:
        if key in msg:
            return data[key]

    # ===== SMART FALLBACK =====
    if "what" in msg:
        return "That's a good question 🤔 I'm still learning but you're thinking right!"

    if "how" in msg:
        return "Try learning step by step and practice 👍"

    if "why" in msg:
        return "Understanding concepts deeply will help you 🤔"

    if "who" in msg:
        return "Try asking with more details 👀"

    # ===== FINAL =====
    return "Hmm 🤔 I don't know that yet, but keep learning 🚀"

# ================= ROUTES =================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = bot_reply(user_msg)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chats (message, response, time) VALUES (?, ?, ?)",
        (user_msg, reply, str(datetime.now()))
    )
    conn.commit()
    conn.close()

    return jsonify({"response": reply})

# ================= MAIN =================
if __name__ == "__main__":
    app.run(debug=True)