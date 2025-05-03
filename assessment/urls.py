from django.urls import path
from . import views

urlpatterns = [
    path("questions/", views.get_questions),
    path("submit/", views.submit_answers),
]
