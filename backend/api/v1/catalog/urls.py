from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list-create'),
    path('techs/', views.TechListView.as_view(), name='tech-list-create'),
]
