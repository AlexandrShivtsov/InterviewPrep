from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('tech-questions/', views.CategoryQuestionsListView.as_view(), name='tech-questions-list'), # show all questions for a specific category (tech_id)
]
