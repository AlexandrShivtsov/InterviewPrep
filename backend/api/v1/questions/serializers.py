from rest_framework import serializers
from questions.models import Question


class QuestionNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answer_text']


