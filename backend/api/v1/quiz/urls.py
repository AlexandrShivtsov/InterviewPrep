from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('tech/', views.QuizQuestionListView.as_view(), name='quiz-questions-list'), # show all quiz questions for a specific category (tech_id)
]
