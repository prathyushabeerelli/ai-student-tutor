from flask import Blueprint, render_template, request, session
from app.services.planner_service import generate_plan

planner_bp = Blueprint("planner", __name__)

@planner_bp.route("/", methods=["GET", "POST"])
def planner():
    plan = None

    if request.method == "POST":
        subjects = request.form["subjects"]
        exam_date = request.form["exam_date"]

        level = session.get("level", "Intermediate")
        weak_topics = session.get("weak_topics", [])

        plan = generate_plan(subjects, exam_date, weak_topics, level)

    return render_template("planner.html", plan=plan)