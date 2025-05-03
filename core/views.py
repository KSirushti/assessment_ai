from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import uuid
from .pdf_utils import generate_pdf_report  # We'll create this soon


# Mock question generator
def create_mock_question(index, difficulty):
    return {
        "id": index,
        "question": f"What is {difficulty} question {index}?",
        "options": ["A", "B", "C", "D"],
        "answer": random.choice(["A", "B", "C", "D"]),
        "difficulty": difficulty,
        "skills": [f"{difficulty}_skill"],
    }


@api_view(["POST"])
def generate_questions(request):
    language = request.data.get("language")
    topic = request.data.get("topic")

    questions = []
    index = 0

    for _ in range(30):
        questions.append(create_mock_question(index, "basic"))
        index += 1
    for _ in range(15):
        questions.append(create_mock_question(index, "intermediate"))
        index += 1
    for _ in range(5):
        questions.append(create_mock_question(index, "hard"))
        index += 1

    return Response(questions)


@api_view(["POST"])
def submit_test(request):
    answers = request.data.get("answers", {})
    questions = request.data.get("questions", [])

    correct = 0
    total = len(questions)
    skill_map = {}

    for q in questions:
        qid = str(q["id"])
        if qid in answers and answers[qid] == q["answer"]:
            correct += 1
            for skill in q["skills"]:
                skill_map[skill] = skill_map.get(skill, 0) + 1

    score = round((correct / total) * 100)

    pdf_data = generate_pdf_report(score, questions, answers, skill_map)

    return Response({"score": score, "pdf": pdf_data.hex(), "skills": skill_map})


@api_view(["GET"])
def generate_questions(request):
    return Response({"message": "Questions generated!"})
