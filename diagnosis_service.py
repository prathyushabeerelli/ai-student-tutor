def evaluate_diagnosis(answers):
    correct_answers = {
        "q1": "4",
        "q2": "stack",
        "q3": "queue"
    }

    score = 0
    weak_topics = []

    for key in correct_answers:
        user_ans = answers.get(key, "").lower().strip()

        if user_ans == correct_answers[key]:
            score += 1
        else:
            weak_topics.append(key)

    total = len(correct_answers)
    percentage = (score / total) * 100

    if percentage < 40:
        level = "Beginner"
    elif percentage < 70:
        level = "Intermediate"
    else:
        level = "Advanced"

    return {
        "score": score,
        "total": total,
        "percentage": round(percentage, 2),
        "level": level,
        "weak_topics": weak_topics
    }