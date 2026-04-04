from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('categories/<int:tech_id>/', views.CategoryQuestionsListView.as_view(), name='category-questions-list'),
]
