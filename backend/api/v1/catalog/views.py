from django.shortcuts import render
from rest_framework import generics
from catalog.models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   