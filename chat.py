from flask import Blueprint, render_template, request
from app.services.chat_service import explain_topic

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/", methods=["GET", "POST"])
def chat():
    explanation = None

    if request.method == "POST":
        topic = request.form["topic"]
        explanation = explain_topic(topic)

    return render_template("chat.html", explanation=explanation)