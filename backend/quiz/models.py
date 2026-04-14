from django.db import models
from catalog.models import Category


class Quiz_question(models.Model):
    tech = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quiz_questions')
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tech.tech + ": " + self.question_text[:50]
    

class Quiz_answer(models.Model):
    quiz_question = models.ForeignKey(Quiz_question, on_delete=models.CASCADE, related_name='quiz_answers')
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.quiz_question.question_text[:50] + " - " + self.answer_text[:50]
    