from django.shortcuts import render
from rest_framework import generics
from catalog.models import Category
from . import selectors
from api.v1.questions.serializers import QuestionNestedSerializer
from .serializers import CategorySerializer, TechListSerializer
from api.v1.paginators import CustomPagination

# Create your views here.
# class CategoryListView(generics.ListAPIView):
   
#     serializer_class = QuestionNestedSerializer   
#     pagination_class = CustomPagination
    
#     def get_queryset(self):
#         tech_id = self.request.query_params.get("tech_id")
#         return selectors.get_questions_by_category(tech_id)
    
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         tech_id = self.request.query_params.get("tech_id")
#         try:
#             tech = Category.objects.get(id=tech_id)
#             context['tech'] = tech.tech
#         except Category.DoesNotExist:
#             context['tech'] = None
#         return context
    
# This view is used to get the list of technologies for the dropdown in the frontend
class TechListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = TechListSerializer
