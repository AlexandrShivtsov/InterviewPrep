from django.shortcuts import render
from rest_framework import generics
from catalog.models import Category
from questions.models import Question
from .serializers import QuestionNestedSerializer
from api.v1.paginators import CustomPagination


# return questions and answers by certain technology category
class CategoryQuestionsListView(generics.ListAPIView):
    serializer_class = QuestionNestedSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        tech_id = self.kwargs.get('tech_id')
        return Question.objects.filter(category_id=tech_id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        tech_id = self.kwargs.get('tech_id')
        try:
            category = Category.objects.get(id=tech_id)
            context['tech'] = category.tech
        except Category.DoesNotExist:
            context['tech'] = None
        return context   