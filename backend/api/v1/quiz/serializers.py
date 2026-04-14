from rest_framework import serializers
from quiz.models import Quiz_question, Quiz_answer

        
class QuizAnswerNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quiz_answer
        fields = ['id', 'answer_text', 'is_correct']
        
        

class QuizQuestionSerializer(serializers.ModelSerializer):
    
    nested_answers = QuizAnswerNestedSerializer(many=True, read_only=True, source='quiz_answers') 
     
    
    class Meta:
        model = Quiz_question
        fields = ['id', 'question_text', 'nested_answers']
        


