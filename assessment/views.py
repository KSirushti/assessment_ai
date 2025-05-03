from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question, UserScore
from .serializers import (
    QuestionSerializer,
    AnswerSubmissionSerializer,
    UserScoreSerializer,
)
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def get_questions(request):
    easy = Question.objects.filter(level="easy")[:30]
    intermediate = Question.objects.filter(level="intermediate")[:15]
    hard = Question.objects.filter(level="hard")[:5]

    questions = list(easy) + list(intermediate) + list(hard)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def submit_answers(request):
    data = request.data
    username = data.get("username")
    answers = data.get("answers", [])

    score = 0
    for answer_data in answers:
        question = get_object_or_404(Question, id=answer_data["question_id"])
        if (
            question.correct_answer.strip().lower()
            == answer_data["user_answer"].strip().lower()
        ):
            if question.level == "easy":
                score += 1
            elif question.level == "intermediate":
                score += 2
            elif question.level == "hard":
                score += 3

    # Determine proficiency
    if score >= 45:
        proficiency = "Advanced"
    elif score >= 30:
        proficiency = "Intermediate"
    else:
        proficiency = "Beginner"

    user_score = UserScore.objects.create(
        username=username, score=score, proficiency=proficiency
    )
    serializer = UserScoreSerializer(user_score)
    return Response(serializer.data)
