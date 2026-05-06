from flask import Blueprint, render_template, request, session
from app.services.diagnosis_service import evaluate_diagnosis

diagnosis_bp = Blueprint("diagnosis", __name__)

@diagnosis_bp.route("/", methods=["GET", "POST"])
def diagnosis():
    result = None

    if request.method == "POST":
        answers = request.form.to_dict()
        result = evaluate_diagnosis(answers)

        # 🔥 store in session
        session["level"] = result["level"]
        session["weak_topics"] = result["weak_topics"]

    return render_template("diagnosis.html", result=result)