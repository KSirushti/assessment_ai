from django.urls import path
from . import views

urlpatterns = [
    path("generate_questions/", views.generate_questions, name="generate_questions"),
    path("submit_test/", views.submit_test, name="submit_test"),
]
