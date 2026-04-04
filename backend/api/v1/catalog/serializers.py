from rest_framework import serializers
from catalog.models import Category
from questions.models import Question
from api.v1.questions.serializers import QuestionNestedSerializer


class CategorySerializer(serializers.ModelSerializer):
    question_data = QuestionNestedSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'tech', 'question_data']  
        

class TechListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'tech']