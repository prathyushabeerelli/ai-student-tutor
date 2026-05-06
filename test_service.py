def evaluate_test(answers):
    correct = {
        "q1": "4",
        "q2": "stack"
    }

    score = 0

    for key in correct:
        user = answers.get(key, "").lower().strip()
        if user == correct[key]:
            score += 1

    total = len(correct)

    if score == total:
        level = "Strong"
    elif score >= 1:
        level = "Average"
    else:
        level = "Weak"

    return {
        "score": score,
        "total": total,
        "level": level
    }