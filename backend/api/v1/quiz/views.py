from django.shortcuts import render
from rest_framework import generics
from catalog.models import Category
from quiz.models import Quiz_question, Quiz_answer
from . import selectors
from .serializers import QuizQuestionSerializer, QuizAnswerNestedSerializer
from api.v1.paginators import QuizPagination


# return questions and answers by certain technology category
# class CategoryQuestionsListView(generics.ListAPIView):
#     serializer_class = QuestionNestedSerializer
#     pagination_class = CustomPagination
    
#     def get_queryset(self):
#         tech_id = self.kwargs.get('tech_id')
#         return Question.objects.filter(category_id=tech_id)
    
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         tech_id = self.kwargs.get('tech_id')
#         try:
#             category = Category.objects.get(id=tech_id)
#             context['tech'] = category.tech
#         except Category.DoesNotExist:
#             context['tech'] = None
#         return context   
    
class QuizQuestionListView(generics.ListAPIView):
    serializer_class = QuizQuestionSerializer
    pagination_class = QuizPagination
    
    def get_queryset(self):
        tech_id = self.request.query_params.get('tech_id')
        return selectors.get_questions_by_category(tech_id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        tech = self.get_queryset()[0].tech.tech if self.get_queryset().exists() else 'Unknown'
        try:
            context['tech'] = tech
        except Category.DoesNotExist:
            context['tech'] = None
        return context
