from datetime import datetime

def generate_plan(subjects, exam_date, weak_topics=None, level="Intermediate"):
    today = datetime.today()
    exam = datetime.strptime(exam_date, "%Y-%m-%d")

    days_left = (exam - today).days

    if days_left <= 0:
        return {"Error": "Exam date must be in future"}

    subjects_list = [s.strip() for s in subjects.split(",") if s.strip()]

    if not subjects_list:
        return {"Error": "Enter subjects"}

    plan = {}

    # 🔥 prioritize weak topics
    weighted_subjects = []

    for subject in subjects_list:
        if weak_topics and subject.lower() in [w.lower() for w in weak_topics]:
            weighted_subjects.extend([subject, subject])  # more weight
        else:
            weighted_subjects.append(subject)

    # 🔥 adjust based on level
    if level == "Beginner":
        repeat_factor = 2
    elif level == "Advanced":
        repeat_factor = 1
    else:
        repeat_factor = 1

    weighted_subjects = weighted_subjects * repeat_factor

    for i in range(days_left):
        day = f"Day {i+1}"
        subject = weighted_subjects[i % len(weighted_subjects)]
        plan[day] = subject

    return plan