from flask import Blueprint, render_template, request
from app.services.test_service import evaluate_test

test_bp = Blueprint("test", __name__)

@test_bp.route("/", methods=["GET", "POST"])
def test():
    result = None

    if request.method == "POST":
        answers = request.form.to_dict()
        result = evaluate_test(answers)

    return render_template("test.html", result=result)