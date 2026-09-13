from flask import Flask, request, jsonify, send_from_directory
from knowledge import knowledge

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/<path:filename>")
def files(filename):
    return send_from_directory(".", filename)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()
    q = question.lower()

    if not question:
        return jsonify({
            "answer": "Please ask me a question. 📚"
        })

    # GREETINGS
    greetings = {
        "hi": "Hi! 👋 I'm your Class 9 SST AI. Ask me anything about History, Geography, Political Science or Economics! 📚",
        "hello": "Hello! 👋 What would you like to learn about in Class 9 SST?",
        "hey": "Hey! 👋 Ready for some Class 9 SST? Ask me a question!",
        "hii": "Hii! 👋 Ask me anything about Class 9 SST!",
        "hiii": "Hiii! 👋 What SST topic are we exploring today?",
        "good morning": "Good morning! ☀️ Ready to learn some SST?",
        "good afternoon": "Good afternoon! 🌤️ What Class 9 SST question do you have?",
        "good evening": "Good evening! 🌆 Ask me anything about Class 9 SST!"
    }

    if q in greetings:
        return jsonify({
            "answer": greetings[q]
        })

    # CREATOR
    creator_questions = [
        "who created you",
        "who made you",
        "who is your creator",
        "who developed you",
        "who built you",
        "who programmed you",
        "who made this ai",
        "who created this ai"
        "who was your father"
    ]
    if q in creator_questions:
        return jsonify({
            "answer": (
                "I was created by Sahil. 🤖✨\n\n"
                "Sahil is a Class 9 student studying at "
                "Daffodil Public School. 📚\n\n"
                "He created me as a Class 9 SST AI learning project."
            )
        })

    # THANK YOU
    thanks = [
        "thanks",
        "thank you",
        "thankyou",
        "thx",
        "thanks bro"
    ]

    if q in thanks:
        return jsonify({
            "answer": "You're welcome! 😊 Keep learning!"
        })

    # EXACT QUESTION
    if q in knowledge:
        answer = knowledge[q]

    else:
        # SMART WORD MATCHING
        answer = None

        ignored_words = {
            "what", "is", "are", "was", "were",
            "the", "a", "an", "of", "to",
            "why", "how", "when", "where",
            "can", "you", "tell", "me",
            "about", "explain", "define",
            "please", "does", "do", "did"
        }

        question_words = set(q.replace("?", "").split())
        important_words = question_words - ignored_words

        best_score = 0

        for key, value in knowledge.items():
            key_words = set(key.split())
            score = len(important_words.intersection(key_words))

            if score > best_score:
                best_score = score
                answer = value

        if best_score == 0:
            answer = None

        # UNKNOWN QUESTION
        if answer is None:
            answer = (
                "I don't know that yet. 🧠\n\n"
                "Ask me anything about Class 9 SST! 📚\n\n"
                "You can ask about:\n"
                "🏛️ Political Science\n"
                "🌍 Geography\n"
                "📜 History\n"
                "💰 Economics"
            )

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(debug=True)