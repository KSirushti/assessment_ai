from django.db import models

from django.db import models


class Question(models.Model):
    LEVEL_CHOICES = [
        ("easy", "Easy"),
        ("intermediate", "Intermediate"),
        ("hard", "Hard"),
    ]

    question_text = models.TextField()
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.level} - {self.question_text[:50]}"


class UserScore(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField()
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username}: {self.proficiency}"
